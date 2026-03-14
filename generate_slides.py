#!/usr/bin/env python3
"""
Generador de Presentaciones HTML con Diapositivas Interactivas.
Lee las planificaciones de Unidad 1 y genera una presentación por clase.
"""

import os
import sys
import re

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Instalando beautifulsoup4...")
    os.system(f'"{sys.executable}" -m pip install beautifulsoup4')
    from bs4 import BeautifulSoup

# ─────────────────────────── CONFIGURACIÓN ───────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

THEMES = {
    "1ro Medio": {
        "primary": "#1565c0",
        "primary_dark": "#0d47a1",
        "primary_light": "#42a5f5",
        "gradient": "linear-gradient(135deg, #0d47a1, #1976d2)",
        "bg_light": "#e3f2fd",
    },
    "3ro Medio": {
        "primary": "#c62828",
        "primary_dark": "#b71c1c",
        "primary_light": "#ef5350",
        "gradient": "linear-gradient(135deg, #b71c1c, #d32f2f)",
        "bg_light": "#ffebee",
    },
    "4to Medio": {
        "primary": "#6a1b9a",
        "primary_dark": "#4a148c",
        "primary_light": "#ab47bc",
        "gradient": "linear-gradient(135deg, #4a148c, #7b1fa2)",
        "bg_light": "#f3e5f5",
    },
}

SPECIALTY_MAP = {
    "automotriz": "Mecánica Automotriz",
    "electricidad": "Electricidad",
    "electronica": "Electrónica",
    "grafica": "Gráfica",
    "industrial": "Mecánica Industrial",
}


# ─────────────────────────── PARSING ───────────────────────────
def get_specialty(filename):
    for key, name in SPECIALTY_MAP.items():
        if key in filename.lower():
            return name
    return ""


def inner_html(tag):
    if tag is None:
        return ""
    return "".join(str(c) for c in tag.children)


def parse_planificacion(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    header = soup.find("div", class_="header")
    unit_title = ""
    if header:
        h2 = header.find("h2")
        if h2:
            unit_title = h2.get_text(strip=True)

    clases = []
    for card in soup.find_all("div", class_="clase-card"):
        c = {}

        hdr = card.find("div", class_="clase-header")
        if hdr:
            num = hdr.find("span", class_="clase-num")
            fecha = hdr.find("span", class_="clase-fecha")
            c["number"] = num.get_text(strip=True) if num else ""
            c["date"] = fecha.get_text(strip=True) if fecha else ""
            c["oas"] = [b.get_text(strip=True) for b in hdr.find_all("span", class_="badge")]
            c["is_eval"] = "evaluacion" in (card.get("class") or [])

        obj = card.find("div", class_="objetivo")
        if obj:
            text = obj.get_text(strip=True)
            text = re.sub(r"^Objetivo de la clase\s*(\(Bloom\))?\s*:\s*", "", text)
            c["objective"] = text
        else:
            c["objective"] = ""

        c["phases"] = []
        for fase in card.find_all("div", class_="fase"):
            ph = {}
            title_sp = fase.find("span", class_="fase-title")
            if title_sp:
                ph["title"] = title_sp.get_text(strip=True)
                cls = title_sp.get("class") or []
                if "fase-inicio" in cls:
                    ph["type"] = "inicio"
                elif "fase-desarrollo" in cls:
                    ph["type"] = "desarrollo"
                elif "fase-cierre" in cls:
                    ph["type"] = "cierre"
                else:
                    ph["type"] = "other"

            content = fase.find("div", class_="fase-content")
            if content:
                ph["html"] = inner_html(content)

                # Split desarrollo activities
                if ph.get("type") == "desarrollo":
                    ol = content.find("ol", recursive=False)
                    if ol:
                        acts = []
                        for li in ol.find_all("li", recursive=False):
                            acts.append(inner_html(li))
                        ph["activities"] = acts
                        # Preamble (text before <ol>)
                        preamble = []
                        for sib in ol.previous_siblings:
                            s = str(sib).strip()
                            if s:
                                preamble.insert(0, s)
                        ph["preamble"] = "".join(preamble) if preamble else ""
                    else:
                        ph["activities"] = []
                        ph["preamble"] = ""

            c["phases"].append(ph)

        rec = card.find("div", class_="recursos")
        if rec:
            c["resources"] = rec.get_text(strip=True)
            c["resources"] = re.sub(r"^(📦\s*)?Recursos:\s*", "", c["resources"])
        else:
            c["resources"] = ""

        ev = card.find("div", class_="evaluacion-box")
        c["evaluation"] = inner_html(ev) if ev else ""

        clases.append(c)

    return {"unit_title": unit_title, "classes": clases}


# ─────────────────────────── HTML TEMPLATE ───────────────────────────
CSS_TEMPLATE = r"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700&display=swap');

:root {
    --primary: %%PRIMARY%%;
    --primary-dark: %%PRIMARY_DARK%%;
    --primary-light: %%PRIMARY_LIGHT%%;
    --gradient: %%GRADIENT%%;
    --bg-light: %%BG_LIGHT%%;
    --inicio: #2e7d32;  --inicio-light: #e8f5e9;
    --desarrollo: #1565c0; --desarrollo-light: #e3f2fd;
    --cierre: #6a1b9a;  --cierre-light: #f3e5f5;
    --text: #1a1a2e;  --text-light: #555;
    --white: #ffffff;
    --shadow: 0 8px 32px rgba(0,0,0,0.10);
}

* { margin:0; padding:0; box-sizing:border-box; }

html, body {
    width:100%; height:100%; overflow:hidden;
    font-family:'Inter','Segoe UI',sans-serif;
    background:#0a0a1a;
}

/* ── Slide core ── */
.presentation { width:100%; height:100%; position:relative; }

.slide {
    position:absolute; inset:0;
    display:flex; align-items:center; justify-content:center;
    opacity:0; transform:translateX(50px);
    transition: opacity .55s cubic-bezier(.4,0,.2,1),
                transform .55s cubic-bezier(.4,0,.2,1);
    pointer-events:none;
    padding:50px 60px;
    background:var(--white);
    overflow-y:auto;
}
.slide.active  { opacity:1; transform:translateX(0); pointer-events:auto; z-index:10; }
.slide.exit-l  { opacity:0; transform:translateX(-50px); }

.slide-content { max-width:960px; width:100%; text-align:center; }

/* ── Title slide ── */
.slide-title { background:var(--gradient); color:var(--white); }
.slide-title .deco { display:flex; align-items:center; justify-content:center; gap:14px; margin-bottom:28px; }
.slide-title .deco-line { width:70px; height:2px; background:rgba(255,255,255,.35); }
.slide-title .deco-dot  { width:10px; height:10px; border:2px solid rgba(255,255,255,.5); border-radius:50%; }
.slide-title .cls-num {
    font-family:'Playfair Display',serif; font-size:3.8em; font-weight:700;
    margin-bottom:12px; text-shadow:0 4px 18px rgba(0,0,0,.18);
    animation: fadeUp .8s ease-out;
}
.slide-title .unit-t  { font-size:1.5em; font-weight:300; margin-bottom:18px; opacity:.95; animation:fadeUp .8s ease-out .12s both; }
.slide-title .lvl     { font-size:1.05em; font-weight:500; opacity:.85; animation:fadeUp .8s ease-out .22s both; }
.slide-title .spec    { font-size:.95em; opacity:.78; margin-top:2px; animation:fadeUp .8s ease-out .28s both; }
.slide-title .dt      { font-size:.9em; opacity:.65; margin-top:8px; animation:fadeUp .8s ease-out .34s both; }
.oa-wrap { display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin-top:22px; animation:fadeUp .8s ease-out .4s both; }
.oa-badge { background:rgba(255,255,255,.18); padding:5px 14px; border-radius:18px; font-size:.82em; font-weight:600; border:1px solid rgba(255,255,255,.25); backdrop-filter:blur(8px); }
.eval-badge { background:#ff6f00; padding:5px 14px; border-radius:18px; font-size:.82em; font-weight:700; }
.hint { margin-top:36px; font-size:.82em; opacity:.45; animation:pulse 2.2s ease-in-out infinite; }

/* ── Objective slide ── */
.slide-obj { background:linear-gradient(135deg,#fff8e1,#fff3e0); }
.slide-obj .ico { font-size:3.2em; margin-bottom:16px; animation:popIn .55s ease-out; }
.slide-obj h2 { font-size:1.9em; color:#ef6c00; margin-bottom:24px; }
.obj-box {
    background:var(--white); padding:28px 36px; border-radius:14px;
    box-shadow:var(--shadow); border-left:5px solid #ef6c00;
    text-align:left; font-size:1.2em; line-height:1.65; color:var(--text);
    animation:fadeUp .55s ease-out .15s both;
}

/* ── Phase colors ── */
.ph-inicio     { background:var(--inicio-light); }
.ph-desarrollo { background:var(--desarrollo-light); }
.ph-cierre     { background:var(--cierre-light); }
.ph-inicio     h2, .ph-inicio .act-n     { color:var(--inicio); }
.ph-desarrollo h2, .ph-desarrollo .act-n { color:var(--desarrollo); }
.ph-cierre     h2, .ph-cierre .act-n     { color:var(--cierre); }
.ph-inicio     .badge-ph  { background:var(--inicio); }
.ph-desarrollo .badge-ph  { background:var(--desarrollo); }
.ph-cierre     .badge-ph  { background:var(--cierre); }
.ph-inicio     .hdr-bar   { border-color:var(--inicio); }
.ph-desarrollo .hdr-bar   { border-color:var(--desarrollo); }
.ph-cierre     .hdr-bar   { border-color:var(--cierre); }

/* ── Phase header slide ── */
.slide-phdr .ico { font-size:3.6em; margin-bottom:12px; animation:popIn .55s ease-out; }
.slide-phdr h2   { font-size:2.5em; font-weight:800; margin-bottom:8px; }
.slide-phdr .sub { font-size:1.15em; color:var(--text-light); }
.slide-phdr .cnt { margin-top:12px; font-size:1em; opacity:.6; }
.slide-phdr .preamble { margin-top:18px; font-size:1em; text-align:center; color:var(--text); }
.slide-phdr .preamble b { color:var(--primary-dark); }

/* ── Activity / Phase content slide ── */
.slide-act .slide-content, .slide-ph .slide-content { text-align:left; }

.hdr-bar {
    display:flex; align-items:center; gap:12px;
    margin-bottom:22px; padding-bottom:10px; border-bottom:3px solid;
}
.hdr-bar h2 { font-size:1.7em; flex:1; }
.badge-ph { padding:4px 12px; border-radius:10px; color:var(--white); font-weight:600; font-size:.82em; }
.act-n { font-size:1.35em; font-weight:700; }

.body-text {
    font-size:1.12em; line-height:1.72; color:var(--text);
    animation:fadeUp .45s ease-out .08s both;
}
.body-text b { font-weight:600; }
.body-text em {
    color:#bf360c; font-style:italic;
    background:#fff3e0; padding:1px 5px; border-radius:3px;
}
.body-text ul, .body-text ol { margin-left:22px; margin-top:8px; }
.body-text li { margin-bottom:7px; }
.body-text table { width:100%; border-collapse:collapse; margin:12px 0; font-size:.92em; }
.body-text th { background:var(--primary); color:white; padding:8px 10px; text-align:left; }
.body-text td { padding:7px 10px; border-bottom:1px solid #e0e0e0; }

/* ── Resources slide ── */
.slide-res { background:linear-gradient(135deg,#e8f5e9,#f1f8e9); }
.slide-res .ico { font-size:3.2em; margin-bottom:16px; }
.slide-res h2 { font-size:1.9em; color:#2e7d32; margin-bottom:22px; }
.res-box {
    background:var(--white); padding:24px 32px; border-radius:14px;
    box-shadow:var(--shadow); border-left:5px solid #2e7d32;
    text-align:left; font-size:1.12em; line-height:1.7;
}

/* ── Evaluation slide ── */
.slide-eval { background:linear-gradient(135deg,#fce4ec,#fff3e0); }
.slide-eval .ico { font-size:3.2em; margin-bottom:16px; }
.slide-eval h2 { font-size:1.9em; color:#c62828; margin-bottom:22px; }
.eval-box {
    background:var(--white); padding:24px 32px; border-radius:14px;
    box-shadow:var(--shadow); border-left:5px solid #c62828;
    text-align:left; font-size:1.05em; line-height:1.7;
}
.eval-box table { width:100%; border-collapse:collapse; margin:12px 0; }
.eval-box th { background:#c62828; color:white; padding:8px 10px; text-align:left; font-size:.88em; }
.eval-box td { padding:7px 10px; border-bottom:1px solid #eee; font-size:.88em; }

/* ── End slide ── */
.slide-end { background:var(--gradient); color:var(--white); }
.slide-end .end-ico { font-size:3.8em; margin-bottom:16px; animation:popIn .55s ease-out; }
.slide-end h2 { font-size:2.4em; font-weight:700; margin-bottom:12px; color:var(--white); }
.slide-end .sub { font-size:1.05em; opacity:.78; margin-bottom:10px; }
.slide-end .msg { font-size:1.25em; opacity:.9; }

/* ── Navigation ── */
.nav {
    position:fixed; bottom:22px; left:50%; transform:translateX(-50%);
    display:flex; gap:12px; z-index:100;
}
.nav button {
    width:46px; height:46px; border-radius:50%; border:none;
    background:rgba(0,0,0,.12); color:var(--text); font-size:1.2em;
    cursor:pointer; transition:all .25s; display:flex; align-items:center; justify-content:center;
    backdrop-filter:blur(8px);
}
.nav button:hover { background:rgba(0,0,0,.25); transform:scale(1.08); }

/* ── Progress ── */
.prog-wrap { position:fixed; top:0; left:0; width:100%; height:4px; background:rgba(0,0,0,.08); z-index:100; }
.prog-bar  { height:100%; background:var(--primary); transition:width .4s ease; border-radius:0 2px 2px 0; }
.counter   {
    position:fixed; bottom:28px; right:28px; font-size:.82em; color:var(--text-light);
    z-index:100; background:rgba(255,255,255,.75); padding:3px 10px; border-radius:10px;
    backdrop-filter:blur(8px);
}

/* ── Animations ── */
@keyframes fadeUp {
    from { opacity:0; transform:translateY(24px); }
    to   { opacity:1; transform:translateY(0); }
}
@keyframes popIn {
    0%  { opacity:0; transform:scale(.3); }
    55% { opacity:1; transform:scale(1.05); }
    75% { transform:scale(.96); }
    100%{ transform:scale(1); }
}
@keyframes pulse {
    0%,100% { opacity:.45; }
    50%     { opacity:.75; }
}

/* ── Responsive ── */
@media (max-width:900px) {
    .slide { padding:24px 20px; }
    .slide-title .cls-num { font-size:2.6em; }
    .slide-title .unit-t  { font-size:1.15em; }
    .obj-box, .res-box, .eval-box { padding:18px 20px; font-size:1em; }
    .body-text { font-size:1em; }
    .nav button { width:38px; height:38px; font-size:1em; }
}
@media print {
    .slide { position:relative!important; opacity:1!important; transform:none!important;
             page-break-after:always; height:auto; min-height:100vh; }
    .nav,.prog-wrap,.counter { display:none; }
}
"""

JS_TEMPLATE = r"""
let cur = 0;
const slides = document.querySelectorAll('.slide');
const N = slides.length;
const bar = document.getElementById('bar');
const ctr = document.getElementById('ctr');

function go(idx, dir) {
    if (idx < 0 || idx >= N) return;
    const old = slides[cur];
    old.classList.remove('active');
    if (dir === 1) old.classList.add('exit-l');
    setTimeout(() => old.classList.remove('exit-l'), 600);
    cur = idx;
    slides[cur].classList.add('active');
    bar.style.width = ((cur+1)/N*100)+'%';
    ctr.textContent = (cur+1)+' / '+N;
}
function next() { go(cur+1, 1); }
function prev() { go(cur-1, -1); }

document.addEventListener('keydown', e => {
    if (e.key==='ArrowRight'||e.key===' '||e.key==='Enter') { e.preventDefault(); next(); }
    else if (e.key==='ArrowLeft'||e.key==='Backspace') { e.preventDefault(); prev(); }
    else if (e.key==='Home') { e.preventDefault(); go(0,-1); }
    else if (e.key==='End')  { e.preventDefault(); go(N-1,1); }
});

let tx=0;
document.addEventListener('touchstart', e => { tx=e.changedTouches[0].screenX; });
document.addEventListener('touchend', e => {
    const d=tx-e.changedTouches[0].screenX;
    if (Math.abs(d)>50) { d>0?next():prev(); }
});

document.querySelector('.presentation').addEventListener('click', e => {
    if (!e.target.closest('.nav')) next();
});

slides[0].classList.add('active');
bar.style.width = (1/N*100)+'%';
"""


# ─────────────────────────── SLIDE BUILDER ───────────────────────────
PHASE_CFG = {
    "inicio":     {"ico": "🟢", "en": "WARM-UP",     "es": "Inicio",     "cls": "ph-inicio"},
    "desarrollo": {"ico": "🔵", "en": "DEVELOPMENT", "es": "Desarrollo", "cls": "ph-desarrollo"},
    "cierre":     {"ico": "🟣", "en": "CLOSING",     "es": "Cierre",     "cls": "ph-cierre"},
}


def build_slides(clase, level, specialty, unit_title, theme):
    slides = []
    cn = clase["number"]
    dt = clase.get("date", "")
    oas = " ".join(f'<span class="oa-badge">{o}</span>' for o in clase.get("oas", []))
    ev_b = '<span class="eval-badge">📝 EVALUACIÓN</span>' if clase.get("is_eval") else ""
    sp_line = f'<p class="spec">{specialty}</p>' if specialty else ""

    # 1 ─ Title
    slides.append(f"""
    <section class="slide slide-title">
      <div class="slide-content">
        <div class="deco"><div class="deco-line"></div><div class="deco-dot"></div><div class="deco-line"></div></div>
        <h1 class="cls-num">{cn}</h1>
        <h2 class="unit-t">{unit_title}</h2>
        <p class="lvl">{level}</p>
        {sp_line}
        <p class="dt">{dt}</p>
        <div class="oa-wrap">{oas} {ev_b}</div>
        <p class="hint">▶ Presiona una tecla o haz clic para comenzar</p>
      </div>
    </section>""")

    # 2 ─ Objective
    slides.append(f"""
    <section class="slide slide-obj">
      <div class="slide-content">
        <div class="ico">🎯</div>
        <h2>Objetivo de la Clase</h2>
        <div class="obj-box"><p>{clase['objective']}</p></div>
      </div>
    </section>""")

    # 3+ ─ Phases
    for ph in clase.get("phases", []):
        pt = ph.get("type", "other")
        cfg = PHASE_CFG.get(pt, {"ico": "📌", "en": ph.get("title", ""), "es": "", "cls": ""})
        pcls = cfg["cls"]

        if pt == "desarrollo" and ph.get("activities"):
            preamble_html = ""
            if ph.get("preamble"):
                preamble_html = f'<div class="preamble">{ph["preamble"]}</div>'
            slides.append(f"""
    <section class="slide slide-phdr {pcls}">
      <div class="slide-content">
        <div class="ico">{cfg['ico']}</div>
        <h2>{cfg['en']}</h2>
        <p class="sub">{ph.get('title','')}</p>
        <p class="cnt">{len(ph['activities'])} actividades</p>
        {preamble_html}
      </div>
    </section>""")
            for i, act_html in enumerate(ph["activities"], 1):
                slides.append(f"""
    <section class="slide slide-act {pcls}">
      <div class="slide-content">
        <div class="hdr-bar">
          <span class="act-n">Actividad {i}</span>
          <h2>{cfg['en']}</h2>
          <span class="badge-ph">{cfg['es']}</span>
        </div>
        <div class="body-text">{act_html}</div>
      </div>
    </section>""")
        else:
            # Single slide (inicio / cierre / desarrollo without <ol>)
            content = ph.get("html", "")
            slides.append(f"""
    <section class="slide slide-ph {pcls}">
      <div class="slide-content">
        <div class="hdr-bar">
          <span style="font-size:1.6em">{cfg['ico']}</span>
          <h2>{cfg['en']}</h2>
          <span class="badge-ph">{ph.get('title','')}</span>
        </div>
        <div class="body-text">{content}</div>
      </div>
    </section>""")

    # Resources
    if clase.get("resources"):
        slides.append(f"""
    <section class="slide slide-res">
      <div class="slide-content">
        <div class="ico">📦</div>
        <h2>Recursos / Resources</h2>
        <div class="res-box"><p>{clase['resources']}</p></div>
      </div>
    </section>""")

    # Evaluation
    if clase.get("evaluation"):
        slides.append(f"""
    <section class="slide slide-eval">
      <div class="slide-content">
        <div class="ico">📋</div>
        <h2>Evaluación</h2>
        <div class="eval-box">{clase['evaluation']}</div>
      </div>
    </section>""")

    # End
    slides.append(f"""
    <section class="slide slide-end">
      <div class="slide-content">
        <div class="end-ico">✅</div>
        <h2>¡Fin de la clase!</h2>
        <p class="sub">{cn} — {unit_title}</p>
        <p class="msg">Great work today! See you next class! 🎓</p>
      </div>
    </section>""")

    total = len(slides)
    slides_block = "\n".join(slides)

    # Assemble CSS with theme
    css = CSS_TEMPLATE
    css = css.replace("%%PRIMARY%%", theme["primary"])
    css = css.replace("%%PRIMARY_DARK%%", theme["primary_dark"])
    css = css.replace("%%PRIMARY_LIGHT%%", theme["primary_light"])
    css = css.replace("%%GRADIENT%%", theme["gradient"])
    css = css.replace("%%BG_LIGHT%%", theme["bg_light"])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cn} — {unit_title} — {level}</title>
    <style>{css}</style>
</head>
<body>
    <div class="presentation">
{slides_block}
    </div>

    <div class="nav">
        <button onclick="prev()">◀</button>
        <button onclick="next()">▶</button>
    </div>
    <div class="prog-wrap"><div class="prog-bar" id="bar"></div></div>
    <div class="counter" id="ctr">1 / {total}</div>

    <script>{JS_TEMPLATE}</script>
</body>
</html>"""
    return html


# ─────────────────────────── MAIN ───────────────────────────
def safe_name(s):
    return (s.replace(" ", "_").replace("á", "a").replace("é", "e")
             .replace("í", "i").replace("ó", "o").replace("ú", "u")
             .replace("ñ", "n"))


def main():
    levels = ["1ro Medio", "3ro Medio", "4to Medio"]
    total = 0

    for level in levels:
        u1_dir = os.path.join(BASE_DIR, level, "Unidad 1")
        if not os.path.isdir(u1_dir):
            print(f"  ⚠ No encontrado: {u1_dir}")
            continue

        theme = THEMES.get(level, THEMES["1ro Medio"])
        files = sorted(f for f in os.listdir(u1_dir) if f.startswith("planificacion") and f.endswith(".html"))
        if not files:
            print(f"  ⚠ Sin planificaciones en {u1_dir}")
            continue

        out_dir = os.path.join(u1_dir, "Presentaciones")
        os.makedirs(out_dir, exist_ok=True)

        for fname in files:
            fpath = os.path.join(u1_dir, fname)
            spec = get_specialty(fname)
            print(f"\n  📄 {level} / {fname}")

            data = parse_planificacion(fpath)
            ut = data["unit_title"]
            print(f"     Unidad: {ut}  ·  Clases: {len(data['classes'])}")

            for clase in data["classes"]:
                cn = clase["number"].lower().replace(" ", "_")
                if spec:
                    out_name = f"{cn}_{safe_name(spec)}.html"
                else:
                    out_name = f"{cn}.html"

                html = build_slides(clase, level, spec, ut, theme)
                out_path = os.path.join(out_dir, out_name)
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(html)

                total += 1
                print(f"     ✅ {out_name}")

    print(f"\n{'='*55}")
    print(f"  ✅ COMPLETADO: {total} presentaciones generadas")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
