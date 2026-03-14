#!/usr/bin/env python3
"""
Generador de Presentaciones V2 — Material Real de Enseñanza.
Genera presentaciones HTML interactivas con contenido real para proyectar en clase.
"""
import os, sys, html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

THEMES = {
    "1ro Medio": {"primary":"#1565c0","primary_dark":"#0d47a1","primary_light":"#42a5f5",
                  "gradient":"linear-gradient(135deg, #0d47a1, #1976d2)","bg_light":"#e3f2fd"},
    "3ro Medio": {"primary":"#c62828","primary_dark":"#b71c1c","primary_light":"#ef5350",
                  "gradient":"linear-gradient(135deg, #b71c1c, #d32f2f)","bg_light":"#ffebee"},
    "4to Medio": {"primary":"#6a1b9a","primary_dark":"#4a148c","primary_light":"#ab47bc",
                  "gradient":"linear-gradient(135deg, #4a148c, #7b1fa2)","bg_light":"#f3e5f5"},
}

SPEC_MAP = {
    "automotriz": "Mecánica Automotriz", "electricidad": "Electricidad",
    "electronica": "Electrónica", "grafica": "Gráfica", "industrial": "Mecánica Industrial",
}

# ═══════════════════ CSS ═══════════════════
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700&display=swap');
:root{--primary:%%P%%;--primary-dark:%%PD%%;--primary-light:%%PL%%;--gradient:%%GR%%;--bg-light:%%BL%%;
--inicio:#2e7d32;--inicio-light:#e8f5e9;--desarrollo:#1565c0;--desarrollo-light:#e3f2fd;
--cierre:#6a1b9a;--cierre-light:#f3e5f5;--text:#1a1a2e;--text-light:#555;--white:#fff;--shadow:0 8px 32px rgba(0,0,0,.10)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;font-family:'Inter','Segoe UI',sans-serif;background:#0a0a1a}
.presentation{width:100%;height:100%;position:relative}
.slide{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;
transform:translateX(50px);transition:opacity .55s cubic-bezier(.4,0,.2,1),transform .55s cubic-bezier(.4,0,.2,1);
pointer-events:none;padding:40px 50px;background:var(--white);overflow-y:auto}
.slide.active{opacity:1;transform:translateX(0);pointer-events:auto;z-index:10}
.slide.exit-l{opacity:0;transform:translateX(-50px)}
.slide-content{max-width:960px;width:100%;text-align:center}

/* Title slide */
.slide-title{background:var(--gradient);color:var(--white)}
.slide-title .deco{display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:28px}
.slide-title .deco-line{width:70px;height:2px;background:rgba(255,255,255,.35)}
.slide-title .deco-dot{width:10px;height:10px;border:2px solid rgba(255,255,255,.5);border-radius:50%}
.slide-title .cls-num{font-family:'Playfair Display',serif;font-size:3.8em;font-weight:700;margin-bottom:12px;text-shadow:0 4px 18px rgba(0,0,0,.18);animation:fadeUp .8s ease-out}
.slide-title .unit-t{font-size:1.5em;font-weight:300;margin-bottom:18px;opacity:.95;animation:fadeUp .8s ease-out .12s both}
.slide-title .lvl{font-size:1.05em;font-weight:500;opacity:.85;animation:fadeUp .8s ease-out .22s both}
.slide-title .spec{font-size:.95em;opacity:.78;margin-top:2px;animation:fadeUp .8s ease-out .28s both}
.hint{margin-top:36px;font-size:.82em;opacity:.45;animation:pulse 2.2s ease-in-out infinite}

/* Objective */
.slide-obj{background:linear-gradient(135deg,#fff8e1,#fff3e0)}
.slide-obj .ico{font-size:3.2em;margin-bottom:16px;animation:popIn .55s ease-out}
.slide-obj h2{font-size:1.9em;color:#ef6c00;margin-bottom:24px}
.obj-box{background:var(--white);padding:28px 36px;border-radius:14px;box-shadow:var(--shadow);border-left:5px solid #ef6c00;text-align:left;font-size:1.2em;line-height:1.65;color:var(--text);animation:fadeUp .55s ease-out .15s both}

/* Vocab card */
.slide-vocab{background:linear-gradient(135deg,#e8eaf6,#e3f2fd)}
.vocab-card{background:var(--white);border-radius:16px;padding:32px 40px;box-shadow:var(--shadow);max-width:700px;margin:0 auto;animation:fadeUp .5s ease-out}
.vocab-card .word{font-size:2.8em;font-weight:800;color:var(--primary-dark);margin-bottom:4px}
.vocab-card .phonetic{font-size:1.1em;color:var(--text-light);font-style:italic;margin-bottom:16px}
.vocab-card .emoji{font-size:3.5em;margin-bottom:16px}
.vocab-card .def{font-size:1.15em;color:var(--text);margin-bottom:12px;line-height:1.6}
.vocab-card .example{font-size:1em;color:#555;font-style:italic;background:#f5f5f5;padding:10px 16px;border-radius:8px;border-left:3px solid var(--primary)}
.vocab-counter{position:absolute;top:20px;right:30px;font-size:.85em;color:var(--text-light);background:rgba(255,255,255,.8);padding:4px 14px;border-radius:12px}

/* Reading text */
.slide-reading{background:linear-gradient(135deg,#fafafa,#f5f5f5)}
.reading-box{background:var(--white);border-radius:14px;padding:28px 36px;box-shadow:var(--shadow);text-align:left;max-width:850px;margin:0 auto;animation:fadeUp .5s ease-out}
.reading-box h3{font-size:1.5em;color:var(--primary-dark);margin-bottom:16px;text-align:center}
.reading-box p{font-size:1.08em;line-height:1.8;color:var(--text);margin-bottom:12px}
.reading-box .keyword{background:#fff9c4;padding:1px 5px;border-radius:3px;font-weight:600;color:#e65100}

/* Grammar */
.slide-grammar{background:linear-gradient(135deg,#e8f5e9,#f1f8e9)}
.grammar-box{background:var(--white);border-radius:14px;padding:28px 36px;box-shadow:var(--shadow);text-align:left;max-width:800px;margin:0 auto;animation:fadeUp .5s ease-out}
.grammar-box h3{font-size:1.5em;color:#2e7d32;margin-bottom:16px;text-align:center}
.grammar-rule{background:#e8f5e9;padding:16px 22px;border-radius:10px;margin-bottom:16px;font-size:1.2em;text-align:center;font-weight:600;color:#1b5e20;border:2px dashed #66bb6a}
.grammar-box .example-row{display:flex;align-items:center;gap:12px;margin-bottom:10px;padding:8px 14px;background:#fafafa;border-radius:8px}
.grammar-box .ex-label{font-size:.8em;font-weight:700;color:var(--white);background:#43a047;padding:2px 10px;border-radius:6px;white-space:nowrap}
.grammar-box .ex-label.neg{background:#e53935}
.grammar-box .ex-label.q{background:#1565c0}
.grammar-box .ex-text{font-size:1.05em;color:var(--text)}
.grammar-box .ex-text b{color:#2e7d32}

/* Exercise */
.slide-exercise{background:linear-gradient(135deg,#fff3e0,#fbe9e7)}
.exercise-box{background:var(--white);border-radius:14px;padding:28px 36px;box-shadow:var(--shadow);text-align:left;max-width:800px;margin:0 auto;animation:fadeUp .5s ease-out}
.exercise-box h3{font-size:1.4em;color:#e65100;margin-bottom:20px;text-align:center}
.exercise-box .q-item{margin-bottom:14px;padding:10px 16px;background:#fafafa;border-radius:8px;font-size:1.05em;line-height:1.6}
.exercise-box .q-item .blank{display:inline-block;min-width:100px;border-bottom:2px dashed #e65100;text-align:center;color:#e65100;font-weight:600;cursor:pointer}
.exercise-box .q-item .blank.revealed{border-bottom-color:#2e7d32;color:#2e7d32}

/* Discussion */
.slide-discuss{background:linear-gradient(135deg,#ede7f6,#e8eaf6)}
.discuss-box{background:var(--white);border-radius:14px;padding:28px 36px;box-shadow:var(--shadow);text-align:left;max-width:800px;margin:0 auto}
.discuss-box h3{font-size:1.4em;color:#5e35b1;margin-bottom:20px;text-align:center}
.discuss-q{margin-bottom:14px;padding:12px 18px;background:#ede7f6;border-radius:10px;font-size:1.12em;font-weight:500;color:#4527a0;border-left:4px solid #7e57c2}
.sentence-frame{margin-top:16px;padding:14px 18px;background:#f3e5f5;border-radius:10px;font-size:1em;color:#6a1b9a;font-style:italic}

/* Table / Diagram */
.slide-table{background:linear-gradient(135deg,#fafafa,#f0f0f0)}
.table-box{background:var(--white);border-radius:14px;padding:22px 30px;box-shadow:var(--shadow);max-width:850px;margin:0 auto;overflow-x:auto;animation:fadeUp .5s ease-out}
.table-box h3{font-size:1.4em;color:var(--primary-dark);margin-bottom:16px;text-align:center}
.table-box table{width:100%;border-collapse:collapse;font-size:.95em}
.table-box th{background:var(--primary);color:white;padding:10px 14px;text-align:left;font-weight:600}
.table-box td{padding:9px 14px;border-bottom:1px solid #e0e0e0}
.table-box tr:nth-child(even) td{background:#f8f9fa}

/* Rubric */
.slide-rubric{background:linear-gradient(135deg,#fce4ec,#fff3e0)}
.rubric-box{background:var(--white);border-radius:14px;padding:22px 30px;box-shadow:var(--shadow);max-width:900px;margin:0 auto;overflow-x:auto}
.rubric-box h3{font-size:1.4em;color:#c62828;margin-bottom:16px;text-align:center}
.rubric-box table{width:100%;border-collapse:collapse;font-size:.82em}
.rubric-box th{background:#c62828;color:white;padding:8px 10px;text-align:center;font-weight:600}
.rubric-box td{padding:7px 10px;border:1px solid #e0e0e0;text-align:center;vertical-align:top}
.rubric-box td:first-child{text-align:left;font-weight:600;background:#fce4ec}

/* End slide */
.slide-end{background:var(--gradient);color:var(--white)}
.slide-end .end-ico{font-size:3.8em;margin-bottom:16px;animation:popIn .55s ease-out}
.slide-end h2{font-size:2.4em;font-weight:700;margin-bottom:12px;color:var(--white)}
.slide-end .sub{font-size:1.05em;opacity:.78;margin-bottom:10px}
.slide-end .msg{font-size:1.25em;opacity:.9}

/* Section header */
.slide-section{background:var(--gradient);color:var(--white)}
.slide-section .sec-ico{font-size:4em;margin-bottom:16px;animation:popIn .55s ease-out}
.slide-section h2{font-size:2.2em;font-weight:700;margin-bottom:12px}
.slide-section .sec-sub{font-size:1.15em;opacity:.8}

/* Nav */
.nav{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);display:flex;gap:12px;z-index:100}
.nav button{width:46px;height:46px;border-radius:50%;border:none;background:rgba(0,0,0,.12);color:var(--text);font-size:1.2em;cursor:pointer;transition:all .25s;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(8px)}
.nav button:hover{background:rgba(0,0,0,.25);transform:scale(1.08)}
.prog-wrap{position:fixed;top:0;left:0;width:100%;height:4px;background:rgba(0,0,0,.08);z-index:100}
.prog-bar{height:100%;background:var(--primary);transition:width .4s ease;border-radius:0 2px 2px 0}
.counter{position:fixed;bottom:28px;right:28px;font-size:.82em;color:var(--text-light);z-index:100;background:rgba(255,255,255,.75);padding:3px 10px;border-radius:10px;backdrop-filter:blur(8px)}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@keyframes popIn{0%{opacity:0;transform:scale(.3)}55%{opacity:1;transform:scale(1.05)}75%{transform:scale(.96)}100%{transform:scale(1)}}
@keyframes pulse{0%,100%{opacity:.45}50%{opacity:.75}}
@media(max-width:900px){.slide{padding:24px 20px}.slide-title .cls-num{font-size:2.6em}.vocab-card .word{font-size:2em}.nav button{width:38px;height:38px;font-size:1em}}
@media print{.slide{position:relative!important;opacity:1!important;transform:none!important;page-break-after:always;height:auto;min-height:100vh}.nav,.prog-wrap,.counter{display:none}}
"""

JS = r"""
let cur=0;const slides=document.querySelectorAll('.slide');const N=slides.length;
const bar=document.getElementById('bar');const ctr=document.getElementById('ctr');
function go(idx,dir){if(idx<0||idx>=N)return;const old=slides[cur];old.classList.remove('active');
if(dir===1)old.classList.add('exit-l');setTimeout(()=>old.classList.remove('exit-l'),600);
cur=idx;slides[cur].classList.add('active');bar.style.width=((cur+1)/N*100)+'%';ctr.textContent=(cur+1)+' / '+N}
function next(){go(cur+1,1)}function prev(){go(cur-1,-1)}
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' '||e.key==='Enter'){e.preventDefault();next()}
else if(e.key==='ArrowLeft'||e.key==='Backspace'){e.preventDefault();prev()}
else if(e.key==='Home'){e.preventDefault();go(0,-1)}else if(e.key==='End'){e.preventDefault();go(N-1,1)}});
let tx=0;document.addEventListener('touchstart',e=>{tx=e.changedTouches[0].screenX});
document.addEventListener('touchend',e=>{const d=tx-e.changedTouches[0].screenX;if(Math.abs(d)>50){d>0?next():prev()}});
document.querySelector('.presentation').addEventListener('click',e=>{if(!e.target.closest('.nav')&&!e.target.closest('.blank'))next()});
slides[0].classList.add('active');bar.style.width=(1/N*100)+'%';
document.querySelectorAll('.blank').forEach(b=>{b.addEventListener('click',e=>{e.stopPropagation();b.textContent=b.dataset.a;b.classList.add('revealed')})});
"""

# ═══════════════════ SLIDE BUILDERS ═══════════════════
def s_title(cn, unit_title, level, specialty=""):
    sp = f'<p class="spec">{specialty}</p>' if specialty else ""
    return f'''<section class="slide slide-title"><div class="slide-content">
<div class="deco"><div class="deco-line"></div><div class="deco-dot"></div><div class="deco-line"></div></div>
<h1 class="cls-num">Clase {cn}</h1><h2 class="unit-t">{unit_title}</h2>
<p class="lvl">{level}</p>{sp}<p class="hint">▶ Press any key or click to start</p>
</div></section>'''

def s_obj(text):
    return f'''<section class="slide slide-obj"><div class="slide-content">
<div class="ico">🎯</div><h2>Objective / Objetivo</h2>
<div class="obj-box"><p>{text}</p></div></div></section>'''

def s_section(icon, title, subtitle=""):
    sub = f'<p class="sec-sub">{subtitle}</p>' if subtitle else ""
    return f'''<section class="slide slide-section"><div class="slide-content">
<div class="sec-ico">{icon}</div><h2>{title}</h2>{sub}</div></section>'''

def s_vocab(word, phonetic, emoji, definition, example, idx=0, total=0):
    ct = f'<div class="vocab-counter">{idx}/{total}</div>' if idx else ""
    return f'''<section class="slide slide-vocab"><div class="slide-content">{ct}
<div class="vocab-card"><div class="emoji">{emoji}</div>
<div class="word">{word}</div><div class="phonetic">{phonetic}</div>
<div class="def">{definition}</div>
<div class="example">"{example}"</div></div></div></section>'''

def s_reading(title, paragraphs):
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    return f'''<section class="slide slide-reading"><div class="slide-content">
<div class="reading-box"><h3>📖 {title}</h3>{ps}</div></div></section>'''

def s_grammar(title, rule, examples):
    exs = ""
    for lbl, cls, txt in examples:
        exs += f'<div class="example-row"><span class="ex-label {cls}">{lbl}</span><span class="ex-text">{txt}</span></div>'
    return f'''<section class="slide slide-grammar"><div class="slide-content">
<div class="grammar-box"><h3>📐 {title}</h3><div class="grammar-rule">{rule}</div>{exs}</div></div></section>'''

def s_exercise(title, items):
    qs = ""
    for q, a in items:
        qs += f'<div class="q-item">{q.replace("___", f"""<span class="blank" data-a="{a}">click</span>""")}</div>'
    return f'''<section class="slide slide-exercise"><div class="slide-content">
<div class="exercise-box"><h3>✏️ {title}</h3>{qs}<p style="margin-top:16px;font-size:.85em;color:#999">Click each blank to reveal the answer</p></div></div></section>'''

def s_discuss(title, questions, frames=""):
    qs = "".join(f'<div class="discuss-q">💬 {q}</div>' for q in questions)
    fr = f'<div class="sentence-frame">💡 Sentence frames: {frames}</div>' if frames else ""
    return f'''<section class="slide slide-discuss"><div class="slide-content">
<div class="discuss-box"><h3>{title}</h3>{qs}{fr}</div></div></section>'''

def s_table(title, headers, rows):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for row in rows:
        trs += "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
    return f'''<section class="slide slide-table"><div class="slide-content">
<div class="table-box"><h3>{title}</h3><table><tr>{ths}</tr>{trs}</table></div></div></section>'''

def s_rubric(title, criteria, levels):
    ths = "<th>Criterion</th>" + "".join(f"<th>{l}</th>" for l in levels)
    trs = ""
    for row in criteria:
        trs += "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
    return f'''<section class="slide slide-rubric"><div class="slide-content">
<div class="rubric-box"><h3>📋 {title}</h3><table><tr>{ths}</tr>{trs}</table></div></div></section>'''

def s_end(cn, unit_title, msg="Great work today! See you next class! 🎓"):
    return f'''<section class="slide slide-end"><div class="slide-content">
<div class="end-ico">✅</div><h2>Class {cn} Complete!</h2>
<p class="sub">{unit_title}</p><p class="msg">{msg}</p></div></section>'''

def assemble(slides, theme, title):
    css = CSS.replace("%%P%%",theme["primary"]).replace("%%PD%%",theme["primary_dark"]).replace("%%PL%%",theme["primary_light"]).replace("%%GR%%",theme["gradient"]).replace("%%BL%%",theme["bg_light"])
    body = "\n".join(slides)
    N = len(slides)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title><style>{css}</style></head><body>
<div class="presentation">{body}</div>
<div class="nav"><button onclick="prev()">◀</button><button onclick="next()">▶</button></div>
<div class="prog-wrap"><div class="prog-bar" id="bar"></div></div>
<div class="counter" id="ctr">1 / {N}</div>
<script>{JS}</script></body></html>'''

def safe(s):
    return s.replace(" ","_").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n")

# ═══════════════════ 1RO MEDIO — 18 CLASES ═══════════════════
UNIT1_1RO = "The World of Technical Work"

def c1_1ro(th):
    return [s_title(1,UNIT1_1RO,"1ro Medio"),
    s_obj("Identify your English level through a diagnostic evaluation with technical-professional context."),
    s_section("📝","Diagnostic Evaluation","Let's find out what you already know!"),
    s_discuss("Warm-Up Questions",["What's your name? How old are you?","What specialty are you interested in?","What English words related to technical work do you already know?"],
    '"My name is... I am interested in... I know the word..."'),
    s_section("📖","Part 1: Reading Comprehension","20 minutes"),
    s_reading("Carlos at the Workshop",["Carlos works at a small automotive workshop in Santiago. Every day, he <span class='keyword'>checks engines</span>, <span class='keyword'>changes oil</span>, and <span class='keyword'>repairs brakes</span>. He uses many tools: a <span class='keyword'>wrench</span>, a <span class='keyword'>screwdriver</span>, and a <span class='keyword'>multimeter</span>.",
    "This morning, a customer brought a car with a strange noise. Carlos listened carefully and checked the <span class='keyword'>engine</span>. He found a loose <span class='keyword'>belt</span>. He replaced it in 30 minutes.",
    "'I love my job,' says Carlos. 'Every day is different. I learn something new.'"]),
    s_exercise("Comprehension Questions",[("Where does Carlos work? ___","At a workshop in Santiago"),("What does he do every day? ___","Checks engines, changes oil, repairs brakes"),("What was wrong with the customer's car? ___","A loose belt"),("How long did the repair take? ___","30 minutes")]),
    s_section("🗣️","Part 2: Oral Assessment","Tell your partner about yourself!"),
    s_discuss("Oral Activity — In Pairs",["Tell your partner: your name, your age, one hobby, and which specialty you like."],
    '"My name is... I am ___ years old. I like... My specialty is..."'),
    s_end(1,UNIT1_1RO,"Welcome to English for your career! 🎓")]

def c2_1ro(th):
    tools = [("Hammer","/ˈhæmər/","🔨","A tool for hitting nails or breaking things","Use a hammer to drive the nail into the wood."),
    ("Screwdriver","/ˈskruːdraɪvər/","🪛","A tool for turning screws","I need a screwdriver to open this panel."),
    ("Wrench","/rɛntʃ/","🔧","A tool for gripping and turning nuts and bolts","Use a wrench to tighten the bolt."),
    ("Pliers","/ˈplaɪərz/","🔧","A tool for gripping, bending, or cutting wire","Use pliers to cut the wire."),
    ("Drill","/drɪl/","🔩","A power tool for making holes","Drill a hole in the wall for the screw."),
    ("Multimeter","/ˈmʌltɪmiːtər/","📟","A device that measures voltage, current, and resistance","Check the voltage with a multimeter."),
    ("Soldering Iron","/ˈsɒldərɪŋ aɪərn/","🔥","A tool for melting solder to join metal parts","Use the soldering iron to connect the wires."),
    ("Measuring Tape","/ˈmɛʒərɪŋ teɪp/","📏","A flexible ruler for measuring length","Measure the pipe with the measuring tape."),
    ("Safety Goggles","/ˈseɪfti ˈɡɒɡəlz/","🥽","Eye protection for dangerous work","Always wear safety goggles when grinding."),
    ("Gloves","/ɡlʌvz/","🧤","Hand protection","Wear gloves when handling chemicals."),
    ("Helmet","/ˈhɛlmɪt/","⛑️","Head protection","A helmet protects your head from falling objects."),
    ("Wire Cutter","/waɪər ˈkʌtər/","✂️","A tool for cutting wires and cables","Cut the cable with a wire cutter."),
    ("Caliper","/ˈkælɪpər/","📐","A precision measuring tool","Use calipers to measure the diameter exactly."),
    ("Saw","/sɔː/","🪚","A tool for cutting wood or metal","Cut the board with a saw."),
    ("Clamp","/klæmp/","🗜️","A device for holding things tightly together","Use a clamp to hold the pieces while the glue dries.")]
    slides = [s_title(2,UNIT1_1RO,"1ro Medio"),
    s_obj("Recognize and categorize basic technical vocabulary of tools common to all five specialties."),
    s_section("🔧","Technical Tools Vocabulary","20 tools you need to know!")]
    for i,t in enumerate(tools,1):
        slides.append(s_vocab(t[0],t[1],t[2],t[3],t[4],i,len(tools)))
    slides.append(s_reading("The Right Tool for the Right Job",[
    "In every workshop, choosing the right tool is essential. Mr. López, a workshop supervisor with 20 years of experience, always tells his students: '<span class='keyword'>The right tool for the right job</span> saves time and prevents accidents.'",
    "'If you use <span class='keyword'>pliers</span> instead of a <span class='keyword'>wrench</span>, you can damage the bolt,' he explains. 'Each tool has a specific purpose. A <span class='keyword'>screwdriver</span> turns screws. A <span class='keyword'>multimeter</span> measures electricity. A <span class='keyword'>caliper</span> measures with precision.'",
    "Safety is also important. 'Always wear your <span class='keyword'>safety goggles</span> and <span class='keyword'>gloves</span>,' says Mr. López. 'A good technician takes care of their tools AND themselves.'"]))
    slides.append(s_exercise("Comprehension Check",[("Who is Mr. López? ___","A workshop supervisor"),("What happens if you use the wrong tool? ___","You can damage the bolt"),("What does a multimeter measure? ___","Electricity"),("What should you always wear? ___","Safety goggles and gloves")]))
    slides.append(s_table("Tool Classification",["Tool","Automotive","Industrial","Electrical","Electronics","Graphic"],
    [["Hammer","✓","✓","","",""],["Screwdriver","✓","✓","✓","✓",""],["Wrench","✓","✓","","",""],
    ["Multimeter","✓","","✓","✓",""],["Soldering Iron","","","","✓",""],["Caliper","✓","✓","","✓","✓"],
    ["Measuring Tape","✓","✓","✓","","✓"],["Safety Goggles","✓","✓","✓","✓","✓"]]))
    slides.append(s_discuss("Closing Discussion",["Which 3 tools will YOU use in your specialty?","Can you describe a tool without saying its name?"],
    '"I will use a... because... / This tool is used for..."'))
    slides.append(s_end(2,UNIT1_1RO))
    return slides

def c3_1ro(th):
    voc = [("Engine","/ˈɛndʒɪn/","⚙️","The machine that powers a car","The engine needs oil to work properly."),
    ("Brake","/breɪk/","🛑","A device for stopping a vehicle","Press the brake to stop the car."),
    ("Transmission","/trænzˈmɪʃən/","⚙️","The system that sends power from the engine to the wheels","The transmission has 5 gears."),
    ("Exhaust Pipe","/ɪɡˈzɔːst paɪp/","💨","The pipe that carries waste gases away","Smoke comes out of the exhaust pipe."),
    ("Spark Plug","/spɑːrk plʌɡ/","⚡","A device that creates a spark to ignite fuel","Change the spark plugs every 30,000 km."),
    ("Oil Filter","/ɔɪl ˈfɪltər/","🛢️","A filter that cleans the engine oil","Replace the oil filter during every oil change."),
    ("Tire","/taɪər/","🛞","The rubber part of a wheel","Check the tire pressure every month."),
    ("Suspension","/səˈspɛnʃən/","🔩","The system that absorbs road bumps","The suspension makes the ride smooth."),
    ("Hood","/hʊd/","🚗","The cover over the engine","Open the hood to check the engine."),
    ("Dashboard","/ˈdæʃbɔːrd/","📊","The panel in front of the driver","Warning lights appear on the dashboard."),
    ("Steering Wheel","/ˈstɪrɪŋ wiːl/","🎡","The wheel the driver turns to control direction","Hold the steering wheel with both hands."),
    ("Radiator","/ˈreɪdieɪtər/","🌡️","A device that cools the engine","The radiator uses coolant to prevent overheating."),
    ("Battery","/ˈbætəri/","🔋","Provides electrical power to start the car","The battery is dead — we need to charge it."),
    ("Alternator","/ˈɔːltərneɪtər/","⚡","Generates electricity while the engine runs","The alternator charges the battery.")]
    slides = [s_title(3,UNIT1_1RO,"1ro Medio"),
    s_obj("Understand explicit information in a descriptive text about an automotive workshop, identifying vocabulary specific to Mecánica Automotriz."),
    s_section("🚗","Automotive Vocabulary","14 key words for the automotive workshop")]
    for i,v in enumerate(voc,1):
        slides.append(s_vocab(v[0],v[1],v[2],v[3],v[4],i,len(voc)))
    slides.append(s_reading("A Day at González Automotive Workshop",[
    "It is 8:00 AM at González Automotive Workshop in Concepción. <span class='keyword'>Mechanic</span> Carlos arrives and puts on his work clothes. Today he has three cars to fix.",
    "The first car has a problem: the <span class='keyword'>engine</span> makes strange noises and loses power. Carlos opens the <span class='keyword'>hood</span> and checks the <span class='keyword'>spark plugs</span>. They are old and dirty. He replaces them with new ones.",
    "The second car needs an oil change. Carlos lifts the car, removes the old <span class='keyword'>oil filter</span>, and installs a new one. He adds fresh oil and checks the <span class='keyword'>dashboard</span> — the oil light turns off.",
    "The third car has a flat <span class='keyword'>tire</span>. Carlos uses a <span class='keyword'>jack</span> to lift the car, removes the flat tire, and puts on the spare. He also checks the <span class='keyword'>tire pressure</span> on the other three tires.",
    "'Another good day at work,' Carlos says. 'Tomorrow, I need to check a <span class='keyword'>transmission</span> problem. That will be more complex.'"]))
    slides.append(s_exercise("Comprehension Questions",[
    ("What is the first car's problem? ___","The engine makes strange noises"),
    ("What does Carlos replace? ___","The spark plugs"),
    ("What does the dashboard show after the oil change? ___","The oil light turns off"),
    ("What tools does Carlos use for the flat tire? ___","A jack")]))
    slides.append(s_discuss("Closing Discussion",["If you worked at this workshop, what would be your favorite task? Why?"],
    '"My favorite task would be... because..."'))
    slides.append(s_end(3,UNIT1_1RO))
    return slides

def c4_1ro(th):
    voc = [("Lathe","/leɪð/","⚙️","A machine for shaping metal by rotating it","The lathe cuts metal into round shapes."),
    ("Milling Machine","/ˈmɪlɪŋ məˈʃiːn/","🏭","A machine that cuts and shapes metal","Use the milling machine to create flat surfaces."),
    ("Welding Torch","/ˈwɛldɪŋ tɔːrtʃ/","🔥","A tool that joins metals using heat","The welding torch reaches 3,000°C."),
    ("Grinding Wheel","/ˈɡraɪndɪŋ wiːl/","💫","A spinning wheel for smoothing metal","Smooth the edge with a grinding wheel."),
    ("Bench Vise","/bɛntʃ vaɪs/","🗜️","A clamping device on a workbench","Hold the piece in the bench vise."),
    ("Steel","/stiːl/","🔩","A strong metal alloy","Steel is used in construction and machinery."),
    ("Bolt","/boʊlt/","🔩","A metal pin with a thread","Tighten the bolt with a wrench."),
    ("Nut","/nʌt/","🔩","A small metal piece that screws onto a bolt","The nut holds the bolt in place."),
    ("Drill Press","/drɪl prɛs/","🔩","A fixed drill for precise holes","Use the drill press for accurate holes."),
    ("Anvil","/ˈænvɪl/","⚒️","A heavy block for shaping metal","The blacksmith hammers metal on the anvil."),
    ("PPE","/piː piː iː/","🦺","Personal Protective Equipment","Always wear your PPE in the workshop.")]
    slides = [s_title(4,UNIT1_1RO,"1ro Medio"),
    s_obj("Understand specific information in a case study about safety in industrial mechanics and identify vocabulary for tools and heavy machinery."),
    s_section("🏭","Industrial Mechanics + Safety","15 key words for the industrial workshop")]
    for i,v in enumerate(voc,1):
        slides.append(s_vocab(v[0],v[1],v[2],v[3],v[4],i,len(voc)))
    slides.append(s_reading("Welding Safety: A Case Study",[
    "Pedro was a new worker at a metal factory in Rancagua. On his third day, his supervisor asked him to <span class='keyword'>weld</span> two steel plates together.",
    "Pedro was in a hurry. He did NOT wear his <span class='keyword'>welding helmet</span>. He did NOT wear <span class='keyword'>safety gloves</span>. He did NOT check the area for flammable materials.",
    "While welding, a <span class='keyword'>spark</span> flew into his eye. He also burned his hand on the hot metal. His supervisor rushed to help and took him to the first aid room.",
    "The doctor said Pedro was lucky — the burn was not serious. But he could have lost his eye.",
    "<b>The lesson:</b> <span class='keyword'>PPE</span> (Personal Protective Equipment) is not optional. Always wear your <span class='keyword'>helmet</span>, <span class='keyword'>goggles</span>, <span class='keyword'>gloves</span>, and <span class='keyword'>boots</span> before starting any work."]))
    slides.append(s_exercise("What went wrong?",[
    ("What PPE did Pedro NOT wear? ___","Welding helmet and safety gloves"),
    ("What happened to Pedro's eye? ___","A spark flew into it"),
    ("What should Pedro have done differently? ___","Wear all PPE before working")]))
    slides.append(s_discuss("Safety Discussion",["What safety rules were broken?","What 5 safety rules should every workshop have?"],
    '"Always wear... / Never touch... / In case of emergency..."'))
    slides.append(s_end(4,UNIT1_1RO))
    return slides

def c5_1ro(th):
    voc = [("Wire","/waɪər/","🔌","A thin metal thread that carries electricity","Connect the wire to the terminal."),
    ("Cable","/ˈkeɪbəl/","🔌","A thick wire or group of wires","The power cable connects to the outlet."),
    ("Circuit","/ˈsɜːrkɪt/","⚡","A complete path for electricity to flow","If the circuit is open, current cannot flow."),
    ("Switch","/swɪtʃ/","🔘","A device for turning electricity on or off","Flip the switch to turn on the light."),
    ("Outlet","/ˈaʊtlɛt/","🔌","A socket in a wall for plugging in devices","Plug the charger into the outlet."),
    ("Fuse","/fjuːz/","💥","A safety device that breaks when current is too high","The fuse blew because of a short circuit."),
    ("Voltage","/ˈvoʊltɪdʒ/","⚡","The electrical pressure that pushes current","Chilean homes use 220 voltage."),
    ("Current","/ˈkɜːrənt/","⚡","The flow of electricity through a conductor","Current is measured in amperes."),
    ("Resistance","/rɪˈzɪstəns/","⚡","Opposition to the flow of current","Resistance is measured in ohms."),
    ("Transformer","/trænsˈfɔːrmər/","🔄","A device that changes voltage levels","The transformer reduces voltage from 220V to 12V."),
    ("Circuit Breaker","/ˈsɜːrkɪt ˈbreɪkər/","🔴","An automatic switch that stops current if too high","The circuit breaker tripped during the storm."),
    ("Ground/Earth","/ɡraʊnd/","⏚","A safety connection to the earth","Every electrical system needs a ground connection."),
    ("Insulation","/ˌɪnsʊˈleɪʃən/","🛡️","Material that prevents electric shock","The insulation on this wire is damaged."),
    ("Conductor","/kənˈdʌktər/","🔌","Material that allows electricity to flow","Copper is an excellent conductor.")]
    slides = [s_title(5,UNIT1_1RO,"1ro Medio"),
    s_obj("Apply reading strategies to understand a text about basic electrical installations and identify technical Electricity vocabulary."),
    s_section("⚡","Electricity Vocabulary","15 key words for electrical work")]
    for i,v in enumerate(voc,1):
        slides.append(s_vocab(v[0],v[1],v[2],v[3],v[4],i,len(voc)))
    slides.append(s_reading("Understanding Basic Electrical Circuits",[
    "An electrical <span class='keyword'>circuit</span> is a path that allows <span class='keyword'>current</span> to flow from a power source, through a device, and back to the source.",
    "A simple circuit has four parts: a power source (like a <span class='keyword'>battery</span>), a <span class='keyword'>conductor</span> (like a copper <span class='keyword'>wire</span>), a load (like a light bulb), and a <span class='keyword'>switch</span>.",
    "When the switch is ON (closed), current flows through the circuit and the light turns on. When the switch is OFF (open), the circuit is broken and no current flows.",
    "Safety devices like <span class='keyword'>fuses</span> and <span class='keyword'>circuit breakers</span> protect the circuit. If too much <span class='keyword'>current</span> flows, the fuse breaks and stops the electricity. This prevents fires and damage.",
    "The <span class='keyword'>ground</span> wire is also important for safety. It provides a safe path for electricity if something goes wrong."]))
    slides.append(s_exercise("Label the Circuit",[
    ("The ___ provides electrical energy to the circuit.","battery"),
    ("___ carries electricity through the circuit.","Wire / Conductor"),
    ("A ___ turns the circuit on and off.","switch"),
    ("A ___ protects against too much current.","fuse")]))
    slides.append(s_end(5,UNIT1_1RO))
    return slides

def c6_1ro(th):
    voc=[("Resistor","/rɪˈzɪstər/","⚡","A component that limits current flow","The resistor controls how much current reaches the LED."),
    ("Capacitor","/kəˈpæsɪtər/","⚡","Stores and releases electrical energy","The capacitor stores energy like a small battery."),
    ("Diode","/ˈdaɪoʊd/","➡️","Allows current to flow in only one direction","A diode acts like a one-way valve for electricity."),
    ("LED","/ɛl iː diː/","💡","Light Emitting Diode — a small efficient light","LEDs use very little energy."),
    ("Transistor","/trænˈzɪstər/","🔀","Amplifies or switches electronic signals","Transistors are the building blocks of computers."),
    ("PCB","/piː siː biː/","📟","Printed Circuit Board — connects components","Every phone has a PCB inside."),
    ("Solder","/ˈsɒldər/","🔥","Metal used to join electronic components","Melt the solder to connect the wire to the board."),
    ("Breadboard","/ˈbrɛdbɔːrd/","📟","A board for building test circuits without soldering","Build your prototype on a breadboard first."),
    ("Sensor","/ˈsɛnsər/","📡","A device that detects changes in the environment","The temperature sensor reads 25°C."),
    ("Microcontroller","/ˈmaɪkroʊkənˌtroʊlər/","🤖","A small computer on a single chip","Arduino is a popular microcontroller.")]
    slides=[s_title(6,UNIT1_1RO,"1ro Medio"),
    s_obj("Understand an instructive text about building a simple electronic circuit, identifying components and sequence connectors."),
    s_section("📟","Electronics Vocabulary","Key components for electronic work")]
    for i,v in enumerate(voc,1):
        slides.append(s_vocab(v[0],v[1],v[2],v[3],v[4],i,len(voc)))
    slides.append(s_reading("How to Build a Simple LED Circuit",[
    "<b>Materials needed:</b> 1 <span class='keyword'>LED</span>, 1 <span class='keyword'>resistor</span> (220Ω), 1 9V <span class='keyword'>battery</span>, <span class='keyword'>wires</span>, 1 <span class='keyword'>breadboard</span>.",
    "<b>First</b>, place the <span class='keyword'>LED</span> on the <span class='keyword'>breadboard</span>. The longer leg is positive (+), the shorter leg is negative (−).",
    "<b>Then</b>, connect the <span class='keyword'>resistor</span> to the positive leg of the LED. The resistor protects the LED from too much current.",
    "<b>Next</b>, connect a wire from the other end of the resistor to the positive (+) terminal of the battery.",
    "<b>After that</b>, connect a wire from the negative leg of the LED to the negative (−) terminal of the battery.",
    "<b>Finally</b>, check all connections. If everything is correct, the LED should light up! 💡",
    "⚠️ <b>Warning:</b> If you connect the LED backwards, it will NOT work (but it won't break)."]))
    slides.append(s_section("🔤","Sequence Connectors","First → Then → Next → After that → Finally")),
    slides.append(s_exercise("Put in order — Use connectors",[
    ("___, place the LED on the breadboard.","First"),
    ("___, connect the resistor to the positive leg.","Then"),
    ("___, connect a wire to the battery (+).","Next"),
    ("___, connect the LED (−) to the battery (−).","After that"),
    ("___, check all connections.","Finally")]))
    slides.append(s_end(6,UNIT1_1RO))
    return slides

def c7_1ro(th):
    voc=[("Printing Press","/ˈprɪntɪŋ prɛs/","🖨️","A machine for printing text and images on paper","The printing press produces 10,000 pages per hour."),
    ("Ink","/ɪŋk/","🎨","Colored liquid used for printing","The printer is out of black ink."),
    ("Layout","/ˈleɪaʊt/","📐","The arrangement of text and images on a page","The designer creates the layout in InDesign."),
    ("Proof","/pruːf/","📄","A test print to check for errors","Always check the proof before printing."),
    ("Binding","/ˈbaɪndɪŋ/","📚","Joining pages together to make a book","The binding holds all the pages together."),
    ("Color Separation","/ˈkʌlər ˌsɛpəˈreɪʃən/","🌈","Dividing an image into CMYK colors for printing","Color separation is essential for full-color printing."),
    ("CMYK","/siː ɛm waɪ keɪ/","🎨","Cyan, Magenta, Yellow, Key (Black) — printing colors","CMYK is the standard for print, RGB for screens."),
    ("Resolution","/ˌrɛzəˈluːʃən/","🔍","The quality/detail of a printed image (measured in DPI)","Use 300 DPI resolution for professional printing."),
    ("Substrate","/ˈsʌbstreɪt/","📄","The material being printed on (paper, cardboard, plastic)","Choose the right substrate for each project."),
    ("Lamination","/ˌlæmɪˈneɪʃən/","✨","Adding a protective plastic layer over a print","Lamination protects the cover from damage.")]
    slides=[s_title(7,UNIT1_1RO,"1ro Medio"),
    s_obj("Understand a descriptive text about graphic arts processes and identify the production sequence of a printed product."),
    s_section("🖨️","Graphic Arts Vocabulary","Key words for the printing industry")]
    for i,v in enumerate(voc,1):
        slides.append(s_vocab(v[0],v[1],v[2],v[3],v[4],i,len(voc)))
    slides.append(s_reading("From Digital File to Printed Product",[
    "The printing process has many steps. It starts with a <span class='keyword'>digital file</span> — a design created on a computer using software like Adobe InDesign or Illustrator.",
    "<b>Step 1: Design.</b> The designer creates the <span class='keyword'>layout</span>, choosing fonts, images, and colors. The file must be in <span class='keyword'>CMYK</span> format (not RGB) for printing.",
    "<b>Step 2: Proofing.</b> Before printing thousands of copies, the printer makes a <span class='keyword'>proof</span> — a test print. The client checks for errors in text, colors, and images.",
    "<b>Step 3: Printing.</b> The <span class='keyword'>printing press</span> applies <span class='keyword'>ink</span> to the <span class='keyword'>substrate</span> (paper, cardboard, or plastic). Each color (C, M, Y, K) is applied separately.",
    "<b>Step 4: Finishing.</b> After printing, the product may be <span class='keyword'>cut</span>, <span class='keyword'>folded</span>, <span class='keyword'>laminated</span>, or <span class='keyword'>bound</span>. A book needs <span class='keyword'>binding</span>; a poster may need <span class='keyword'>lamination</span>."]))
    slides.append(s_table("The Printing Process Flowchart",["Step","Action","Key Term"],
    [["1","Create design on computer","Layout"],["2","Make test print","Proof"],["3","Print on material","Printing Press"],
    ["4","Cut, fold, bind","Finishing"],["5","Deliver to client","Final Product"]]))
    slides.append(s_end(7,UNIT1_1RO))
    return slides

def c8_1ro(th):
    slides=[s_title(8,UNIT1_1RO,"1ro Medio"),
    s_obj("Synthesize and apply technical vocabulary from all five specialties in integrated reading comprehension and oral production activities."),
    s_section("🎯","Integration Class","Bringing all 5 specialties together!"),
    s_section("🎰","Technical English Bingo","Listen to the description — find the word on your card!"),
    s_table("Bingo Clues",["#","Clue","Answer"],
    [["1","A tool that measures voltage, current, and resistance","Multimeter"],
    ["2","The machine that powers a car","Engine"],
    ["3","A device for cutting wire","Wire Cutter"],
    ["4","Material that prevents electric shock","Insulation"],
    ["5","The arrangement of text and images on a page","Layout"],
    ["6","A machine for shaping metal by rotating it","Lathe"],
    ["7","A small efficient light that uses very little energy","LED"],
    ["8","Joining pages together to make a book","Binding"]]),
    s_reading("Five Careers, Five Futures",[
    "<b>🚗 Andrés — Automotive Technician:</b> 'I check engines, repair brakes, and diagnose problems using a <span class='keyword'>diagnostic scanner</span>. I love solving mysteries — every car has a different problem!'",
    "<b>🏭 María — Industrial Welder:</b> 'I weld steel structures for buildings. I use a <span class='keyword'>welding torch</span> and always wear full <span class='keyword'>PPE</span>. My favorite project was a bridge in Biobío.'",
    "<b>⚡ Juan — Electrician:</b> 'I install <span class='keyword'>circuits</span> in new buildings. I test <span class='keyword'>voltage</span> and make sure everything is safe. A mistake can cause a fire!'",
    "<b>📟 Camila — Electronics Technician:</b> 'I program <span class='keyword'>microcontrollers</span> and design <span class='keyword'>PCBs</span>. Technology changes fast, so I'm always learning new things.'",
    "<b>🖨️ Diego — Graphic Arts Specialist:</b> 'I operate the <span class='keyword'>printing press</span> and control <span class='keyword'>color separation</span>. Seeing a beautiful print come off the press is the best feeling!'"]),
    s_table("Compare the Five Careers",["Specialty","What they do","Main tools","What they like"],
    [["Automotive","Check engines, repair brakes","Diagnostic scanner","Solving problems"],
    ["Industrial","Weld steel structures","Welding torch, PPE","Building things"],
    ["Electricity","Install circuits","Multimeter","Keeping people safe"],
    ["Electronics","Program microcontrollers","PCB, breadboard","Learning new tech"],
    ["Graphic Arts","Operate printing press","Color separation","Seeing final product"]]),
    s_discuss("Closing Discussion",["Which specialty has the most interesting vocabulary for you?","Which career would you choose? Why?"],
    '"I think... is the most interesting because... / I would choose... because..."')]
    slides.append(s_end(8,UNIT1_1RO))
    return slides

def c9_1ro(th):
    slides=[s_title(9,UNIT1_1RO,"1ro Medio"),
    s_obj("Understand the structure and use of Present Perfect Simple to describe achievements and experiences in technical-professional contexts."),
    s_section("📐","Present Perfect Simple","Talking about experiences and achievements"),
    s_grammar("Present Perfect — Structure","Subject + <b>have/has</b> + <b>past participle</b>",[
    ("✅","","She <b>has repaired</b> many engines."),("✅","","They <b>have built</b> 30 circuits."),
    ("✅","","He <b>has designed</b> a new logo."),("✅","","We <b>have installed</b> the wiring."),
    ("✅","","I <b>have welded</b> 100 structures.")]),
    s_grammar("When do we use it?","Experiences • Achievements • Unfinished actions",[
    ("EXP","","<b>Have</b> you ever <b>welded</b>? — Yes, I have."),
    ("ACH","","She <b>has installed</b> 200 solar panels."),
    ("DUR","","He <b>has worked</b> here for 10 years.")]),
    s_grammar("Negative & Question Forms","",
    [("−","neg","She <b>has not (hasn't) finished</b> the repair."),
    ("?","q","<b>Have</b> you <b>checked</b> the oil? — Yes, I have."),
    ("−","neg","They <b>haven't used</b> this machine before.")]),
    s_table("Irregular Past Participles",["Base Form","Past Simple","Past Participle"],
    [["build","built","built"],["do","did","done"],["make","made","made"],["cut","cut","cut"],
    ["see","saw","seen"],["write","wrote","written"],["break","broke","broken"],
    ["drive","drove","driven"],["choose","chose","chosen"],["put","put","put"]]),
    s_exercise("Complete with Present Perfect",[
    ("She ___ (repair) many engines.","has repaired"),("They ___ (build) 30 circuits.","have built"),
    ("I ___ (never / use) a lathe.","have never used"),
    ("___ you ever ___ (weld) steel? ","Have... welded"),
    ("He ___ (work) here for 10 years.","has worked")]),
    s_reading("Interview with Don Pedro",[
    "'My name is Pedro González. I <span class='keyword'>have worked</span> as a mechanic for 30 years. I <span class='keyword'>have repaired</span> more than 5,000 cars in my career.'",
    "'I <span class='keyword'>have seen</span> many changes in technology. When I started, we didn't have diagnostic computers. Now I <span class='keyword'>have learned</span> to use OBD scanners and digital tools.'",
    "'<span class='keyword'>Have</span> I ever <span class='keyword'>had</span> an accident? Yes, once. I <span class='keyword'>have broken</span> my arm when a jack failed. That's why I always tell my students: safety first!'"]),
    s_end(9,UNIT1_1RO)]
    return slides

def c10_1ro(th):
    return [s_title(10,UNIT1_1RO,"1ro Medio"),
    s_obj("Differentiate the use of 'since' and 'for' with Present Perfect to describe the duration of technical-professional activities."),
    s_section("📐","Since vs For","Talking about duration with Present Perfect"),
    s_grammar("SINCE = specific point in time","since 2015 / since Monday / since January",[
    ("SINCE","","He <b>has worked</b> at the factory <b>since 2015</b>."),
    ("SINCE","","This machine <b>has been</b> here <b>since 1990</b>."),
    ("SINCE","","I <b>have studied</b> English <b>since</b> I was 10.")]),
    s_grammar("FOR = duration of time","for 3 years / for 2 months / for a long time",[
    ("FOR","","He <b>has worked</b> at the factory <b>for 10 years</b>."),
    ("FOR","","They <b>have used</b> this software <b>for 5 years</b>."),
    ("FOR","","She <b>has been</b> an electrician <b>for a long time</b>.")]),
    s_exercise("Since or For?",[("He has worked here ___ 2015.","since"),("She has studied English ___ 8 years.","for"),
    ("They have used this machine ___ last Monday.","since"),("I have lived in Chile ___ my whole life.","for"),
    ("We have known each other ___ 2020.","since")]),
    s_reading("Five Professionals, Five Stories",[
    "<b>⚡ María — Electrician:</b> 'I <span class='keyword'>have worked</span> as an electrician <span class='keyword'>since 2010</span>. I <span class='keyword'>have installed</span> systems <span class='keyword'>for 15 years</span>.'",
    "<b>🚗 Carlos — Mechanic:</b> 'I <span class='keyword'>have repaired</span> cars <span class='keyword'>since</span> I was 18. I <span class='keyword'>have been</span> at this workshop <span class='keyword'>for 12 years</span>.'",
    "<b>🏭 Pedro — Welder:</b> 'I <span class='keyword'>have welded</span> steel <span class='keyword'>for 20 years</span>. I <span class='keyword'>have worked</span> in this factory <span class='keyword'>since 2005</span>.'",
    "<b>📟 Ana — Electronics Tech:</b> 'I <span class='keyword'>have programmed</span> microcontrollers <span class='keyword'>since 2018</span>. I <span class='keyword'>have designed</span> PCBs <span class='keyword'>for 7 years</span>.'",
    "<b>🖨️ Diego — Graphic Designer:</b> 'I <span class='keyword'>have operated</span> printing presses <span class='keyword'>for 10 years</span>. I <span class='keyword'>have worked</span> here <span class='keyword'>since 2016</span>.'"]),
    s_table("Complete the Table",["Name","Specialty","Since...","For..."],
    [["María","Electrician","2010","15 years"],["Carlos","Mechanic","age 18","12 years"],
    ["Pedro","Welder","2005","20 years"],["Ana","Electronics","2018","7 years"],["Diego","Graphic Arts","2016","10 years"]]),
    s_end(10,UNIT1_1RO)]

def c11_1ro(th):
    return [s_title(11,UNIT1_1RO,"1ro Medio"),
    s_obj("Understand and use 'used to + infinitive' to compare past and present technical practices."),
    s_section("📐","Used To","Talking about past habits that no longer exist"),
    s_grammar("Used to — Structure","Subject + <b>used to</b> + <b>infinitive</b>",[
    ("✅","","Mechanics <b>used to</b> fix cars without computers."),
    ("−","neg","They <b>didn't use to</b> have digital multimeters."),
    ("?","q","<b>Did</b> they <b>use to</b> weld by hand?")]),
    s_grammar("Used to = Past vs Now","Contrasting past habits with present reality",[
    ("PAST","neg","Mechanics <b>used to</b> use only hand tools."),
    ("NOW","q","Now they <b>use</b> diagnostic software."),
    ("PAST","neg","Printers <b>used to</b> use only black ink."),
    ("NOW","q","Now they <b>use</b> CMYK color printing.")]),
    s_reading("Then and Now: How Technology Changed the Workshop",[
    "<b>🚗 Automotive:</b> Mechanics <span class='keyword'>used to</span> diagnose problems by listening to the engine. Now they <span class='keyword'>use</span> OBD scanners and computers.",
    "<b>🏭 Industrial:</b> Workers <span class='keyword'>used to</span> weld with basic torches. Now they <span class='keyword'>use</span> MIG and TIG welding machines with digital controls.",
    "<b>⚡ Electricity:</b> Electricians <span class='keyword'>used to</span> work with simple circuits. Now they <span class='keyword'>install</span> smart home systems and solar panels.",
    "<b>📟 Electronics:</b> Technicians <span class='keyword'>used to</span> solder everything by hand. Now they <span class='keyword'>use</span> automated assembly and microcontrollers.",
    "<b>🖨️ Graphic Arts:</b> Printers <span class='keyword'>used to</span> set type by hand (letter by letter). Now everything is <span class='keyword'>digital</span> — designed on computers."]),
    s_exercise("Complete with 'used to'",[("Mechanics ___ fix cars without computers.","used to"),
    ("They ___ have digital tools. (negative)","didn't use to"),
    ("Printers ___ set type by hand.","used to"),("___ they ___ weld by hand? (question)","Did... use to")]),
    s_discuss("Discussion",["What is the most important technological change in technical work?","What did people used to do that we don't do anymore?"],
    '"People used to... but now they... / The most important change is..."'),
    s_end(11,UNIT1_1RO)]

def c12_1ro(th):
    return [s_title(12,UNIT1_1RO,"1ro Medio"),
    s_obj("Analyze a case study about a workplace accident applying reading strategies (pre-reading, focused reading, post-reading)."),
    s_section("📖","Case Study","The Day Everything Went Wrong"),
    s_discuss("Pre-Reading Prediction",["Look at the title: 'The Day Everything Went Wrong at Rivera's Workshop'","What do you think happened? Write a prediction."],
    '"I think... happened because..."'),
    s_reading("The Day Everything Went Wrong at Rivera's Workshop",[
    "It was a normal Tuesday morning at Rivera's Workshop in Valparaíso. Three technicians were working: Luis was <span class='keyword'>welding</span> a steel frame, Marcos was changing <span class='keyword'>brake pads</span>, and Sofia was testing an <span class='keyword'>electrical panel</span>.",
    "At 10:30 AM, things went wrong. Luis was welding without <span class='keyword'>safety goggles</span>. A <span class='keyword'>spark</span> hit a can of paint nearby. The paint caught <span class='keyword'>fire</span>!",
    "Marcos ran to help but slipped on <span class='keyword'>oil</span> on the floor. He fell and hurt his knee. Sofia quickly grabbed the <span class='keyword'>fire extinguisher</span> and put out the fire.",
    "The supervisor, Mr. Rivera, was very upset. He called a meeting: 'Three safety rules were broken today: no goggles, flammable materials near welding, and oil on the floor. This could have been much worse.'",
    "Nobody was seriously hurt, but the workshop was closed for 2 days for a complete <span class='keyword'>safety inspection</span>."]),
    s_table("Incident Report Form",["Field","Details"],
    [["Who was involved?","Luis, Marcos, Sofia"],["What happened?","Fire started from welding spark"],
    ["What caused it?","No goggles, paint near welding area"],["Consequences?","Fire, knee injury, 2-day closure"],
    ["Safety rules broken?","No PPE, flammable materials nearby, oil on floor"],["What should they do?","Wear PPE, clean floor, remove flammables"]]),
    s_discuss("Post-Reading Discussion",["What went wrong?","What safety rules were broken?","What would you do differently?"],
    '"The problem was... They should have... I would..."'),
    s_end(12,UNIT1_1RO)]

def c13_1ro(th):
    return [s_title(13,UNIT1_1RO,"1ro Medio"),
    s_obj("Orally describe a simple technical process using specialized vocabulary and sequence connectors."),
    s_section("🔤","Describing Processes","Using sequence connectors to explain step by step"),
    s_table("Sequence Connectors",["Connector","Example"],
    [["First","First, check the oil level."],["Second","Second, remove the old filter."],["Then","Then, install the new filter."],
    ["Next","Next, add fresh oil."],["After that","After that, start the engine."],["Finally","Finally, check for leaks."]]),
    s_reading("How to Change Engine Oil (Step by Step)",[
    "<b>First</b>, park the car on a flat surface and turn off the <span class='keyword'>engine</span>. Wait 5 minutes for the oil to cool.",
    "<b>Second</b>, place a container under the <span class='keyword'>oil drain plug</span>. Remove the plug with a <span class='keyword'>wrench</span> and let the old oil drain out.",
    "<b>Then</b>, remove the old <span class='keyword'>oil filter</span> and install a new one. Make sure it's tight.",
    "<b>Next</b>, put the drain plug back and tighten it. Add fresh <span class='keyword'>engine oil</span> through the oil cap on top.",
    "<b>After that</b>, start the engine and let it run for 2 minutes. Check the <span class='keyword'>dashboard</span> — the oil light should turn off.",
    "<b>Finally</b>, turn off the engine and check the <span class='keyword'>oil level</span> with the dipstick. It should be between the two marks."]),
    s_discuss("Your Turn — Describe a Process",["Choose a simple process from your specialty and describe it step by step using connectors.","Examples: How to change a tire / How to test a circuit / How to print a poster"],
    '"First, you need to... Then... Next... Finally..."'),
    s_end(13,UNIT1_1RO)]

def c14_1ro(th):
    return [s_title(14,UNIT1_1RO,"1ro Medio"),
    s_obj("Understand and compare information from five short texts about technical professionals from around the world (jigsaw reading)."),
    s_section("🌍","Professionals Around the World","Jigsaw Reading Activity"),
    s_reading("Hans — Automotive Technician, Germany",["Hans works at a BMW factory in Munich. He <span class='keyword'>has specialized</span> in electric vehicles <span class='keyword'>for 5 years</span>. He repairs <span class='keyword'>hybrid engines</span> and <span class='keyword'>battery systems</span>. 'Germany is the leader in automotive engineering,' he says."]),
    s_reading("Yuki — Electronics Engineer, Japan",["Yuki designs <span class='keyword'>microchips</span> at a Sony factory in Tokyo. She <span class='keyword'>has worked</span> there <span class='keyword'>since 2019</span>. She uses <span class='keyword'>CAD software</span> to design circuits. 'Japan is famous for electronics innovation,' she says."]),
    s_reading("Camila — Electrician, Chile",["Camila installs <span class='keyword'>solar panels</span> in Santiago. She <span class='keyword'>has installed</span> more than 200 systems <span class='keyword'>for 8 years</span>. 'Chile has the best solar energy potential in South America,' she says."]),
    s_reading("Mike — Industrial Welder, USA",["Mike welds <span class='keyword'>steel structures</span> for skyscrapers in New York. He <span class='keyword'>has worked</span> on 15 buildings <span class='keyword'>since 2012</span>. 'Every building I weld makes me proud,' he says."]),
    s_reading("Jake — Graphic Designer, Australia",["Jake operates a digital <span class='keyword'>printing press</span> in Sydney. He <span class='keyword'>has printed</span> magazines, posters, and packaging <span class='keyword'>for 12 years</span>. 'The printing industry is going digital, but quality still matters,' he says."]),
    s_table("Compare the Professionals",["Name","Country","Specialty","Experience","What they do"],
    [["Hans","Germany","Automotive","5 years","Repairs hybrid engines"],["Yuki","Japan","Electronics","Since 2019","Designs microchips"],
    ["Camila","Chile","Electricity","8 years","Installs solar panels"],["Mike","USA","Industrial","Since 2012","Welds steel structures"],
    ["Jake","Australia","Graphic Arts","12 years","Operates printing press"]]),
    s_end(14,UNIT1_1RO)]

def c15_1ro(th):
    return [s_title(15,UNIT1_1RO,"1ro Medio"),
    s_obj("Organize and rehearse an oral presentation titled 'My Future Career' using technical vocabulary and grammar structures learned."),
    s_section("🎤","Preparing Your Oral Presentation","'My Future Career' — Evaluation Preparation"),
    s_rubric("Oral Presentation Rubric (20 points)",
    [["Content (4)","Covers all 3 required topics clearly","Covers 2-3 topics","Covers 1-2 topics","Incomplete"],
    ["Vocabulary (4)","Uses 8+ technical words correctly","Uses 5-7 technical words","Uses 3-4 technical words","Uses 0-2 words"],
    ["Pronunciation (4)","Clear, mostly accurate","Some errors, understandable","Frequent errors","Very difficult to understand"],
    ["Fluency (4)","Smooth, natural pace","Some pauses, generally fluent","Many pauses, reads mainly","Cannot speak without reading"],
    ["Structure (4)","Clear intro, body, conclusion","Has structure, some gaps","Unclear structure","No structure"]],
    ["4 (Excellent)","3 (Good)","2 (Developing)","1 (Beginning)"]),
    s_table("Presentation Structure",["Section","What to include","Time"],
    [["Introduction","Name, specialty, why you chose it","30 sec"],
    ["Body — Tools","3 tools/equipment you know and what they're for","1 min"],
    ["Body — Skills","2 things you have learned or can do","30 sec"],
    ["Conclusion","Why your specialty is important + future goals","30 sec"]]),
    s_discuss("Model Sentences for Your Presentation",[],
    '"My name is... I study... because... / I know how to use a... It is used for... / I have learned to... / In the future, I want to..."'),
    s_end(15,UNIT1_1RO,"Practice your presentation at home! 📝")]

def c16_1ro(th):
    return [s_title(16,UNIT1_1RO,"1ro Medio"),
    s_obj("Deliver an oral presentation 'My Future Career' demonstrating technical vocabulary and grammar structures (Group A)."),
    s_section("🎤","Oral Presentations — Group A","📝 EVALUATION — Nota 1"),
    s_rubric("Evaluation Rubric (20 points)",
    [["Content (4)","Covers all topics clearly","Covers most topics","Covers some topics","Incomplete"],
    ["Vocabulary (4)","8+ technical words","5-7 words","3-4 words","0-2 words"],
    ["Pronunciation (4)","Clear, accurate","Some errors","Frequent errors","Very unclear"],
    ["Fluency (4)","Smooth, natural","Some pauses","Many pauses","Cannot continue"],
    ["Structure (4)","Clear organization","Some structure","Unclear","No structure"]],
    ["4 (Excellent)","3 (Good)","2 (Developing)","1 (Beginning)"]),
    s_discuss("Audience — Peer Feedback Form",["While listening to each presenter, write:","✅ One strength: something they did well","💡 One suggestion: something they could improve"]),
    s_end(16,UNIT1_1RO,"Great presentations! Group B is next class! 🎓")]

def c17_1ro(th):
    return [s_title(17,UNIT1_1RO,"1ro Medio"),
    s_obj("Deliver an oral presentation 'My Future Career' demonstrating technical vocabulary and grammar structures (Group B)."),
    s_section("🎤","Oral Presentations — Group B","📝 EVALUATION — Nota 1 (continued)"),
    s_rubric("Evaluation Rubric (20 points)",
    [["Content (4)","Covers all topics clearly","Covers most topics","Covers some topics","Incomplete"],
    ["Vocabulary (4)","8+ technical words","5-7 words","3-4 words","0-2 words"],
    ["Pronunciation (4)","Clear, accurate","Some errors","Frequent errors","Very unclear"],
    ["Fluency (4)","Smooth, natural","Some pauses","Many pauses","Cannot continue"],
    ["Structure (4)","Clear organization","Some structure","Unclear","No structure"]],
    ["4 (Excellent)","3 (Good)","2 (Developing)","1 (Beginning)"]),
    s_discuss("Audience — Peer Feedback Form",["While listening, write:","✅ One strength","💡 One suggestion"]),
    s_end(17,UNIT1_1RO,"All presentations complete! Well done everyone! 🏆")]

def c18_1ro(th):
    return [s_title(18,UNIT1_1RO,"1ro Medio"),
    s_obj("Demonstrate reading comprehension of technical texts using vocabulary and grammar from Unit 1 (written test)."),
    s_section("📝","Written Test — Nota 2","Reading Comprehension + Vocabulary + Grammar"),
    s_table("Test Structure",["Section","Content","Points"],
    [["Part 1","Vocabulary matching (15 items)","15"],["Part 2","Reading comprehension — short text","10"],
    ["Part 3","Grammar — Present Perfect + Since/For + Used to","10"],["Part 4","Sequence connectors — order a process","5"],
    ["","TOTAL","40"]]),
    s_discuss("Test-Taking Strategies",["Read ALL questions before starting","Underline key words in each question","Use context clues for unknown words",
    "Check your answers before submitting","Manage your time: 90 minutes total"]),
    s_section("🔮","Preview: Unit 2","Coming up next — more advanced topics!"),
    s_end(18,UNIT1_1RO,"Unit 1 complete! Great work this semester! 🎓🏆")]

CLASSES_1RO = {i:f for i,f in enumerate([None,c1_1ro,c2_1ro,c3_1ro,c4_1ro,c5_1ro,c6_1ro,c7_1ro,c8_1ro,c9_1ro,c10_1ro,c11_1ro,c12_1ro,c13_1ro,c14_1ro,c15_1ro,c16_1ro,c17_1ro,c18_1ro],0) if f}

# ═══════════════════ 3RO MEDIO — 9 CLASES × 5 ESPECIALIDADES ═══════════════════
UNIT1_3RO = "Technical Skills & Career Paths"
SPEC_DATA_3RO = {
    "automotriz":{"name":"Mecánica Automotriz","emoji":"🚗",
        "vocab":[("Engine","⚙️","The machine that powers a car"),("Brake Pad","🛑","Disc that creates friction to stop"),
        ("Transmission","⚙️","Sends power to wheels"),("Coolant","🌡️","Liquid that prevents overheating"),
        ("Wrench","🔧","Tool for turning bolts"),("Jack","⬆️","Device for lifting cars"),
        ("Spark Plug","⚡","Creates spark to ignite fuel"),("Oil Filter","🛢️","Cleans engine oil"),
        ("Radiator","🌡️","Cools the engine"),("Exhaust","💨","Carries waste gases"),
        ("Tire","🛞","Rubber wheel covering"),("Battery","🔋","Provides electrical power"),
        ("Alternator","⚡","Charges battery while driving"),("Diagnostic Scanner","📟","Reads car computer codes")],
        "text_title":"A Day in an Automotive Workshop",
        "text":["Carlos arrives at González Workshop at 8 AM. His first job: a car with <span class='keyword'>engine</span> problems. He connects the <span class='keyword'>diagnostic scanner</span> and reads error code P0301 — misfire in cylinder 1.",
        "He checks the <span class='keyword'>spark plugs</span>. Cylinder 1's plug is worn out. He replaces all four plugs, clears the code, and tests the engine. Problem solved!",
        "Next, he changes <span class='keyword'>brake pads</span> on a truck. He uses a <span class='keyword'>jack</span> to lift it, removes the wheel, and installs new pads. He checks the <span class='keyword'>brake fluid</span> level — it's low, so he adds more."],
        "case_title":"The Overheating Engine",
        "case":["A client brings her car: the temperature gauge is in the red zone. The <span class='keyword'>engine</span> is <span class='keyword'>overheating</span>.",
        "<b>Step 1:</b> Carlos checks the <span class='keyword'>coolant</span> level — it's empty! <b>Step 2:</b> He inspects the <span class='keyword'>radiator</span> — there's a small crack. <b>Step 3:</b> He tests the <span class='keyword'>thermostat</span> — it's stuck closed.",
        "<b>Solution:</b> Replace the radiator and thermostat. Add new coolant. Total repair time: 3 hours."],
        "safety_title":"Safety in the Automotive Workshop",
        "safety":["<b>Rule 1:</b> Always wear <span class='keyword'>safety goggles</span> when working under a car.","<b>Rule 2:</b> Use <span class='keyword'>jack stands</span> — never work under a car supported only by a jack.",
        "<b>Rule 3:</b> Wear <span class='keyword'>gloves</span> when handling chemicals (coolant, brake fluid, oil).","<b>Rule 4:</b> Keep a <span class='keyword'>fire extinguisher</span> near the work area."],
        "verbs":["check","repair","install","measure","test","replace","adjust","calibrate"]},
    "electricidad":{"name":"Electricidad","emoji":"⚡",
        "vocab":[("Wire","🔌","Carries electricity"),("Circuit Breaker","🔴","Stops excessive current"),
        ("Transformer","🔄","Changes voltage levels"),("Conduit","🔧","Pipe for wiring"),
        ("Multimeter","📟","Measures V/A/Ω"),("Switch","🔘","Controls circuit on/off"),
        ("Panel","📦","Distribution box"),("Ground","⏚","Safety earth connection"),
        ("Outlet","🔌","Wall socket"),("Fuse","💥","Breaks on overload"),
        ("Insulation","🛡️","Prevents shock"),("Voltage","⚡","Electrical pressure"),
        ("Current","⚡","Flow of electricity"),("Load","💡","Device using power")],
        "text_title":"A Day as an Electrician","text":["Miguel arrives at a construction site at 7:30 AM. Today he is installing the <span class='keyword'>electrical panel</span> for a new apartment building.","He runs <span class='keyword'>conduit</span> through the walls and pulls <span class='keyword'>wires</span> to each room. He installs <span class='keyword'>outlets</span>, <span class='keyword'>switches</span>, and connects everything to the <span class='keyword'>circuit breakers</span>.","Before finishing, he uses his <span class='keyword'>multimeter</span> to test every circuit. Safety first — all connections must be perfect."],
        "case_title":"The Power Outage","case":["A restaurant calls: half the building has no power. Miguel checks the <span class='keyword'>electrical panel</span> — a <span class='keyword'>circuit breaker</span> has tripped.","He tests the circuit with a <span class='keyword'>multimeter</span>. The <span class='keyword'>voltage</span> is 0V on one phase. He traces the wires and finds a damaged <span class='keyword'>wire</span> behind the kitchen wall.","<b>Solution:</b> Replace the damaged wire, reset the breaker. Power is restored in 2 hours."],
        "safety_title":"Electrical Safety Rules","safety":["<b>Rule 1:</b> Always turn OFF power before working on a circuit.","<b>Rule 2:</b> Use a <span class='keyword'>multimeter</span> to verify zero voltage.","<b>Rule 3:</b> Wear insulated <span class='keyword'>gloves</span> rated for the voltage.","<b>Rule 4:</b> Never work alone on live circuits."],
        "verbs":["wire","connect","install","test","measure","troubleshoot","ground","calibrate"]},
    "electronica":{"name":"Electrónica","emoji":"📟",
        "vocab":[("Resistor","⚡","Limits current flow"),("Capacitor","⚡","Stores energy"),
        ("LED","💡","Light-emitting diode"),("Transistor","🔀","Switches/amplifies signals"),
        ("PCB","📟","Printed circuit board"),("Microcontroller","🤖","Programmable chip"),
        ("Sensor","📡","Detects changes"),("Oscilloscope","📊","Displays waveforms"),
        ("Solder","🔥","Joining metal"),("Breadboard","📟","Prototype board"),
        ("IC","📟","Integrated circuit"),("Diode","➡️","One-way current"),
        ("Relay","🔀","Electric switch"),("Antenna","📡","Receives/sends signals")],
        "text_title":"A Day in Electronics","text":["Ana works at a tech company designing <span class='keyword'>PCBs</span>. Today she's building a prototype temperature monitoring system.","She places <span class='keyword'>resistors</span>, <span class='keyword'>LEDs</span>, and a <span class='keyword'>microcontroller</span> on a <span class='keyword'>breadboard</span>. She connects a <span class='keyword'>sensor</span> and programs the system using Arduino.","She uses an <span class='keyword'>oscilloscope</span> to check the signal quality. Everything works! Tomorrow she'll design the final <span class='keyword'>PCB</span>."],
        "case_title":"The Faulty Circuit","case":["A factory reports that their sensor system gives wrong readings. Ana inspects the <span class='keyword'>PCB</span>.","She uses an <span class='keyword'>oscilloscope</span> — the signal from the <span class='keyword'>sensor</span> is noisy. She checks the <span class='keyword'>capacitors</span> — one is damaged.","<b>Solution:</b> Replace the damaged capacitor and add a filter circuit. The readings are now accurate."],
        "safety_title":"Electronics Workshop Safety","safety":["<b>Rule 1:</b> Always discharge <span class='keyword'>capacitors</span> before touching a circuit.","<b>Rule 2:</b> Use an <span class='keyword'>anti-static wristband</span> to protect sensitive components.","<b>Rule 3:</b> Wear safety glasses when <span class='keyword'>soldering</span>.","<b>Rule 4:</b> Ensure proper ventilation — solder fumes are harmful."],
        "verbs":["program","solder","test","measure","design","debug","assemble","calibrate"]},
    "grafica":{"name":"Gráfica","emoji":"🖨️",
        "vocab":[("Printing Press","🖨️","Machine for mass printing"),("Ink","🎨","Colored liquid for printing"),
        ("Layout","📐","Page arrangement"),("Proof","📄","Test print"),
        ("CMYK","🎨","Print color model"),("Resolution","🔍","Image quality (DPI)"),
        ("Substrate","📄","Material to print on"),("Lamination","✨","Protective coating"),
        ("Binding","📚","Joining pages"),("Die-cutting","✂️","Cutting shapes"),
        ("Registration","📐","Color alignment"),("Bleed","📐","Print beyond trim"),
        ("Prepress","💻","Before printing phase"),("Finishing","✂️","Post-print processing")],
        "text_title":"A Day in Graphic Arts","text":["Diego operates a <span class='keyword'>printing press</span> at a commercial print shop. Today he's printing 5,000 brochures for a client.","First, he checks the <span class='keyword'>proof</span> — the colors look good in <span class='keyword'>CMYK</span>. He loads the <span class='keyword'>substrate</span> (glossy paper) and sets up the press.","After printing, the brochures go to <span class='keyword'>finishing</span>: <span class='keyword'>lamination</span>, folding, and trimming. Diego checks <span class='keyword'>registration</span> — all colors are perfectly aligned."],
        "case_title":"The Color Mismatch","case":["A client complains: the printed colors don't match the design. Diego investigates.","He checks the file: it was saved in RGB, not <span class='keyword'>CMYK</span>. The <span class='keyword'>resolution</span> was also only 72 DPI instead of 300.","<b>Solution:</b> Convert the file to CMYK, increase resolution to 300 DPI, make a new <span class='keyword'>proof</span>, get client approval, reprint."],
        "safety_title":"Safety in Graphic Arts","safety":["<b>Rule 1:</b> Keep hands away from moving parts of the <span class='keyword'>printing press</span>.","<b>Rule 2:</b> Wear <span class='keyword'>gloves</span> when handling inks and chemicals.","<b>Rule 3:</b> Use hearing protection near loud machinery.","<b>Rule 4:</b> Ensure proper ventilation for ink fumes."],
        "verbs":["print","design","align","cut","laminate","proof","calibrate","bind"]},
    "industrial":{"name":"Mecánica Industrial","emoji":"🏭",
        "vocab":[("Lathe","⚙️","Shapes metal by rotating"),("Milling Machine","⚙️","Cuts/shapes metal"),
        ("Welding Torch","🔥","Joins metals with heat"),("Grinding Wheel","💫","Smooths metal"),
        ("Bench Vise","🗜️","Workbench clamp"),("Steel","🔩","Strong metal alloy"),
        ("CNC Machine","🤖","Computer-controlled tools"),("Caliper","📐","Precision measuring"),
        ("Drill Press","🔩","Fixed drill for precision"),("Anvil","⚒️","Metal-shaping block"),
        ("PPE","🦺","Protective equipment"),("Hydraulic Press","⬇️","Shapes metal with pressure"),
        ("Bolt","🔩","Threaded metal pin"),("Bearing","⚙️","Reduces friction in machines")],
        "text_title":"A Day in Industrial Mechanics","text":["Roberto works in a metal fabrication factory. Today he's making custom steel parts for a mining company.","He programs the <span class='keyword'>CNC machine</span> to cut steel plates with precision. Then he uses the <span class='keyword'>lathe</span> to shape cylindrical parts and a <span class='keyword'>milling machine</span> for flat surfaces.","He measures every piece with <span class='keyword'>calipers</span> — tolerance is 0.01mm. After machining, he uses the <span class='keyword'>grinding wheel</span> to smooth the edges."],
        "case_title":"The Defective Weld","case":["A construction company reports cracks in welded steel beams. Roberto inspects the welds.","He finds the welds have <span class='keyword'>porosity</span> (tiny holes). The <span class='keyword'>welding</span> was done too fast, without enough heat.","<b>Solution:</b> Remove defective welds, clean the surfaces, re-weld at proper speed and temperature. All new welds pass ultrasonic testing."],
        "safety_title":"Industrial Workshop Safety","safety":["<b>Rule 1:</b> Always wear <span class='keyword'>welding helmet</span>, gloves, and apron when welding.","<b>Rule 2:</b> Use <span class='keyword'>ear protection</span> near grinding and cutting machines.","<b>Rule 3:</b> Never operate the <span class='keyword'>lathe</span> without safety guards.","<b>Rule 4:</b> Check all <span class='keyword'>PPE</span> before starting work."],
        "verbs":["weld","machine","grind","measure","cut","drill","assemble","calibrate"]},
}

def gen_3ro(spec_key, th):
    d = SPEC_DATA_3RO[spec_key]; n = d["name"]; all_cls = {}
    # Class 1: Vocabulary
    def c1(th):
        slides = [s_title(1,UNIT1_3RO,"3ro Medio",n),s_obj(f"Identify basic technical English vocabulary for {n}."),s_section(d["emoji"],f"{n} Vocabulary","14 key words")]
        for i,(w,e,df) in enumerate(d["vocab"],1):
            slides.append(s_vocab(w,"",e,df,f"The technician uses the {w.lower()} every day.",i,len(d["vocab"])))
        slides.append(s_end(1,UNIT1_3RO));return slides
    # Class 2: Reading
    def c2(th):
        return [s_title(2,UNIT1_3RO,"3ro Medio",n),s_obj(f"Understand explicit information in a text about {n}."),
        s_reading(d["text_title"],d["text"]),
        s_exercise("Comprehension",[("What is the main topic? ___","The daily work routine"),("What tools are mentioned? ___","Various specialty tools"),("What is the purpose of the text? ___","To inform about the profession")]),
        s_end(2,UNIT1_3RO)]
    # Class 3: Simple Present + Verbs
    def c3(th):
        slides = [s_title(3,UNIT1_3RO,"3ro Medio",n),s_obj(f"Use Simple Present and action verbs to describe {n} routines."),
        s_section("📐","Action Verbs","8 essential verbs")]
        for i,v in enumerate(d["verbs"],1):
            slides.append(s_vocab(v.capitalize(),"","🔧",f"A common action in {n}",f"The technician {v}s the equipment every day.",i,len(d["verbs"])))
        slides.append(s_exercise("Complete the sentences",[
        (f"A {n} technician ___ the equipment every day.",d["verbs"][0]+"s"),
        (f"She ___ the components carefully.",d["verbs"][4]+"s"),
        (f"They ___ new parts when needed.",d["verbs"][5])]))
        slides.append(s_end(3,UNIT1_3RO));return slides
    # Class 4: Case Study
    def c4(th):
        return [s_title(4,UNIT1_3RO,"3ro Medio",n),s_obj(f"Analyze a technical case study in {n}."),
        s_reading(d["case_title"],d["case"]),
        s_table("Problem → Solution",["Stage","Details"],[["Problem","Equipment malfunction"],["Diagnosis","Systematic testing"],["Solution","Replace/repair components"]]),
        s_discuss("Discussion",["What was the problem?","What steps did the technician follow?","Do you agree with the solution?"],'"The problem was... First they... The solution was..."'),
        s_end(4,UNIT1_3RO)]
    # Class 5: Video + Description
    def c5(th):
        return [s_title(5,UNIT1_3RO,"3ro Medio",n),s_obj(f"Understand information from a video and produce oral descriptions about {n}."),
        s_discuss("Pre-Viewing Questions",["What do you expect to see in the video?","What vocabulary might appear?"]),
        s_discuss("Post-Viewing — Describe & Explain",["Describe the main equipment shown","What process was demonstrated?","What tools were used?"],
        '"In the video, I saw... They used... to... The process involves..."'),
        s_end(5,UNIT1_3RO)]
    # Class 6: Safety
    def c6(th):
        return [s_title(6,UNIT1_3RO,"3ro Medio",n),s_obj(f"Understand and evaluate safety rules in English for {n}."),
        s_reading(d["safety_title"],d["safety"]),
        s_table("Safety Analysis",["Rule","Reason","PPE Required"],
        [["Wear goggles","Protect eyes from debris","Safety goggles"],["Wear gloves","Protect hands","Work gloves"],
        ["Use proper equipment","Prevent accidents","Varies"],["Follow procedures","Ensure safety","All required PPE"]]),
        s_discuss("Create Your Safety Poster",["Write 5 safety rules in English for your workshop","Use: Always wear... / Never touch... / In case of emergency..."]),
        s_end(6,UNIT1_3RO)]
    # Class 7: Prep evaluation
    def c7(th):
        return [s_title(7,UNIT1_3RO,"3ro Medio",n),s_obj(f"Organize and rehearse an oral presentation about {n} skills."),
        s_rubric(f"Oral Presentation Rubric — {n} (20 pts)",
        [["Content (4)","Complete coverage","Most topics","Some topics","Incomplete"],
        ["Vocabulary (4)","8+ technical words","5-7 words","3-4 words","0-2 words"],
        ["Pronunciation (4)","Clear, accurate","Some errors","Frequent errors","Very unclear"],
        ["Fluency (4)","Smooth delivery","Some pauses","Many pauses","Cannot continue"],
        ["Structure (4)","Well organized","Some structure","Unclear","None"]],
        ["4","3","2","1"]),
        s_discuss("Presentation Template",[],'"My name is... I study '+n+'. I know how to use... I have learned to... This specialty is important because..."'),
        s_end(7,UNIT1_3RO,"Practice for your evaluation next class!")]
    # Class 8: Evaluation
    def c8(th):
        return [s_title(8,UNIT1_3RO,"3ro Medio",n),s_obj(f"Deliver an oral presentation about your skills in {n}."),
        s_section("📝","Oral Evaluation","Nota 1 — Semestre 1"),
        s_rubric(f"Rubric — {n} (20 pts)",
        [["Content (4)","Complete","Most","Some","Incomplete"],["Vocabulary (4)","8+","5-7","3-4","0-2"],
        ["Pronunciation (4)","Clear","Some errors","Frequent","Unclear"],["Fluency (4)","Smooth","Pauses","Many pauses","Blocked"],
        ["Structure (4)","Organized","Some","Unclear","None"]],["4","3","2","1"]),
        s_end(8,UNIT1_3RO,"Great job on your presentation! 🏆")]
    # Class 9: Review
    def c9(th):
        return [s_title(9,UNIT1_3RO,"3ro Medio",n),s_obj(f"Synthesize Unit 1 learning about {n}."),
        s_section("🎮","Review Game","Jeopardy Time!"),
        s_table("Jeopardy Categories",["Category","Example Question"],
        [["Tools","What tool measures voltage?"],["Safety","Name 3 items of PPE"],["Processes","Describe 3 steps of a repair"],["Vocabulary","Define 'diagnostic scanner'"]]),
        s_discuss("Self-Assessment",["I can name ___ tools in English","I can describe a process using sequence connectors","I need to practice more on ___"]),
        s_section("🔮","Preview: Unit 2","Coming up: Technical challenges and global issues"),
        s_end(9,UNIT1_3RO,"Unit 1 complete! See you in Unit 2! 🎓")]
    return {1:c1,2:c2,3:c3,4:c4,5:c5,6:c6,7:c7,8:c8,9:c9}

# ═══════════════════ 4TO MEDIO — 9 CLASES × 5 ESPECIALIDADES ═══════════════════
UNIT1_4TO = "Professional Profile & Workplace English"
SPEC_DATA_4TO = {k:v for k,v in SPEC_DATA_3RO.items()}  # Reuse vocab/case data, different class structure

def gen_4to(spec_key, th):
    d = SPEC_DATA_4TO[spec_key]; n = d["name"]
    def c1(th):
        adv_vocab = d["vocab"][:8]
        slides = [s_title(1,UNIT1_4TO,"4to Medio",n),s_obj(f"Identify advanced vocabulary and describe professional goals in {n}."),s_section(d["emoji"],f"Advanced {n} Vocabulary","8 professional-level words")]
        for i,(w,e,df) in enumerate(adv_vocab,1):
            slides.append(s_vocab(w,"",e,df,f"A professional in {n} must understand {w.lower()}.",i,len(adv_vocab)))
        slides.append(s_discuss("Career Goals",["Where do you see yourself in 5 years?","What skills do you need to develop?"],'"First, I will... Then, I plan to... My goal is to..."'))
        slides.append(s_end(1,UNIT1_4TO));return slides
    def c2(th):
        return [s_title(2,UNIT1_4TO,"4to Medio",n),s_obj(f"Analyze a career trajectory case study in {n}."),
        s_reading(f"Career Path in {n}",["A young technician describes their journey: vocational school, internship, first job, specialization.",
        "They explain how <span class='keyword'>English</span> helped them read technical manuals and attend international training.",
        "'Without English, I couldn't have advanced in my career,' they say. 'Technical manuals are in English.'"]),
        s_table("Career Path Analysis",["Stage","Skills Developed","Role of English"],
        [["Education","Basic technical skills","Learning vocabulary"],["Internship","Practical experience","Reading manuals"],
        ["First Job","Professional skills","Communicating with clients"],["Specialization","Advanced expertise","International training"]]),
        s_end(2,UNIT1_4TO)]
    def c3(th):
        return [s_title(3,UNIT1_4TO,"4to Medio",n),s_obj(f"Create a professional CV in English for {n}."),
        s_section("📄","Your CV in English","Building your professional profile"),
        s_table("CV Sections",["Section","What to include","Example"],
        [["Objective","Career goal","'To obtain a position as a "+n+" technician'"],
        ["Education","School, specialty","Liceo TP, "+n],["Skills","5+ technical skills","Equipment operation, diagnostics"],
        ["Languages","Language level","Spanish (native), English (basic)"]]),
        s_table("Action Verbs for CV",["Verb","Example"],
        [["Operated","Operated diagnostic equipment"],["Maintained","Maintained electrical systems"],
        ["Installed","Installed components"],["Designed","Designed circuit layouts"],
        ["Repaired","Repaired faulty equipment"]]),
        s_end(3,UNIT1_4TO)]
    def c4(th):
        return [s_title(4,UNIT1_4TO,"4to Medio",n),s_obj(f"Practice job interview skills in English for {n}."),
        s_section("💼","Job Interview Preparation","Common questions and strategies"),
        s_table("Interview Questions",["#","Question","Strategy"],
        [["1","Tell me about yourself.","Name + education + specialty + goal"],
        ["2","Why do you want this job?","Interest + skills + contribution"],
        ["3","What are your strengths?","Technical skills + soft skills"],
        ["4","What experience do you have?","Internship + projects + learning"]]),
        s_discuss("Practice Your Answers",[],'"My name is... I study '+n+' at... I am interested in this position because... My strengths are... I have experience in..."'),
        s_end(4,UNIT1_4TO,"Practice for your mock interview!")]
    def c5(th):
        return [s_title(5,UNIT1_4TO,"4to Medio",n),s_obj(f"Demonstrate interview skills in a mock job interview for {n}."),
        s_section("📝","Mock Job Interview","Nota 1 — Semestre 1"),
        s_rubric(f"Interview Rubric — {n} (20 pts)",
        [["Pronunciation (4)","Clear","Some errors","Frequent errors","Unclear"],
        ["Vocabulary (4)","Technical + professional","Mostly technical","Basic","Insufficient"],
        ["Coherence (4)","Logical, complete answers","Mostly coherent","Some gaps","Incoherent"],
        ["Fluency (4)","Natural pace","Some pauses","Many pauses","Cannot continue"],
        ["Presentation (4)","Professional manner","Good manner","Casual","Unprepared"]],
        ["4","3","2","1"]),
        s_end(5,UNIT1_4TO,"Great interview! 🏆")]
    def c6(th):
        return [s_title(6,UNIT1_4TO,"4to Medio",n),s_obj("Write formal emails and messages in English for workplace communication."),
        s_section("✉️","Professional Emails","Formal communication in English"),
        s_reading("Email Structure",["<b>Subject:</b> Clear and specific","<b>Greeting:</b> Dear Mr./Ms. [Name],",
        "<b>Opening:</b> I am writing to inquire about...",
        "<b>Body:</b> Clear, professional language","<b>Closing:</b> Kind regards, / Best regards,","<b>Signature:</b> Full name + contact info"]),
        s_table("Formal vs Informal",["Formal","Informal"],
        [["Dear Sir/Madam","Hey!"],["I would like to request","I want"],["Please find attached","Here's the file"],
        ["Kind regards","Bye!"],["I am writing to inform you","Just letting you know"]]),
        s_end(6,UNIT1_4TO)]
    def c7(th):
        return [s_title(7,UNIT1_4TO,"4to Medio",n),s_obj(f"Analyze workplace scenarios from a video about {n}."),
        s_discuss("Video Analysis Questions",["What impressed you most about the workplace?","Would you like to work in that environment?","What skills do you need to develop?"]),
        s_end(7,UNIT1_4TO)]
    def c8(th):
        return [s_title(8,UNIT1_4TO,"4to Medio",n),s_obj(f"Understand and produce workplace safety instructions in English for {n}."),
        s_reading(d["safety_title"],d["safety"]),
        s_table("Safety Signs",["Sign","Meaning","Color"],
        [["⚠️ WARNING","Potential hazard","Yellow"],["🚫 DANGER","Immediate danger","Red"],
        ["ℹ️ CAUTION","Be careful","Yellow"],["🚪 EMERGENCY EXIT","Evacuation route","Green"]]),
        s_end(8,UNIT1_4TO)]
    def c9(th):
        return [s_title(9,UNIT1_4TO,"4to Medio",n),s_obj(f"Synthesize Unit 1 learning about professional English for {n}."),
        s_section("🎮","Career Jeopardy","Final Review Game"),
        s_table("Categories",["Category","Topics"],
        [["Vocabulary","Technical terms"],["CV Writing","Sections & verbs"],["Interview","Questions & strategies"],
        ["Safety","Rules & signs"],["Communication","Emails & messages"]]),
        s_discuss("Reflection",["In Unit 1, I learned...","The most useful skill was...","I still need to practice..."]),
        s_section("🔮","Preview: Unit 2","Advanced technical reading & workplace challenges"),
        s_end(9,UNIT1_4TO,"Unit 1 complete! Excellent work! 🎓🏆")]
    return {1:c1,2:c2,3:c3,4:c4,5:c5,6:c6,7:c7,8:c8,9:c9}

# ═══════════════════ MAIN ═══════════════════
def main():
    total = 0
    # 1ro Medio
    th = THEMES["1ro Medio"]
    out_dir = os.path.join(BASE_DIR,"1ro Medio","Unidad 1","Presentaciones")
    os.makedirs(out_dir, exist_ok=True)
    for cn, fn in CLASSES_1RO.items():
        slides = fn(th)
        html = assemble(slides, th, f"Clase {cn} — {UNIT1_1RO} — 1ro Medio")
        path = os.path.join(out_dir, f"clase_{cn}.html")
        with open(path,"w",encoding="utf-8") as f: f.write(html)
        total += 1; print(f"  [OK] 1ro Medio / Clase {cn}")

    # 3ro Medio
    th = THEMES["3ro Medio"]
    out_dir = os.path.join(BASE_DIR,"3ro Medio","Unidad 1","Presentaciones")
    os.makedirs(out_dir, exist_ok=True)
    for spec_key, spec_name in SPEC_MAP.items():
        classes = gen_3ro(spec_key, th)
        for cn, fn in classes.items():
            slides = fn(th)
            html = assemble(slides, th, f"Clase {cn} — {UNIT1_3RO} — 3ro Medio — {spec_name}")
            fname = f"clase_{cn}_{safe(spec_name)}.html"
            with open(os.path.join(out_dir, fname),"w",encoding="utf-8") as f: f.write(html)
            total += 1
        print(f"  [OK] 3ro Medio / {spec_name} (9 clases)")

    # 4to Medio
    th = THEMES["4to Medio"]
    out_dir = os.path.join(BASE_DIR,"4to Medio","Unidad 1","Presentaciones")
    os.makedirs(out_dir, exist_ok=True)
    for spec_key, spec_name in SPEC_MAP.items():
        classes = gen_4to(spec_key, th)
        for cn, fn in classes.items():
            slides = fn(th)
            html = assemble(slides, th, f"Clase {cn} — {UNIT1_4TO} — 4to Medio — {spec_name}")
            fname = f"clase_{cn}_{safe(spec_name)}.html"
            with open(os.path.join(out_dir, fname),"w",encoding="utf-8") as f: f.write(html)
            total += 1
        print(f"  [OK] 4to Medio / {spec_name} (9 clases)")

    print(f"\n{'='*55}")
    print(f"  COMPLETADO: {total} presentaciones V2 generadas")
    print(f"{'='*55}")

if __name__ == "__main__":
    main()
