let state = { courses: {} };
let activeCourse = null;
let activePeriodByCourse = {};

const WEIGHTS = { C: 1.0, I: 0.5, S: 0.0 };

const $ = (sel) => document.querySelector(sel);
const esc = (s) => String(s ?? "")
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;");

async function api(url, opts = {}) {
  const response = await fetch(url, {
    headers: opts.body && !(opts.body instanceof FormData) ? { "Content-Type": "application/json" } : undefined,
    ...opts,
  });

  if (!response.ok) {
    let msg = `Error ${response.status}`;
    try {
      const j = await response.json();
      if (j.error) msg = j.error;
    } catch {}
    throw new Error(msg);
  }

  const ct = response.headers.get("content-type") || "";
  if (ct.includes("application/json")) return response.json();
  return response;
}

function calcGrade(marks, numClasses, exigencyPct) {
  if (!marks || !numClasses) return null;
  const absenceCount = marks.filter((m) => m === "A").length;
  const effectiveClasses = Math.max(0, numClasses - absenceCount);
  if (effectiveClasses <= 0) return null;
  const exig = (exigencyPct || 60) / 100;
  const score = marks.reduce((a, m) => a + (m === "A" ? 0 : (WEIGHTS[m] ?? 0)), 0);
  const maxScore = effectiveClasses;
  const passingScore = maxScore * exig;
  let grade;
  if (score >= passingScore) {
    grade = 4.0 + 3.0 * ((score - passingScore) / Math.max(1e-9, maxScore - passingScore));
  } else {
    grade = 1.0 + 3.0 * (score / Math.max(1e-9, passingScore));
  }
  return Math.max(1.0, Math.min(7.0, grade));
}

function studentPeriodGrade(course, period, studentName) {
  if (!period?.classes?.length) return null;
  const marks = period.marks?.[studentName] || [];
  return calcGrade(marks, period.classes.length, period.exigency || 60);
}

function studentAvg(course, studentName) {
  const grades = [];
  (course.periods || []).forEach((p) => {
    const g = studentPeriodGrade(course, p, studentName);
    if (g !== null) grades.push(g);
  });
  if (!grades.length) return null;
  return grades.reduce((a, b) => a + b, 0) / grades.length;
}

function fmt(g) {
  return g === null || g === undefined ? "-" : g.toFixed(1);
}

async function loadState() {
  state = await api("/api/state");
  const names = Object.keys(state.courses).sort();
  if (!activeCourse || !state.courses[activeCourse]) activeCourse = names[0] || null;
  render();
}

function render() {
  renderCourseTabs();
  renderPanels();
}

function renderCourseTabs() {
  const tabs = $("#courseTabs");
  const names = Object.keys(state.courses).sort();
  if (!names.length) {
    tabs.innerHTML = '<p class="p-3 text-slate-400 text-sm">Sin cursos. Agrega uno.</p>';
    return;
  }
  tabs.innerHTML = names.map((name) => `
    <button class="course-tab py-2.5 px-5 text-sm font-semibold text-slate-500 rounded-t-lg flex-shrink-0 ${activeCourse === name ? "active" : ""}" data-course="${esc(name)}">${esc(name)}</button>
  `).join("");

  tabs.querySelectorAll("button[data-course]").forEach((btn) => {
    btn.onclick = () => {
      activeCourse = btn.dataset.course;
      render();
    };
  });
}

function renderPanels() {
  const container = $("#coursePanels");
  const names = Object.keys(state.courses).sort();
  container.innerHTML = names.map((name) => {
    const active = activeCourse === name ? "active" : "";
    return `<section class="course-panel ${active}" id="panel-${esc(name)}">${buildCoursePanel(name)}</section>`;
  }).join("");

  names.forEach(bindPanel);
}

function buildCoursePanel(courseName) {
  const course = state.courses[courseName];
  const periods = course.periods || [];
  let activePeriod = activePeriodByCourse[courseName] || periods.at(-1)?.id || null;
  if (!periods.some((p) => p.id === activePeriod)) activePeriod = periods.at(-1)?.id || null;
  activePeriodByCourse[courseName] = activePeriod;

  let html = `<div class="bg-white rounded-b-xl rounded-tr-xl border border-slate-200 border-t-0 shadow-sm">`;
  html += `<div class="flex flex-wrap gap-3 items-center justify-between p-4 border-b border-slate-100">
      <div class="flex gap-2 flex-wrap">
        <button class="add-student-btn bg-indigo-50 text-indigo-700 font-bold py-1.5 px-3 rounded-lg hover:bg-indigo-100 text-sm" data-course="${esc(courseName)}">+ Estudiante</button>
        <label class="bg-slate-100 text-slate-700 font-bold py-1.5 px-3 rounded-lg hover:bg-slate-200 text-sm cursor-pointer">Carga masiva Excel
          <input type="file" accept=".xlsx,.xls" class="hidden excel-input" data-course="${esc(courseName)}">
        </label>
        <button class="add-period-btn bg-emerald-50 text-emerald-700 font-bold py-1.5 px-3 rounded-lg hover:bg-emerald-100 text-sm" data-course="${esc(courseName)}">+ Periodo</button>
      </div>
      <div class="flex gap-2 flex-wrap">
        <button class="pdf-individual-btn bg-indigo-600 text-white font-bold py-1.5 px-3 rounded-lg hover:bg-indigo-700 text-sm" data-course="${esc(courseName)}">PDF Individual</button>
        <button class="pdf-group-btn bg-violet-600 text-white font-bold py-1.5 px-3 rounded-lg hover:bg-violet-700 text-sm" data-course="${esc(courseName)}">PDF Grupal</button>
        <button class="delete-course-btn bg-red-50 text-red-600 font-bold py-1.5 px-3 rounded-lg hover:bg-red-100 text-sm" data-course="${esc(courseName)}">Eliminar curso</button>
      </div>
    </div>`;

  if (!periods.length) {
    html += '<div class="p-8 text-center text-slate-400">No hay periodos. Crea el primero.</div></div>';
    return html;
  }

  html += `<div class="flex gap-1 p-3 border-b border-slate-100 overflow-x-auto bg-slate-50">`;
  periods.forEach((p) => {
    const active = p.id === activePeriod ? "active" : "hover:bg-slate-200";
    html += `<button class="period-tab py-1.5 px-4 rounded-lg text-sm font-semibold flex-shrink-0 text-slate-600 ${active}" data-course="${esc(courseName)}" data-period="${esc(p.id)}">${esc(p.name)}</button>`;
  });
  html += `</div>`;

  const period = periods.find((p) => p.id === activePeriod);
  if (!period) return html + "</div>";

  html += `<div class="p-4 border-b border-slate-100 bg-slate-50 flex flex-wrap gap-4 items-center">
      <div class="flex items-center gap-2"><span class="text-sm font-semibold text-slate-600">Periodo:</span>
      <input type="text" class="period-name-input w-44" value="${esc(period.name)}" data-course="${esc(courseName)}" data-period="${esc(period.id)}"></div>
      <div class="flex items-center gap-2"><span class="text-sm font-semibold text-slate-600">Exigencia:</span>
      <input type="number" min="1" max="100" class="period-exig-input w-20" value="${period.exigency || 60}" data-course="${esc(courseName)}" data-period="${esc(period.id)}"><span>%</span></div>
      <button class="add-class-btn bg-white border border-slate-300 text-slate-700 font-semibold py-1.5 px-3 rounded-lg hover:bg-slate-100 text-sm" data-course="${esc(courseName)}" data-period="${esc(period.id)}">+ Clase</button>
      <button class="delete-period-btn text-red-400 hover:text-red-600 text-sm font-semibold ml-auto" data-course="${esc(courseName)}" data-period="${esc(period.id)}">Eliminar periodo</button>
    </div>`;

  const classes = period.classes || [];
  if (!classes.length) return html + '<div class="p-8 text-center text-slate-400">Sin clases en este periodo.</div></div>';

  const students = (course.students || []).filter((s) => s.active !== false).sort((a, b) => a.name.localeCompare(b.name));

  html += `<div class="overflow-x-auto"><table class="w-full text-sm"><thead><tr class="border-b border-slate-200">
    <th class="text-left p-3 font-semibold text-slate-600 sticky left-0 bg-white z-10 min-w-56">Estudiante</th>`;

  classes.forEach((cls, i) => {
    html += `<th class="p-2 text-center font-semibold text-slate-500 min-w-28">
      <div class="flex flex-col items-center gap-1">
        <span class="text-xs text-slate-400">C${i + 1}</span>
        <input type="text" class="class-label-input text-center text-xs w-24 py-0.5" value="${esc(cls.label || "")}" data-course="${esc(courseName)}" data-period="${esc(period.id)}" data-class-idx="${i}">
        <button class="delete-class-btn text-red-300 hover:text-red-500 text-xs" data-course="${esc(courseName)}" data-period="${esc(period.id)}" data-class-idx="${i}">&times;</button>
      </div></th>`;
  });

  html += `<th class="p-3 text-center font-semibold text-slate-600 min-w-20">Nota</th>
    <th class="p-3 text-center font-semibold text-slate-600 min-w-20">Prom.</th>
  </tr></thead><tbody>`;

  students.forEach((st) => {
    const marks = period.marks?.[st.name] || [];
    const g = studentPeriodGrade(course, period, st.name);
    const avg = studentAvg(course, st.name);
    const gColor = g !== null ? (g >= 4.0 ? "text-blue-600" : "text-red-600") : "text-slate-400";
    const aColor = avg !== null ? (avg >= 4.0 ? "text-blue-500" : "text-red-500") : "text-slate-300";

    html += `<tr class="border-b border-slate-100">
      <td class="p-3 sticky left-0 bg-white z-10">
        <div class="flex items-center justify-between gap-2">
          <span class="font-medium text-slate-800 text-sm">${esc(st.name)}</span>
          <button class="remove-student-btn text-slate-300 hover:text-red-400 text-xs" data-course="${esc(courseName)}" data-student="${esc(st.name)}">&times;</button>
        </div>
      </td>`;

    classes.forEach((_, i) => {
      const m = marks[i] || "";
      const cls = m === "C" ? "mark-C" : m === "I" ? "mark-I" : m === "S" ? "mark-S" : m === "A" ? "mark-A" : "mark-none";
      html += `<td class="p-2 text-center"><button class="mark-btn ${cls} rounded-lg py-1 px-3 text-xs" data-course="${esc(courseName)}" data-period="${esc(period.id)}" data-student="${esc(st.name)}" data-class-idx="${i}">${m || "&nbsp;&nbsp;&nbsp;"}</button></td>`;
    });

    html += `<td class="p-3 text-center font-bold text-lg ${gColor}">${fmt(g)}</td>
      <td class="p-3 text-center font-semibold text-sm ${aColor}">${fmt(avg)}</td>
    </tr>`;
  });

  html += `</tbody></table></div></div>`;
  return html;
}

function nextMark(cur) {
  if (!cur) return "C";
  if (cur === "C") return "I";
  if (cur === "I") return "S";
  if (cur === "S") return "A";
  return "";
}

function bindPanel(courseName) {
  const panel = document.querySelector(`#panel-${CSS.escape(courseName)}`);
  if (!panel) return;

  panel.querySelectorAll(".period-tab").forEach((btn) => {
    btn.onclick = () => {
      activePeriodByCourse[courseName] = btn.dataset.period;
      render();
    };
  });

  panel.querySelector(".add-student-btn")?.addEventListener("click", async () => {
    const name = prompt("Nombre del estudiante:");
    if (!name?.trim()) return;
    await api(`/api/course/${encodeURIComponent(courseName)}/student`, { method: "POST", body: JSON.stringify({ name: name.trim() }) });
    await loadState();
  });

  panel.querySelector(".excel-input")?.addEventListener("change", async (e) => {
    const f = e.target.files?.[0];
    if (!f) return;
    const fd = new FormData();
    fd.append("file", f);
    const res = await api(`/api/course/${encodeURIComponent(courseName)}/upload-excel`, { method: "POST", body: fd });
    alert(`Se agregaron ${res.added} estudiantes.`);
    e.target.value = "";
    await loadState();
  });

  panel.querySelector(".add-period-btn")?.addEventListener("click", async () => {
    const name = prompt("Nombre del periodo:", new Date().toLocaleString("es-CL", { month: "long", year: "numeric" }));
    if (!name?.trim()) return;
    await api(`/api/course/${encodeURIComponent(courseName)}/period`, { method: "POST", body: JSON.stringify({ name: name.trim() }) });
    await loadState();
  });

  panel.querySelector(".add-class-btn")?.addEventListener("click", async (e) => {
    const periodId = e.target.dataset.period;
    const label = prompt("Etiqueta de la clase:", "Clase") || "Clase";
    await api(`/api/course/${encodeURIComponent(courseName)}/period/${encodeURIComponent(periodId)}/class`, { method: "POST", body: JSON.stringify({ label }) });
    await loadState();
  });

  panel.querySelectorAll(".delete-class-btn").forEach((btn) => btn.onclick = async () => {
    if (!confirm("¿Eliminar clase y marcas?")) return;
    await api(`/api/course/${encodeURIComponent(courseName)}/period/${encodeURIComponent(btn.dataset.period)}/class/${btn.dataset.classIdx}`, { method: "DELETE" });
    await loadState();
  });

  panel.querySelectorAll(".class-label-input").forEach((inp) => inp.onchange = async () => {
    await api(`/api/course/${encodeURIComponent(courseName)}/period/${encodeURIComponent(inp.dataset.period)}/class/${inp.dataset.classIdx}`, { method: "PUT", body: JSON.stringify({ label: inp.value }) });
    await loadState();
  });

  panel.querySelector(".period-name-input")?.addEventListener("change", async (e) => {
    await api(`/api/course/${encodeURIComponent(courseName)}/period/${encodeURIComponent(e.target.dataset.period)}`, { method: "PUT", body: JSON.stringify({ name: e.target.value }) });
    await loadState();
  });

  panel.querySelector(".period-exig-input")?.addEventListener("change", async (e) => {
    await api(`/api/course/${encodeURIComponent(courseName)}/period/${encodeURIComponent(e.target.dataset.period)}`, { method: "PUT", body: JSON.stringify({ exigency: Number(e.target.value || 60) }) });
    await loadState();
  });

  panel.querySelector(".delete-period-btn")?.addEventListener("click", async (e) => {
    if (!confirm("¿Eliminar periodo?")) return;
    await api(`/api/course/${encodeURIComponent(courseName)}/period/${encodeURIComponent(e.target.dataset.period)}`, { method: "DELETE" });
    await loadState();
  });

  panel.querySelector(".delete-course-btn")?.addEventListener("click", async () => {
    if (!confirm(`¿Eliminar curso ${courseName}?`)) return;
    await api(`/api/course/${encodeURIComponent(courseName)}`, { method: "DELETE" });
    activeCourse = null;
    await loadState();
  });

  panel.querySelectorAll(".remove-student-btn").forEach((btn) => btn.onclick = async () => {
    if (!confirm(`¿Eliminar a ${btn.dataset.student}?`)) return;
    await api(`/api/course/${encodeURIComponent(courseName)}/student/${encodeURIComponent(btn.dataset.student)}`, { method: "DELETE" });
    await loadState();
  });

  panel.querySelectorAll(".mark-btn").forEach((btn) => btn.onclick = async () => {
    const cur = btn.textContent.trim() || "";
    const mark = nextMark(cur === "" || cur === "\u00a0\u00a0\u00a0" ? "" : cur);
    await api(`/api/course/${encodeURIComponent(courseName)}/period/${encodeURIComponent(btn.dataset.period)}/mark`, {
      method: "POST",
      body: JSON.stringify({ student: btn.dataset.student, class_idx: Number(btn.dataset.classIdx), mark }),
    });
    await loadState();
  });

  panel.querySelector(".pdf-individual-btn")?.addEventListener("click", () => {
    window.open(`/api/course/${encodeURIComponent(courseName)}/report/individual.pdf`, "_blank");
  });
  panel.querySelector(".pdf-group-btn")?.addEventListener("click", () => {
    window.open(`/api/course/${encodeURIComponent(courseName)}/report/group.pdf`, "_blank");
  });
}

$("#addCourseBtn").addEventListener("click", async () => {
  const name = prompt("Nombre del curso (ej: 2C):");
  if (!name?.trim()) return;
  await api("/api/course", { method: "POST", body: JSON.stringify({ name: name.trim() }) });
  activeCourse = name.trim().toUpperCase();
  await loadState();
});

$("#exportBtn").addEventListener("click", () => {
  window.open("/api/export/json", "_blank");
});

$("#importJsonInput").addEventListener("change", async (e) => {
  const f = e.target.files?.[0];
  if (!f) return;
  if (!confirm("¿Importar y reemplazar los datos actuales?")) {
    e.target.value = "";
    return;
  }
  const fd = new FormData();
  fd.append("file", f);
  await api("/api/import/json", { method: "POST", body: fd });
  e.target.value = "";
  await loadState();
});

loadState().catch((err) => {
  alert(err.message);
});
