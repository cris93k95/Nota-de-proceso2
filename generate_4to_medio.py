#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generates all 20 HTML planificacion files for 4 Medio (5 specialties x 4 units).
4to Medio: ends Nov 12, ~33 classes total, 1 session/week (90 min).
Greater complexity than 3ro: job preparation, interviews, project defense.
OA from Bases Curriculares 2019 (4to Medio):
  OA1: Comprender textos orales y escritos para un proposito especifico.
  OA2: Producir textos orales y escritos claros.
  OA3: Utilizar su conocimiento del ingles para construir postura personal critica.
  OA4: Producir y comprender con fluidez textos orales y escritos claros.
"""
import os

BASE = r"c:\Users\crist\OneDrive\Escritorio\2026\4to Medio"

SPECIALTIES = {
    "automotriz": {
        "name": "Mecánica Automotriz",
        "adj": "automotriz",
        "color1": "#b71c1c", "color2": "#d32f2f",
        "bg_light": "#ffebee", "bg_accent": "#ffcdd2",
        "text_color": "#b71c1c",
    },
    "electricidad": {
        "name": "Electricidad",
        "adj": "eléctrica",
        "color1": "#e65100", "color2": "#f57c00",
        "bg_light": "#fff3e0", "bg_accent": "#ffe0b2",
        "text_color": "#e65100",
    },
    "electronica": {
        "name": "Electrónica",
        "adj": "electrónica",
        "color1": "#1b5e20", "color2": "#2e7d32",
        "bg_light": "#e8f5e9", "bg_accent": "#c8e6c9",
        "text_color": "#1b5e20",
    },
    "industrial": {
        "name": "Mecánica Industrial",
        "adj": "industrial",
        "color1": "#263238", "color2": "#455a64",
        "bg_light": "#eceff1", "bg_accent": "#cfd8dc",
        "text_color": "#263238",
    },
}


# ================= UNIT 1: Professional Profile & Workplace English =================

def u1_classes(sp):
    """Unit 1: Professional Profile & Workplace English — 9 classes, March-April"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        vocab_area = "engine diagnostics, OBD scanner, fuel injection, turbocharger, hybrid system, torque, horsepower, alignment"
        reading1 = "an adapted text: <em>The Modern Automotive Technician</em> — describing the evolving role of mechanics: from manual repairs to computer-assisted diagnostics, hybrid/electric vehicles."
        case_study = "Case Study: <em>From Workshop to Dealership</em> — Carlos, a Chilean automotive technician, describes his career path: vocational school, internship at a workshop, certification, and current job at a dealership. He explains how English helped him read technical manuals and attend a training in Germany."
        cv_focus = "automotive technician CV: technical skills (engine diagnostics, brake systems, electronic fuel injection), certifications (ASE equivalent), workshop experience"
        interview_qs = "What experience do you have with engine diagnostics?, Can you describe a difficult repair you completed?, What safety procedures do you follow?"
        video_topic = "a YouTube video about a day in a modern car dealership service department (adapted, 5 min)"
        safety_vocab = "jack stand safety, chemical handling (coolant, brake fluid), PPE in automotive workshops, lifting procedures"
    elif sp == "electricidad":
        vocab_area = "three-phase power, circuit breaker, transformer, voltage regulator, conduit, switchgear, grounding, load calculation"
        reading1 = "an adapted text: <em>The Professional Electrician in 2026</em> — describing career paths: residential, commercial, and industrial electricians, renewable energy specialists, smart home installers."
        case_study = "Case Study: <em>Powering a Career</em> — María, a Chilean electrician, shares her career journey: technical school, apprenticeship in residential wiring, specialization in solar panel installation, and starting her own business. She uses English to read international electrical codes."
        cv_focus = "electrician CV: technical skills (wiring, circuit design, solar installation), certifications (SEC license), project experience"
        interview_qs = "What types of electrical installations have you worked on?, How do you ensure compliance with safety codes?, Describe a challenging project you completed."
        video_topic = "a YouTube video about smart home electrical installation by a professional electrician (adapted, 5 min)"
        safety_vocab = "lockout/tagout procedures, arc flash protection, voltage testing before work, PPE for electrical work, grounding verification"
    elif sp == "electronica":
        vocab_area = "microcontroller, PCB design, firmware, oscilloscope, soldering station, IoT sensor, embedded system, signal processing"
        reading1 = "an adapted text: <em>Electronics Technicians in the Digital Age</em> — describing career opportunities: PCB manufacturing, IoT development, telecommunications, medical device maintenance."
        case_study = "Case Study: <em>Building a Tech Career</em> — Diego, a Chilean electronics technician, shares his path: technical school, internship at a telecommunications company, self-taught programming (Arduino/Raspberry Pi), and current role maintaining medical equipment at a hospital. English was key for reading datasheets."
        cv_focus = "electronics technician CV: technical skills (PCB assembly, microcontroller programming, equipment calibration), certifications, lab experience"
        interview_qs = "What experience do you have with PCB assembly?, Can you program microcontrollers?, How do you troubleshoot electronic circuits?"
        video_topic = "a YouTube video about IoT device assembly and testing in a modern electronics lab (adapted, 5 min)"
        safety_vocab = "ESD (electrostatic discharge) prevention, soldering safety, chemical handling (flux, solvents), proper ventilation in electronics labs"
    elif sp == "grafica":
        vocab_area = "offset printing, CMYK color model, prepress, die-cutting, substrate, resolution (DPI), color management, bindery"
        reading1 = "an adapted text: <em>The Modern Graphic Technician</em> — describing the evolution from traditional to digital printing: wide-format, packaging, 3D printing of prototypes, sustainable printing practices."
        case_study = "Case Study: <em>Ink to Innovation</em> — Valentina, a Chilean graphic technician, describes her career: school, internship at a print shop, specialization in packaging design, now working for an international company. English helps her communicate with foreign suppliers and use design software."
        cv_focus = "graphic technician CV: technical skills (offset/digital printing, prepress, color management), software (Adobe Suite), portfolio highlights"
        interview_qs = "What printing technologies are you experienced with?, How do you ensure color accuracy?, Describe a complex print job you managed."
        video_topic = "a YouTube video about a modern print production facility showing the workflow from design to finished product (adapted, 5 min)"
        safety_vocab = "ink and solvent handling, machine guarding on presses, proper ventilation, noise protection, material handling for paper rolls"
    else:  # industrial
        vocab_area = "CNC machine, lathe, milling, hydraulic press, welding (MIG/TIG), quality control, tolerance, technical drawing"
        reading1 = "an adapted text: <em>Industrial Mechanics in the Age of Automation</em> — describing how Industry 4.0 is changing the field: CNC programming, robotic maintenance, predictive maintenance, 3D metal printing."
        case_study = "Case Study: <em>From Apprentice to Specialist</em> — Andrés, a Chilean industrial mechanic, shares his career: technical school, apprenticeship in a mining company, specialization in CNC programming, now supervising a production line. English was essential for reading machine manuals and communicating with foreign engineers."
        cv_focus = "industrial mechanic CV: technical skills (CNC operation, welding, hydraulics), certifications, industrial experience"
        interview_qs = "What CNC machines can you operate?, How do you read and interpret technical drawings?, Describe your experience with preventive maintenance."
        video_topic = "a YouTube video about a modern CNC machining center and its operator workflow (adapted, 5 min)"
        safety_vocab = "machine lockout procedures, welding safety (fumes, UV protection), heavy lifting protocols, PPE in industrial workshops, confined space awareness"

    classes = [
        # Class 1: Vocabulary & Career Exploration
        {
            "title": "Advanced Technical Vocabulary & Career Goals",
            "oa": "OA1",
            "bloom": f"Identificar vocabulario técnico avanzado en inglés relacionado con {n} y describir metas profesionales a corto y largo plazo.",
            "inicio": f"""<ul>
                <li>Docente saluda en inglés y contextualiza: <em>\"This is your final year. This year, English will help you prepare for your professional life in {n}.\"</em></li>
                <li>Activación: <em>\"What are your career goals after graduation? Where do you see yourself in 5 years?\"</em> — quick-write (3 min).</li>
                <li>Se muestran 3-4 imágenes de profesionales del área trabajando en contextos internacionales.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Vocabulary expansion (20 min):</b> Presentación de vocabulario técnico avanzado: {vocab_area}. Los estudiantes completan un <em>vocabulary map</em>: palabra → definición → imagen → oración de ejemplo.</li>
                <li><b>Reading (20 min):</b> Lectura guiada de {reading1} Los estudiantes subrayan vocabulario nuevo y responden: <em>\"What skills does a modern {n.lower()} professional need?\"</em></li>
                <li><b>Career mapping (15 min):</b> En parejas, los estudiantes crean un <em>\"Career Pathway Map\"</em>: Technical School → Internship → First Job → Specialization → Future Goal. Usan frases: <em>\"First, I will... Then, I plan to... My goal is to...\"</em></li>
                <li><b>Sharing (5 min):</b> 3-4 parejas comparten sus mapas con la clase.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Ticket de salida: escribir 3 metas profesionales usando el vocabulario nuevo.</li>
                <li>Preview de la unidad: <em>\"This unit we will prepare your professional profile in English: CV, interview skills, and workplace communication.\"</em></li>
            </ul>""",
            "recursos": f"Imágenes de profesionales de {n.lower()} en contextos internacionales, ficha de vocabulary map, ficha de Career Pathway Map, pizarra.",
            "evaluacion": "Diagnóstica informal — el docente observa nivel de vocabulario, capacidad de expresión escrita y oral comparado con 3° Medio.",
        },
        # Class 2: Reading a Professional Profile / Case Study
        {
            "title": "Case Study: A Professional Career Path",
            "oa": "OA1 · OA3",
            "bloom": f"Analizar un estudio de caso sobre la trayectoria profesional de un técnico de {n}, identificando hitos clave, habilidades requeridas y el rol del inglés en su carrera.",
            "inicio": f"""<ul>
                <li>Warm-up: repaso de vocabulario con <em>\"Word Relay\"</em> — en equipos, cada estudiante dice una palabra técnica en inglés; el equipo con más palabras gana.</li>
                <li>Pre-reading: <em>\"What steps does someone take to become a successful professional in {n.lower()}?\"</em> — lluvia de ideas.</li>
                <li>Se introduce el concepto de <em>Case Study</em> como herramienta de aprendizaje.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {case_study} Lectura guiada con pausas. Los estudiantes completan una tabla:
                    <ul>
                        <li><b>Stage</b> (education, internship, first job, specialization)</li>
                        <li><b>Skills developed</b> at each stage</li>
                        <li><b>Role of English</b> at each stage</li>
                        <li><b>Challenges faced</b></li>
                    </ul>
                </li>
                <li><b>Comprehension (15 min):</b> 8 preguntas: 4 explícitas + 4 de análisis crítico (<em>\"Why was English important for his/her career?\"</em>, <em>\"What would you do differently?\"</em>).</li>
                <li><b>Discussion (15 min):</b> En grupos de 3: <em>\"Compare this career path to your own plans. What is similar? What is different?\"</em> Usar: <em>\"Like him/her, I will... Unlike him/her, I plan to... I agree/disagree that...\"</em></li>
                <li><b>Wrap-up (5 min):</b> Plenario: 2-3 grupos comparten conclusiones.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Reflexión escrita (3 líneas): <em>\"What is the most important lesson from this case study for my own career?\"</em></li>
                <li>Preview: <em>\"Next class, we will build your professional CV in English.\"</em></li>
            </ul>""",
            "recursos": "Texto impreso del estudio de caso (1.5 páginas), ficha de análisis con tabla, preguntas de comprensión.",
            "evaluacion": "Formativa — revisión de tabla de análisis y calidad de respuestas de comprensión.",
        },
        # Class 3: Writing a CV in English
        {
            "title": "Building Your Professional CV in English",
            "oa": "OA2 · OA4",
            "bloom": f"Producir un currículum vitae en inglés adaptado al perfil profesional de {n}, aplicando formato estándar y vocabulario técnico apropiado.",
            "inicio": f"""<ul>
                <li>Docente muestra 2 CVs reales (adaptados): uno bien hecho y uno con errores. <em>\"Which CV would you hire? Why?\"</em></li>
                <li>Se identifican las secciones de un CV: Personal Information, Objective, Education, Work Experience, Skills, Languages, References.</li>
                <li>Vocabulario clave: <em>objective, proficient, experienced in, certified, reference, internship, vocational training</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Model analysis (15 min):</b> Los estudiantes analizan un CV modelo de un técnico de {n.lower()} en inglés. Identifican: secciones, verbos de acción (<em>operated, maintained, installed, designed, programmed</em>), y vocabulario técnico.</li>
                <li><b>CV writing workshop (35 min):</b> Cada estudiante redacta su propio CV usando una plantilla guiada:
                    <ul>
                        <li><b>Objective:</b> <em>\"To obtain a position as a [job title] where I can apply my skills in [area].\"</em></li>
                        <li><b>Education:</b> Liceo TP, especialidad {n}.</li>
                        <li><b>Skills:</b> Al menos 5 habilidades técnicas usando {cv_focus}.</li>
                        <li><b>Languages:</b> Spanish (native), English (basic-intermediate).</li>
                    </ul>
                </li>
                <li><b>Peer review (10 min):</b> En parejas, intercambian CVs y dan feedback usando una checklist: ¿Tiene todas las secciones? ¿Los verbos están bien usados? ¿La información es clara?</li>
            </ol>""",
            "cierre": """<ul>
                <li>3 voluntarios comparten su <em>Objective</em> con la clase.</li>
                <li>Tarea: completar y mejorar el CV para la próxima semana.</li>
            </ul>""",
            "recursos": f"CV modelo impreso de técnico en {n.lower()}, plantilla de CV en blanco, checklist de peer review, pizarra con verbos de acción.",
            "evaluacion": "Formativa — revisión del borrador de CV y calidad del peer review.",
        },
        # Class 4: Job Interview Preparation
        {
            "title": "Job Interview Skills in English",
            "oa": "OA2 · OA4",
            "bloom": f"Aplicar estrategias de comunicación oral para responder preguntas frecuentes de entrevista laboral en inglés en el contexto de {n}.",
            "inicio": f"""<ul>
                <li>Warm-up: <em>\"Have you ever had a job interview? What questions did they ask?\"</em> — Lluvia de ideas en español/inglés.</li>
                <li>Docente presenta el contexto: <em>\"Imagine you are applying for your first job in {n.lower()}. The interview is in English. What do you need to know?\"</em></li>
                <li>Se presentan las 3 fases de una entrevista: Introduction, Questions & Answers, Closing.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Common questions (15 min):</b> Docente presenta las 8 preguntas más comunes:
                    <ul>
                        <li><em>\"Tell me about yourself.\"</em></li>
                        <li><em>\"Why do you want this job?\"</em></li>
                        <li><em>\"What are your strengths/weaknesses?\"</em></li>
                        <li><em>\"{interview_qs}\"</em></li>
                    </ul>
                    Los estudiantes practican respuestas modelo usando sentence frames.
                </li>
                <li><b>Model interview (10 min):</b> Docente y un estudiante voluntario modelan una entrevista completa frente a la clase.</li>
                <li><b>Practice in pairs (25 min):</b> Rol-play: un estudiante es el entrevistador, el otro el candidato. Se turnan. Usan las preguntas de la ficha y sus CVs como referencia. El docente circula y da feedback.</li>
                <li><b>Tips & strategies (10 min):</b> Docente presenta consejos: mantener contacto visual, usar <em>\"I believe...\"</em>, no decir <em>\"I don't know\"</em> sino <em>\"I am learning about...\"</em>, agradecer al final.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Cada estudiante escribe su mejor respuesta a <em>\"Tell me about yourself\"</em> (5 líneas).</li>
                <li>Preview: <em>\"Next class, you will do a mock interview for your first grade.\"</em></li>
            </ul>""",
            "recursos": f"Ficha con preguntas de entrevista para {n.lower()}, CVs de los estudiantes (clase anterior), sentence frames, tips de entrevista.",
            "evaluacion": "Formativa — observación de práctica de rol-play y calidad de respuestas.",
        },
        # Class 5: EVALUACION — Mock Job Interview (Nota 1 S1)
        {
            "title": "EVALUACIÓN: Mock Job Interview",
            "oa": "OA2 · OA4",
            "bloom": f"Producir respuestas orales coherentes y pertinentes en una simulación de entrevista laboral en inglés para un puesto técnico en {n}.",
            "inicio": """<ul>
                <li>Docente explica la dinámica: entrevista individual de 5-6 minutos, con 4 preguntas (2 generales + 2 técnicas). Se puede usar el CV como apoyo.</li>
                <li>Se repasan los criterios de evaluación: pronunciación (4 pts), vocabulario técnico (4 pts), coherencia de respuestas (4 pts), fluidez (4 pts), presentación personal (4 pts) = 20 pts.</li>
                <li>Mientras esperan su turno, los demás practican en silencio con un compañero.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Mock interviews (55 min):</b> El docente llama a cada estudiante individualmente. Entrevista de 5-6 minutos:
                    <ul>
                        <li>Q1: <em>\"Tell me about yourself and your education.\"</em></li>
                        <li>Q2: <em>\"Why are you interested in working in {n.lower()}?\"</em></li>
                        <li>Q3-Q4: Preguntas técnicas específicas de la especialidad.</li>
                    </ul>
                </li>
                <li><b>Peer practice (while waiting):</b> Los estudiantes que esperan turno practican en parejas con preguntas adicionales de la ficha.</li>
                <li><b>Self-reflection (5 min after interview):</b> Cada estudiante completa una ficha: <em>\"I felt confident when... I struggled with... Next time I will...\"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación general (sin notas individuales): aspectos positivos y áreas de mejora del grupo.</li>
                <li><em>\"You all did great! Remember, practice makes perfect. These skills will help you in real interviews.\"</em></li>
            </ul>""",
            "recursos": f"Rúbrica de evaluación (5 criterios × 4 pts = 20), CVs de los estudiantes, ficha de autorreflexión, ficha de práctica entre pares.",
            "evaluacion": "<b>SUMATIVA — Nota 1 Semestre 1:</b> Mock Job Interview. Rúbrica de 5 criterios × 4 puntos = 20 pts. Exigencia 60%.",
            "sugerencia": "<b>Consideración:</b> Para estudiantes con alta ansiedad, permitir que graben su entrevista en video como alternativa. Mantener los mismos criterios."
        },
        # Class 6: Workplace Communication
        {
            "title": "Workplace Communication: Emails & Messages",
            "oa": "OA2 · OA4",
            "bloom": f"Producir correos electrónicos y mensajes formales en inglés aplicables al contexto laboral de {n}, utilizando registro apropiado.",
            "inicio": """<ul>
                <li>Docente muestra 2 emails: uno formal correcto y uno informal/inapropiado para el trabajo. <em>\"Which one is professional? Why?\"</em></li>
                <li>Se introduce vocabulario de comunicación formal: <em>Dear, I am writing to, Please find attached, Kind regards, I would like to request</em>.</li>
                <li>Se comparan registros: formal vs informal (<em>Dear Sir → Hey, I would like → I want, Kind regards → Bye</em>).</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Email structure (15 min):</b> Análisis de la estructura: Subject line, Greeting, Opening, Body, Closing, Signature. Los estudiantes etiquetan cada parte en un email modelo.</li>
                <li><b>Guided writing (20 min):</b> Los estudiantes escriben 2 emails usando plantillas:
                    <ul>
                        <li>Email 1: Solicitar información sobre una vacante laboral en {n.lower()}.</li>
                        <li>Email 2: Confirmar asistencia a una entrevista de trabajo.</li>
                    </ul>
                </li>
                <li><b>WhatsApp/Teams messages (10 min):</b> Práctica de mensajes semi-formales para el trabajo: reportar un problema, pedir un día libre, confirmar una reunión.</li>
                <li><b>Peer review (15 min):</b> Intercambian emails y revisan con checklist: ¿Tiene saludo formal? ¿El propósito es claro? ¿El cierre es apropiado?</li>
            </ol>""",
            "cierre": """<ul>
                <li>2-3 estudiantes leen su mejor email en voz alta.</li>
                <li>Resumen: <em>\"Professional communication in English can open doors. Always check your spelling and tone.\"</em></li>
            </ul>""",
            "recursos": "Emails modelo impresos (formal e informal), plantilla de email, ficha de mensajes, checklist de peer review.",
            "evaluacion": "Formativa — revisión de emails y calidad del peer review.",
        },
        # Class 7: Video Comprehension - Workplace Scenarios
        {
            "title": "Video: Workplace Scenarios & Professional Communication",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender y evaluar críticamente escenarios laborales presentados en un video en inglés sobre el campo de {n}.",
            "inicio": f"""<ul>
                <li>Warm-up: <em>\"What does a typical workday look like for a professional in {n.lower()}?\"</em> — 3 estudiantes comparten.</li>
                <li>Pre-viewing: se entregan 5 preguntas guía y vocabulario clave del video.</li>
                <li>Predicción: a partir del título del video, <em>\"What do you think we will see?\"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Video viewing (15 min):</b> {video_topic}. Primera reproducción completa; segunda con pausas para preguntas.</li>
                <li><b>Comprehension tasks (15 min):</b> Responder preguntas guía. Trabajo individual, luego comparación en parejas.</li>
                <li><b>Critical analysis (20 min):</b> En grupos de 3, discutir:
                    <ul>
                        <li><em>\"What impressed you most about the workplace shown?\"</em></li>
                        <li><em>\"Would you like to work in that environment? Why or why not?\"</em></li>
                        <li><em>\"What skills from the video do you already have? Which ones do you need to develop?\"</em></li>
                    </ul>
                    Cada grupo prepara una mini-presentación oral (1 min).
                </li>
                <li><b>Group presentations (10 min):</b> 3-4 grupos presentan sus conclusiones.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Resumen colectivo: <em>\"What is the most important skill for the workplace?\"</em> — votación.</li>
                <li>Vocabulario nuevo del video registrado en cuadernos.</li>
            </ul>""",
            "recursos": f"Video sobre contexto laboral en {n.lower()} (YouTube, 5 min adaptado), preguntas guía impresas, pizarra.",
            "evaluacion": "Formativa — calidad de análisis crítico y participación en presentaciones grupales.",
        },
        # Class 8: Workplace Safety in English
        {
            "title": "Workplace Safety Communication in English",
            "oa": "OA1 · OA4",
            "bloom": f"Comprender y producir instrucciones de seguridad laboral en inglés específicas para el contexto de {n}.",
            "inicio": f"""<ul>
                <li>Docente muestra señales de seguridad en inglés (Warning, Danger, Caution, Emergency Exit) y pregunta: <em>\"Where have you seen these signs? What do they mean?\"</em></li>
                <li>Vocabulario de seguridad: <em>safety goggles, hard hat, fire extinguisher, first aid kit, hazard, emergency, prohibited, mandatory</em>.</li>
                <li>Se introduce el concepto de <em>Safety Data Sheets (SDS)</em> y <em>Standard Operating Procedures (SOPs)</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading safety protocols (20 min):</b> Texto adaptado: procedimientos de seguridad específicos para {n.lower()}: {safety_vocab}. Los estudiantes leen e identifican: hazards, required PPE, emergency procedures.</li>
                <li><b>Creating safety instructions (20 min):</b> En parejas, los estudiantes redactan 5 instrucciones de seguridad en inglés para su taller/laboratorio usando imperativos: <em>\"Always wear...\", \"Never touch...\", \"In case of emergency...\"</em></li>
                <li><b>Safety scenario role-play (15 min):</b> Cada pareja actúa un escenario: explicar un procedimiento de seguridad a un colega nuevo que solo habla inglés.</li>
                <li><b>Sharing (5 min):</b> Mejores instrucciones se comparten con la clase.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Quiz rápido: 5 preguntas de seguridad en inglés (oral, grupal).</li>
                <li><em>\"Safety is universal. Knowing safety vocabulary in English can save lives.\"</em></li>
            </ul>""",
            "recursos": f"Señales de seguridad impresas, texto de protocolos de seguridad para {n.lower()}, fichas para redacción, tarjetas de escenarios.",
            "evaluacion": "Formativa — calidad de instrucciones escritas y participación en role-play.",
        },
        # Class 9: Unit 1 Closure & Review
        {
            "title": "Unit 1 Review & Closure",
            "oa": "OA1 · OA2 · OA3 · OA4",
            "bloom": f"Sintetizar los aprendizajes de vocabulario profesional, comunicación laboral y entrevista en inglés adquiridos en la Unidad 1 de {n}.",
            "inicio": """<ul>
                <li>Devolución de rúbricas de la entrevista (Nota 1) con retroalimentación individual.</li>
                <li>Actividad: <em>\"Unit 1 Bingo\"</em> — cartones con vocabulario y conceptos de la unidad. Los estudiantes marcan cuando el docente da definiciones en inglés.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Review game (20 min):</b> <em>\"Career Jeopardy\"</em> — Categorías: Vocabulary, CV Writing, Interview Skills, Workplace Safety, Communication. Equipos compiten.</li>
                <li><b>CV final version (15 min):</b> Los estudiantes finalizan sus CVs incorporando feedback del docente y compañeros.</li>
                <li><b>Reflection writing (15 min):</b> Párrafo en inglés: <em>\"In Unit 1, I learned... The most useful skill was... I feel more confident about... I still need to practice...\"</em></li>
                <li><b>Sharing (10 min):</b> Voluntarios leen reflexiones. Se celebran los logros.</li>
            </ol>""",
            "cierre": f"""<ul>
                <li>Preview Unidad 2: <em>\"Next unit, we will deepen our reading skills with advanced technical texts and prepare for real workplace challenges in {n.lower()}.\"</em></li>
                <li>Docente recoge CVs finales (portafolio).</li>
            </ul>""",
            "recursos": "Bingo cards, Jeopardy en PPT/pizarra, CVs de estudiantes, ficha de reflexión.",
            "evaluacion": "Formativa — participación en juego de revisión, CV final y reflexión escrita.",
        },
    ]
    return classes


# ================= UNIT 2: Advanced Technical Reading & Critical Thinking =================

def u2_classes(sp):
    """Unit 2: Advanced Technical Reading & Critical Thinking — 7 classes, May-June"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        case1 = "Case Study: <em>The Rise of Electric Vehicles in Chile</em> — How the transition from combustion engines to EVs is affecting automotive workshops: new skills needed, training programs, infrastructure changes. Data from Chile and Latin America."
        case2 = "Case Study: <em>When Diagnostics Fail</em> — A dealership faces a recurring problem: cars returned multiple times for the same issue. The root cause? Technicians relying too much on computer diagnostics and not enough on manual inspection. Students analyze the problem and propose solutions."
        global_topic = "the impact of electric vehicles on the automotive industry worldwide and in Chile"
        debate_topic = "Should Chile invest more in EV infrastructure or in training mechanics for traditional vehicles?"
        reading_eval = "a text about autonomous vehicle technology and its implications for automotive technicians (1.5 pages, adapted A2-B1)"
    elif sp == "electricidad":
        case1 = "Case Study: <em>Chile's Renewable Energy Revolution</em> — How solar and wind energy are transforming the electrical sector: new job opportunities, required certifications, challenges of integrating renewable sources into the grid."
        case2 = "Case Study: <em>The Blackout That Changed Everything</em> — A city experiences a major power outage due to poor maintenance of the distribution network. Students analyze: What went wrong? What safety protocols were ignored? How could this be prevented?"
        global_topic = "renewable energy adoption and its impact on electrical workers in developing countries"
        debate_topic = "Should Chile prioritize solar energy or wind energy for its future electrical grid?"
        reading_eval = "a text about smart grid technology and the role of electricians in modern energy systems (1.5 pages, adapted A2-B1)"
    elif sp == "electronica":
        case1 = "Case Study: <em>E-Waste: A Global Crisis</em> — The growing problem of electronic waste: where old devices end up, environmental impact, recycling challenges, and the role of electronics technicians in sustainable disposal and repair."
        case2 = "Case Study: <em>The IoT Security Breach</em> — A hospital's IoT medical devices are hacked, compromising patient data. Students analyze: What were the vulnerabilities? What security measures should have been in place? What is the technician's role in cybersecurity?"
        global_topic = "electronic waste management and the circular economy in the tech industry"
        debate_topic = "Should manufacturers be required to make electronic devices easier to repair (Right to Repair)?"
        reading_eval = "a text about artificial intelligence in electronics manufacturing and quality control (1.5 pages, adapted A2-B1)"
    elif sp == "grafica":
        case1 = "Case Study: <em>Sustainable Printing: The Green Revolution</em> — How the printing industry is adapting to environmental demands: soy-based inks, recycled substrates, energy-efficient presses, reducing waste in production runs."
        case2 = "Case Study: <em>The Packaging Error That Cost Millions</em> — A graphic production company delivers 500,000 food packaging units with a color error. Students analyze: What went wrong in the prepress process? What quality control steps were missed? How to prevent this?"
        global_topic = "the future of print media in a digital world and sustainable printing practices"
        debate_topic = "Is print media dying, or will it evolve and survive alongside digital media?"
        reading_eval = "a text about 3D printing technology and its applications in graphic production and packaging (1.5 pages, adapted A2-B1)"
    else:  # industrial
        case1 = "Case Study: <em>Industry 4.0 in Latin America</em> — How automation, robotics, and AI are transforming manufacturing in Chile and the region: new skills needed, job displacement concerns, opportunities for CNC-trained technicians."
        case2 = "Case Study: <em>The Machine That Stopped Production</em> — A factory loses 3 days of production because a critical CNC machine fails and no one on-site can diagnose the problem (the manual is in English). Students analyze: What preventive maintenance was missed? How could English skills have helped?"
        global_topic = "the impact of automation and Industry 4.0 on industrial workers in developing countries"
        debate_topic = "Will robots replace industrial mechanics, or will they create new and better jobs?"
        reading_eval = "a text about predictive maintenance using AI and sensors in modern factories (1.5 pages, adapted A2-B1)"

    classes = [
        # Class 1(10): Advanced Case Study 1
        {
            "title": "Case Study: Industry Trends & Challenges",
            "oa": "OA1 · OA3",
            "bloom": f"Analizar críticamente un estudio de caso sobre tendencias globales que afectan al campo de {n}, extrayendo información relevante y formando una postura personal.",
            "inicio": f"""<ul>
                <li>Warm-up: <em>\"What is the biggest change happening in {n.lower()} right now?\"</em> — brainstorm en la pizarra.</li>
                <li>Pre-reading: docente presenta 3 datos/estadísticas sobre la tendencia global y pregunta: <em>\"What do these numbers tell us?\"</em></li>
                <li>Vocabulario clave: <em>trend, impact, challenge, opportunity, transition, sustainability, workforce, infrastructure</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {case1} Texto adaptado A2-B1 (1.5 páginas).
                    <ul>
                        <li>Primera lectura: scanning para ideas principales.</li>
                        <li>Segunda lectura: completar tabla de análisis: <b>Trend → Impact on workers → Opportunities → Challenges → My opinion</b></li>
                    </ul>
                </li>
                <li><b>Comprehension (10 min):</b> 6 preguntas: 3 de información explícita + 3 de análisis (<em>\"What does this mean for your career?\"</em>).</li>
                <li><b>Critical discussion (20 min):</b> En grupos de 3-4, debatir: <em>\"How will this trend affect YOUR future job? Is this a threat or an opportunity?\"</em> Cada grupo prepara una postura (2-3 argumentos).</li>
                <li><b>Group sharing (5 min):</b> Un representante de cada grupo comparte la postura.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Ticket de salida: <em>\"In my opinion, this trend is [positive/negative/both] because...\"</em> (3 líneas).</li>
                <li>Preview: <em>\"Next class, we will analyze a real workplace problem through another case study.\"</em></li>
            </ul>""",
            "recursos": f"Texto impreso del estudio de caso (1.5 páginas), ficha de análisis con tabla, preguntas de comprensión, pizarra.",
            "evaluacion": "Formativa — calidad de análisis en tabla y participación en discusión crítica.",
        },
        # Class 2(11): Case Study 2 - Workplace Problem
        {
            "title": "Case Study: Analyzing a Workplace Problem",
            "oa": "OA1 · OA3",
            "bloom": f"Evaluar un problema laboral presentado en un estudio de caso de {n}, proponiendo soluciones fundamentadas en inglés.",
            "inicio": """<ul>
                <li>Warm-up: <em>\"Think of a problem you have seen or heard about in a workshop/workplace. What happened?\"</em> — 3 estudiantes comparten.</li>
                <li>Se introduce vocabulario de resolución de problemas: <em>root cause, analysis, solution, prevention, protocol, inspection, negligence, accountability</em>.</li>
                <li>Pre-reading: <em>\"Read only the title. What do you think happened?\"</em> — predicciones.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {case2} Texto adaptado A2-B1 (1 página). Lectura guiada.
                    <ul>
                        <li>Los estudiantes completan un diagrama de análisis: <b>Problem → Cause → Consequences → Solution → Prevention</b></li>
                    </ul>
                </li>
                <li><b>Group analysis (20 min):</b> En grupos de 3: <em>\"What went wrong? Who was responsible? What should they have done differently?\"</em> Cada grupo propone 3 acciones correctivas en inglés.</li>
                <li><b>Presentations (10 min):</b> Cada grupo presenta su análisis y propuestas (2 min).</li>
                <li><b>Class vote (5 min):</b> <em>\"Which group had the best solution?\"</em> — justificar la votación.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Reflexión: <em>\"What did this case teach you about professional responsibility?\"</em></li>
                <li>Se conectan las lecciones con el contexto laboral real de los estudiantes.</li>
            </ul>""",
            "recursos": "Texto impreso del estudio de caso, diagrama de análisis (Problem-Cause-Solution), tarjetas para propuestas.",
            "evaluacion": "Formativa — calidad del diagrama de análisis y de las propuestas de solución.",
        },
        # Class 3(12): Debate preparation
        {
            "title": "Preparing for a Structured Debate",
            "oa": "OA3 · OA4",
            "bloom": f"Construir argumentos fundamentados en inglés para defender una postura sobre un tema controversial en {n}.",
            "inicio": f"""<ul>
                <li>Docente presenta el tema del debate: <em>\"{debate_topic}\"</em></li>
                <li>Quick poll: ¿A favor o en contra? Los estudiantes se posicionan físicamente en el aula.</li>
                <li>Se introduce vocabulario de debate: <em>I believe, In my opinion, The evidence shows, On the other hand, However, Furthermore, In conclusion</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Argument building (25 min):</b> Los estudiantes se dividen en 2 grupos (a favor y en contra). Cada grupo:
                    <ul>
                        <li>Lee un texto corto con datos que apoyan su postura.</li>
                        <li>Identifica 3 argumentos principales.</li>
                        <li>Prepara evidencia de los textos leídos en la unidad.</li>
                        <li>Redacta un <em>opening statement</em> (2-3 oraciones).</li>
                    </ul>
                </li>
                <li><b>Counter-arguments (15 min):</b> Cada grupo anticipa 2 argumentos del otro lado y prepara respuestas.</li>
                <li><b>Practice round (15 min):</b> Mini-debate de práctica dentro de cada grupo para refinar argumentos y practicar pronunciación.</li>
                <li><b>Strategy (5 min):</b> Cada grupo elige: un orador de apertura, 2-3 oradores de argumentos, un orador de cierre.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Cada grupo lee su <em>opening statement</em> como preview.</li>
                <li><em>\"Next class, the debate! Be ready to defend your position.\"</em></li>
            </ul>""",
            "recursos": "Textos de apoyo con datos y estadísticas, ficha de argumentación, vocabulary de debate, pizarra.",
            "evaluacion": "Formativa — calidad de argumentos preparados y coherencia del opening statement.",
        },
        # Class 4(13): Debate + Evaluation intro
        {
            "title": "Structured Debate & Critical Thinking",
            "oa": "OA3 · OA4",
            "bloom": f"Defender una postura personal de manera crítica y fundamentada en un debate estructurado en inglés sobre un tema de {n}.",
            "inicio": f"""<ul>
                <li>Docente organiza el aula para el debate: dos grupos frente a frente, moderador (docente).</li>
                <li>Se repasan las reglas: respetar turnos, usar inglés, no interrumpir, usar evidencia para argumentar.</li>
                <li>Vocabulario de debate visible en la pizarra como apoyo.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Debate (40 min):</b> Estructura:
                    <ul>
                        <li>Opening statements (2 min cada grupo).</li>
                        <li>Argument round 1 (3 argumentos por lado, 2 min cada uno).</li>
                        <li>Rebuttal round (cada grupo responde al otro, 5 min).</li>
                        <li>Open floor (preguntas y respuestas libres, 10 min).</li>
                        <li>Closing statements (2 min cada grupo).</li>
                    </ul>
                </li>
                <li><b>Audience evaluation (10 min):</b> Los compañeros evalúan con ficha: mejor argumento, mejor orador, argumento más débil.</li>
                <li><b>Exam preparation (10 min):</b> Docente introduce la evaluación de lectura de la próxima clase: formato, tipo de texto, estrategias de lectura recomendadas.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Reflexión grupal: <em>\"What did you learn from hearing the other side's arguments?\"</em></li>
                <li>Recordatorio de la evaluación de lectura de la próxima clase.</li>
            </ul>""",
            "recursos": "Disposición de aula para debate, vocabulario de debate en pizarra, ficha de evaluación de pares, timer.",
            "evaluacion": "Formativa — participación en debate, calidad de argumentos y uso de inglés.",
        },
        # Class 5(14): EVALUACION — Reading Comprehension (Nota 2 S1)
        {
            "title": "EVALUACIÓN: Reading Comprehension Test",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender y analizar un texto técnico en inglés sobre {n.lower()}, respondiendo preguntas de comprensión explícita, inferencial y crítica.",
            "inicio": """<ul>
                <li>Docente repasa estrategias de lectura: scanning, skimming, inference, identifying purpose.</li>
                <li>Se distribuye la prueba y se explica el formato: Sección A (vocabulario, 8 pts), Sección B (comprensión explícita, 10 pts), Sección C (inferencia y opinión, 12 pts).</li>
                <li>Tiempo: 70 minutos para completar la prueba.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Evaluación escrita (70 min):</b> Los estudiantes leen {reading_eval} y responden:
                    <ul>
                        <li><b>Sección A — Vocabulario (8 pts):</b> Matching: 8 palabras técnicas con sus definiciones.</li>
                        <li><b>Sección B — Comprensión explícita (10 pts):</b> 5 preguntas de información directa del texto (2 pts c/u).</li>
                        <li><b>Sección C — Inferencia y opinión (12 pts):</b> 3 preguntas de inferencia (2 pts c/u) + 2 preguntas de opinión fundamentada (3 pts c/u).</li>
                    </ul>
                    Total: 30 puntos.
                </li>
            </ol>""",
            "cierre": """<ul>
                <li>Los estudiantes entregan la prueba.</li>
                <li>Breve conversación: <em>\"How did you feel? Which part was most difficult?\"</em></li>
                <li>Preview: <em>\"Next class, we will do our semester integration evaluation.\"</em></li>
            </ul>""",
            "recursos": "Prueba impresa (texto de lectura + preguntas), hoja de respuestas.",
            "evaluacion": "<b>SUMATIVA — Nota 2 Semestre 1:</b> Prueba de comprensión lectora. 30 pts (8 vocabulario + 10 explícita + 12 inferencia/opinión). Exigencia 60%.",
        },
        # Class 6(15): Integrated Semester Evaluation (Nota 3 S1)
        {
            "title": "EVALUACIÓN: Integrated Semester Assessment",
            "oa": "OA1 · OA2 · OA3 · OA4",
            "bloom": f"Integrar habilidades de comprensión lectora, expresión oral y pensamiento crítico desarrolladas durante el semestre en {n}.",
            "inicio": """<ul>
                <li>Docente explica el formato: Parte 1 — lectura y respuestas escritas (20 min), Parte 2 — actividad oral en parejas (15 min), Parte 3 — reflexión crítica escrita (15 min).</li>
                <li>Se repasan criterios de evaluación: comprensión (15 pts), producción oral (15 pts), pensamiento crítico (15 pts) = 45 pts.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Parte 1 — Reading & Writing (20 min):</b> Texto nuevo breve sobre un tema integrador de {n.lower()}. 5 preguntas de comprensión + 1 pregunta de análisis. (15 pts)</li>
                <li><b>Parte 2 — Oral activity (20 min):</b> En parejas, los estudiantes reciben un escenario laboral y deben:
                    <ul>
                        <li>Describir el problema en inglés.</li>
                        <li>Proponer una solución.</li>
                        <li>Responder 2 preguntas del docente.</li>
                    </ul>
                    (15 pts por estudiante)
                </li>
                <li><b>Parte 3 — Critical reflection (15 min):</b> Escribir un párrafo de opinión: <em>\"How has English helped me understand my profession better this semester? Give specific examples.\"</em> (15 pts)</li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación general del semestre: logros, áreas de mejora.</li>
                <li><em>\"Excellent work this semester! Enjoy your winter break. We will continue with technical communication in Semester 2.\"</em></li>
            </ul>""",
            "recursos": "Prueba integrada (texto + preguntas + escenarios orales + ficha de reflexión), rúbrica oral.",
            "evaluacion": "<b>SUMATIVA — Nota 3 Semestre 1:</b> Evaluación integradora. 45 pts (15 lectura + 15 oral + 15 reflexión crítica). Exigencia 60%.",
            "sugerencia": "<b>Consideración:</b> Para la parte oral, si hay muchos estudiantes, programar parejas con tiempos definidos. Alternativa: grabación de audio."
        },
        # Class 7(16): Semester 1 Closure
        {
            "title": "Semester 1 Review & Closure",
            "oa": "OA1 · OA3 · OA4",
            "bloom": f"Sintetizar y reflexionar sobre los aprendizajes del primer semestre de inglés técnico en {n}.",
            "inicio": """<ul>
                <li>Devolución de notas del semestre con rúbricas y retroalimentación.</li>
                <li><em>\"What is your proudest achievement this semester?\"</em> — round robin rápido.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Semester review game (20 min):</b> <em>\"The Big Semester Quiz\"</em> — equipos compiten con preguntas de vocabulario, lectura, entrevista, seguridad, comunicación laboral.</li>
                <li><b>Portfolio review (15 min):</b> Los estudiantes revisan su CV, trabajos escritos y fichas del semestre. Seleccionan su mejor trabajo y escriben por qué lo eligieron.</li>
                <li><b>Goal setting (15 min):</b> Cada estudiante escribe 3 metas para el Semestre 2: <em>\"I want to improve my... I will practice... I want to learn about...\"</em></li>
                <li><b>Sharing (10 min):</b> Voluntarios comparten sus metas. Aplausos del grupo.</li>
            </ol>""",
            "cierre": f"""<ul>
                <li>Preview Semestre 2: <em>\"After the break, we will focus on advanced technical texts, real-world projects, and your final presentation — your 'Thesis Defense' in English!\"</em></li>
                <li>Despedida y buenos deseos para las vacaciones de invierno.</li>
            </ul>""",
            "recursos": "Quiz semestral en PPT/pizarra, portafolios de estudiantes, ficha de metas, rúbricas con notas.",
            "evaluacion": "Formativa — participación en revisión, reflexión de portafolio y escritura de metas.",
        },
    ]
    return classes


# ================= UNIT 3: Technical Documentation & Procedures =================

def u3_classes(sp):
    """Unit 3: Technical Documentation & Procedures — 9 classes, July-September"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        tech_doc = "a vehicle service manual excerpt: <em>Brake Pad Replacement Procedure</em> — step-by-step instructions with diagrams for replacing front brake pads on a sedan. Includes safety precautions, required tools, and torque specifications."
        procedure = "brake pad replacement: jack up vehicle, remove wheel, remove caliper, remove old pads, install new pads, reassemble, test brakes"
        report_topic = "a diagnostic report for a vehicle with intermittent electrical problems"
        manual_text = "an owner's manual section about the vehicle's onboard diagnostic (OBD) system and warning lights"
        case_comm = "Case Study: <em>Lost in Translation</em> — A Chilean technician at an international repair chain misunderstands maintenance instructions written in English, leading to a customer complaint. Analysis of what went wrong and how to prevent miscommunication."
        video_proc = "a YouTube video showing a professional mechanic performing a complete vehicle inspection, narrating each step in English (adapted, 6 min)"
    elif sp == "electricidad":
        tech_doc = "an electrical installation manual excerpt: <em>Three-Phase Motor Connection Procedure</em> — step-by-step instructions with wiring diagrams for connecting a three-phase motor to a power supply. Includes safety protocols and testing procedures."
        procedure = "three-phase motor connection: verify power is off (lockout/tagout), identify wiring, connect leads, ground the motor, test rotation, verify current draw"
        report_topic = "an inspection report for a commercial building's electrical panel"
        manual_text = "a technical manual section about circuit breaker selection and sizing for residential installations"
        case_comm = "Case Study: <em>The Miswired Panel</em> — An electrician misreads an English-language wiring diagram, causing a short circuit during testing. Students analyze the communication breakdown and propose protocols for working with technical documents in English."
        video_proc = "a YouTube video showing a professional electrician installing a residential electrical panel, explaining safety procedures in English (adapted, 6 min)"
    elif sp == "electronica":
        tech_doc = "a component datasheet: <em>Arduino Uno Microcontroller Technical Specifications</em> — pin configuration, operating voltage, memory specifications, and application notes for connecting sensors and actuators."
        procedure = "sensor integration project: select sensor, connect to Arduino pins, upload firmware, calibrate sensor, test output, document results"
        report_topic = "a technical report on testing and calibrating a temperature monitoring system"
        manual_text = "a user manual section for an oscilloscope: setting up channels, adjusting timebase, measuring voltage and frequency"
        case_comm = "Case Study: <em>The Datasheet Disaster</em> — An electronics technician connects a component incorrectly because they misread the English datasheet, damaging the PCB. Students analyze what information was misunderstood and how to read datasheets effectively."
        video_proc = "a YouTube video about assembling and programming an Arduino-based IoT sensor project, explained step-by-step in English (adapted, 6 min)"
    elif sp == "grafica":
        tech_doc = "a printing press operation manual: <em>Offset Press Setup Procedure</em> — step-by-step instructions for preparing an offset press: loading plates, mixing inks, setting registration marks, paper feed adjustment."
        procedure = "offset press setup: clean previous job residue, mount plates, load paper, adjust ink feeds, set registration, run test prints, verify color"
        report_topic = "a quality control report for a packaging print run showing color deviations"
        manual_text = "a software manual section for prepress color management: ICC profiles, color proofing, and PDF/X export settings"
        case_comm = "Case Study: <em>The Color Catastrophe</em> — A graphic technician exports files with wrong color profiles because the software manual was in English. The entire print run has shifted colors. Students analyze the error and create a bilingual checklist."
        video_proc = "a YouTube video showing the complete workflow of a modern packaging production facility, from design to print (adapted, 6 min)"
    else:  # industrial
        tech_doc = "a CNC machine operation manual: <em>G-Code Programming Basics for CNC Lathe</em> — common G-codes and M-codes, coordinate systems, programming a simple turning operation, safety interlocks."
        procedure = "CNC lathe setup: power on sequence, home machine axes, load program, mount workpiece in chuck, set tool offsets, run simulation, execute program"
        report_topic = "a production report showing tolerances and quality measurements for a batch of machined parts"
        manual_text = "a hydraulic system maintenance manual: fluid levels, filter replacement, pressure testing, and troubleshooting common faults"
        case_comm = "Case Study: <em>The G-Code Mistake</em> — A CNC operator enters incorrect values from an English-language program sheet, resulting in a batch of defective parts. Students analyze the miscommunication and propose verification protocols."
        video_proc = "a YouTube video showing a CNC machinist programming and operating a lathe, explaining the process in English (adapted, 6 min)"

    classes = [
        # Class 1(17): Reading Technical Documentation
        {
            "title": "Reading Technical Manuals & Documentation",
            "oa": "OA1",
            "bloom": f"Comprender información técnica específica en un documento profesional en inglés del área de {n}, identificando pasos, precauciones y especificaciones.",
            "inicio": f"""<ul>
                <li>Docente da la bienvenida al Semestre 2: <em>\"Welcome back! This semester, we focus on reading real technical documents, writing reports, and your final project.\"</em></li>
                <li>Pregunta: <em>\"Have you ever had to read a manual or instruction in English? What was it?\"</em></li>
                <li>Se presentan tipos de documentos técnicos: manuals, datasheets, SOPs, reports, specifications.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {tech_doc} Texto adaptado A2-B1 (1.5 páginas con diagramas).
                    <ul>
                        <li>Pre-reading: identificar secciones visuales (título, pasos numerados, advertencias, diagramas).</li>
                        <li>Lectura guiada: el docente modela cómo leer un documento técnico (no lineal: primero precauciones, luego materiales, luego pasos).</li>
                        <li>Los estudiantes completan: <b>Step → Action → Tool/Material → Safety Note</b></li>
                    </ul>
                </li>
                <li><b>Comprehension (15 min):</b> 8 preguntas: vocabulario técnico (4) + comprensión de pasos (4).</li>
                <li><b>Transfer activity (15 min):</b> En parejas, los estudiantes explican oralmente el procedimiento a su compañero usando sus propias palabras en inglés.</li>
                <li><b>Wrap-up (5 min):</b> Discusión: <em>\"Why is it important to read these documents carefully?\"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Vocabulario nuevo registrado en cuadernos (mínimo 10 palabras).</li>
                <li>Preview: <em>\"Next class, you will practice following and giving technical instructions in English.\"</em></li>
            </ul>""",
            "recursos": f"Documento técnico impreso de {n.lower()} con diagramas, ficha de análisis (tabla Step-Action-Tool-Safety), preguntas de comprensión.",
            "evaluacion": "Formativa — calidad de la tabla de análisis y capacidad de explicar el procedimiento oralmente.",
        },
        # Class 2(18): Following & Giving Technical Instructions
        {
            "title": "Following & Giving Technical Instructions",
            "oa": "OA1 · OA4",
            "bloom": f"Producir instrucciones técnicas claras en inglés para un procedimiento específico de {n}, utilizando secuenciadores e imperativos.",
            "inicio": """<ul>
                <li>Warm-up: <em>\"Simon Says\"</em> con instrucciones técnicas simples para activar memoria cinestésica.</li>
                <li>Repaso de secuenciadores: <em>First, Next, Then, After that, Finally</em> + imperativos: <em>Connect, Remove, Check, Tighten, Verify</em>.</li>
                <li>Se muestra un ejemplo de instrucciones mal escritas y se pide mejorarlas.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Model procedure (10 min):</b> Docente presenta un procedimiento modelo con pasos claros: {procedure}. Los estudiantes identifican secuenciadores y verbos imperativos.</li>
                <li><b>Writing instructions (25 min):</b> Cada estudiante escribe un procedimiento de 8-10 pasos para una tarea técnica de su especialidad. Deben incluir:
                    <ul>
                        <li>Title</li>
                        <li>Materials/Tools needed</li>
                        <li>Safety precautions</li>
                        <li>Numbered steps with clear imperatives</li>
                    </ul>
                </li>
                <li><b>Peer testing (20 min):</b> En parejas, un estudiante lee las instrucciones del otro y simula seguirlas (o las sigue con dibujos). ¿Se entienden? ¿Falta algún paso?</li>
                <li><b>Revision (5 min):</b> Los estudiantes mejoran sus instrucciones según el feedback.</li>
            </ol>""",
            "cierre": """<ul>
                <li>2-3 estudiantes leen sus instrucciones en voz alta.</li>
                <li>Reflexión: <em>\"Were the instructions easy to follow? What made them clear or confusing?\"</em></li>
            </ul>""",
            "recursos": "Modelo de instrucciones técnicas impreso, plantilla de procedimiento, fichas de peer review.",
            "evaluacion": "Formativa — calidad de las instrucciones escritas y feedback del peer testing.",
        },
        # Class 3(19): Video Comprehension - Technical Procedure
        {
            "title": "Video: Understanding Technical Procedures",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender y evaluar un procedimiento técnico presentado en un video en inglés sobre {n}, comparándolo con la práctica local.",
            "inicio": f"""<ul>
                <li>Pre-viewing: <em>\"Today we will watch a professional demonstration. What procedures have you seen in your workshop classes?\"</em></li>
                <li>Se entregan preguntas guía y vocabulario clave del video.</li>
                <li>Predicción: <em>\"Based on the title, what steps do you think we will see?\"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Video viewing (15 min):</b> {video_proc} Primera reproducción completa; segunda con pausas para preguntas de comprensión.</li>
                <li><b>Comprehension tasks (15 min):</b>
                    <ul>
                        <li>Ordenar los pasos del procedimiento (sequence ordering).</li>
                        <li>Responder 6 preguntas de comprensión.</li>
                        <li>Identificar vocabulario nuevo del video.</li>
                    </ul>
                </li>
                <li><b>Comparative analysis (20 min):</b> En grupos de 3: <em>\"How does this procedure compare to what you do in your workshop? What is similar? What is different? What can we learn?\"</em>. Completar tabla comparativa: <b>Video procedure vs Our workshop procedure</b></li>
                <li><b>Group sharing (10 min):</b> Cada grupo comparte 2 diferencias interesantes.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Resumen: <em>\"Professional videos in English are great learning resources. Use YouTube to keep learning after school.\"</em></li>
                <li>Vocabulario nuevo registrado.</li>
            </ul>""",
            "recursos": f"Video técnico de {n.lower()} (YouTube, 6 min adaptado), preguntas guía, ficha de comparación.",
            "evaluacion": "Formativa — calidad de respuestas de comprensión y análisis comparativo.",
        },
        # Class 4(20): Technical Report Writing
        {
            "title": "Writing Technical Reports in English",
            "oa": "OA2 · OA4",
            "bloom": f"Producir un informe técnico breve en inglés siguiendo una estructura estándar aplicada al contexto de {n}.",
            "inicio": f"""<ul>
                <li>Docente muestra un ejemplo de reporte técnico real (adaptado): <em>\"This is how professionals communicate results in English.\"</em></li>
                <li>Se identifican las secciones: Title, Date, Author, Purpose, Procedure, Findings, Conclusion, Recommendations.</li>
                <li>Vocabulario: <em>findings, recommendations, compliance, deviation, within tolerance, out of spec, corrective action</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Model analysis (15 min):</b> Análisis guiado de {report_topic}. Los estudiantes identifican cada sección y su propósito.</li>
                <li><b>Guided report writing (30 min):</b> Cada estudiante redacta un reporte técnico breve basado en un escenario dado:
                    <ul>
                        <li><b>Scenario:</b> Usar un problema técnico ficticio pero realista de {n.lower()}.</li>
                        <li>Deben incluir todas las secciones del reporte.</li>
                        <li>Se proporciona una plantilla con sentence frames para cada sección.</li>
                    </ul>
                </li>
                <li><b>Peer review (10 min):</b> Intercambian reportes y evalúan: ¿Tiene todas las secciones? ¿Las conclusiones son lógicas? ¿Las recomendaciones son prácticas?</li>
                <li><b>Revision (5 min):</b> Incorporar feedback y mejorar el reporte.</li>
            </ol>""",
            "cierre": """<ul>
                <li>2 estudiantes leen su sección de <em>Findings and Recommendations</em>.</li>
                <li><em>\"Technical reports are essential in any professional setting. Practice writing them clearly.\"</em></li>
            </ul>""",
            "recursos": f"Reporte técnico modelo de {n.lower()}, plantilla de reporte con sentence frames, ficha de peer review.",
            "evaluacion": "Formativa — calidad del reporte técnico y del peer review.",
        },
        # Class 5(21): Reading Equipment Manuals
        {
            "title": "Reading & Interpreting Equipment Manuals",
            "oa": "OA1",
            "bloom": f"Comprender información técnica específica en un manual de equipo en inglés usado en {n}, aplicando estrategias de lectura selectiva.",
            "inicio": f"""<ul>
                <li>Warm-up: <em>\"What manuals do you use in your workshop? Are any in English?\"</em></li>
                <li>Se presenta la diferencia entre reading for detail (intensive) y reading for specific information (scanning).</li>
                <li>Vocabulario: <em>specifications, operating range, troubleshooting, warranty, compliance, rated capacity</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {manual_text} Texto adaptado con formato de manual (tablas, bullets, advertencias).
                    <ul>
                        <li>Actividad 1: Scanning — encontrar 5 datos específicos en el texto (ej: voltaje, capacidad, pasos de mantenimiento).</li>
                        <li>Actividad 2: Comprensión detallada — responder 6 preguntas sobre procedimientos descritos.</li>
                    </ul>
                </li>
                <li><b>Troubleshooting practice (20 min):</b> El manual incluye una sección de <em>Troubleshooting</em>. Los estudiantes reciben 3 escenarios de problemas y deben encontrar la solución en el manual.</li>
                <li><b>Discussion (10 min):</b> <em>\"How confident do you feel reading technical manuals in English now compared to the beginning of the year?\"</em></li>
                <li><b>Vocabulary log (5 min):</b> Registrar 8 palabras nuevas.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Quick quiz oral: docente describe un problema, los estudiantes buscan la solución en el manual.</li>
                <li>Preview: <em>\"Next class, we will analyze a case study about communication failures in the workplace.\"</em></li>
            </ul>""",
            "recursos": f"Manual técnico impreso de {n.lower()} (adaptado), ficha de scanning, escenarios de troubleshooting.",
            "evaluacion": "Formativa — precisión en scanning, calidad de respuestas y resolución de troubleshooting.",
        },
        # Class 6(22): Communication Failure Case Study
        {
            "title": "Case Study: When Communication Fails",
            "oa": "OA1 · OA3",
            "bloom": f"Evaluar críticamente un caso de falla de comunicación en inglés en el contexto laboral de {n} y proponer estrategias de prevención.",
            "inicio": """<ul>
                <li>Warm-up: <em>\"Have you ever misunderstood instructions? What happened?\"</em> — 3 estudiantes comparten.</li>
                <li>Se introduce el concepto de <em>miscommunication</em> en el trabajo y sus consecuencias.</li>
                <li>Vocabulario: <em>miscommunication, misunderstand, misread, misinterpret, protocol, verification, double-check</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {case_comm} Texto adaptado A2-B1 (1 página).
                    <ul>
                        <li>Los estudiantes completan un análisis: <b>What happened → Why → Consequences → How to prevent</b></li>
                    </ul>
                </li>
                <li><b>Group problem-solving (20 min):</b> En grupos de 3-4:
                    <ul>
                        <li>Crear una <em>\"Communication Checklist\"</em> en inglés para prevenir errores similares (5-7 items).</li>
                        <li>Ejemplo: <em>\"Always read the document twice. Highlight key numbers. Ask a colleague to verify.\"</em></li>
                    </ul>
                </li>
                <li><b>Presentation (10 min):</b> Cada grupo presenta su checklist (1 min cada uno).</li>
                <li><b>Class vote (5 min):</b> Se vota por la mejor checklist, que se adoptará como estándar de la clase.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Reflexión: <em>\"What is one thing you will always do when reading English documents in the future?\"</em></li>
                <li>Preview de la evaluación oral de la próxima clase.</li>
            </ul>""",
            "recursos": "Texto del estudio de caso impreso, ficha de análisis, cartulinas para checklists, marcadores.",
            "evaluacion": "Formativa — calidad del análisis de caso y de las checklists creadas.",
        },
        # Class 7(23): EVALUACION Oral — Explaining a Technical Procedure (Nota 1 S2)
        {
            "title": "EVALUACIÓN: Oral Explanation of a Technical Procedure",
            "oa": "OA2 · OA4",
            "bloom": f"Producir una explicación oral clara y secuencial en inglés de un procedimiento técnico específico de {n}.",
            "inicio": """<ul>
                <li>Docente explica la dinámica: cada estudiante explica un procedimiento técnico en inglés (3-4 minutos). Puede usar una ficha con palabras clave (no oraciones completas).</li>
                <li>Criterios: claridad de pasos (5 pts), vocabulario técnico (5 pts), secuenciadores (3 pts), pronunciación (4 pts), seguridad mencionada (3 pts) = 20 pts.</li>
                <li>Los estudiantes reciben su tema 5 minutos antes de presentar para preparar.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Oral evaluations (55 min):</b> Cada estudiante presenta individualmente (3-4 min):
                    <ul>
                        <li>Explicar un procedimiento técnico de {n.lower()} en inglés.</li>
                        <li>Temas asignados al azar de un banco de 8-10 procedimientos del área.</li>
                        <li>Estructura esperada: Introduction (what procedure, why), Safety precautions, Steps (using sequencers), Conclusion.</li>
                    </ul>
                </li>
                <li><b>Peer practice (while waiting):</b> Los demás practican explicando procedimientos en voz baja entre pares.</li>
                <li><b>Post-evaluation (5 min):</b> Autorreflexión: <em>\"I explained clearly when... I had difficulty with... I will practice...\"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación general (aspectos positivos y áreas de mejora del grupo).</li>
                <li><em>\"You are becoming technical communicators in English! Well done.\"</em></li>
            </ul>""",
            "recursos": f"Banco de temas de procedimientos de {n.lower()} (tarjetas), rúbrica de evaluación (5 criterios = 20 pts), fichas de autorreflexión.",
            "evaluacion": "<b>SUMATIVA — Nota 1 Semestre 2:</b> Explicación oral de procedimiento técnico. Rúbrica de 5 criterios = 20 pts. Exigencia 60%.",
            "sugerencia": "<b>Consideración:</b> Si hay muchos estudiantes, continuar en la siguiente clase. Alternativa para estudiantes con ansiedad: grabar un video explicativo."
        },
        # Class 8(25): Reading Manuals Review + Project Intro
        {
            "title": "Technical Reading Review & Final Project Introduction",
            "oa": "OA1 · OA2",
            "bloom": f"Sintetizar las estrategias de lectura técnica adquiridas y planificar el proyecto final de inglés técnico para {n}.",
            "inicio": """<ul>
                <li>Devolución de rúbricas de la evaluación oral con retroalimentación.</li>
                <li>Warm-up: <em>\"What types of technical documents in English can you now read with confidence?\"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading skills review (20 min):</b> Actividad integradora: los estudiantes reciben un texto técnico nuevo y aplican todas las estrategias aprendidas (scanning, análisis de estructura, vocabulary in context, troubleshooting).</li>
                <li><b>Project introduction (25 min):</b> <em>\"Your final project: Project Defense in English.\"</em>
                    <ul>
                        <li><b>Task:</b> Investigar un tema técnico de {n.lower()}, preparar un informe escrito (1 página) y una presentación oral de 5 minutos (tipo \"defensa de proyecto\").</li>
                        <li><b>Structure:</b> Introduction → Problem/Topic → Research → Proposed Solution/Analysis → Conclusion → Q&A.</li>
                        <li>Se entregan rúbricas y cronograma.</li>
                        <li>Se forman parejas o tríos (según tamaño del curso).</li>
                    </ul>
                </li>
                <li><b>Topic selection (10 min):</b> Los grupos eligen su tema de una lista proporcionada o proponen uno propio (aprobado por el docente).</li>
                <li><b>Timeline (5 min):</b> Clase 9 — Investigación. Clase 10 — Evaluación lectura. Clase 11 — Proyecto final.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Cada grupo anuncia su tema al curso.</li>
                <li><em>\"Start thinking about your research. This is your chance to show everything you have learned!\"</em></li>
            </ul>""",
            "recursos": f"Texto técnico nuevo de {n.lower()} para revisión, ficha del proyecto final (instrucciones, rúbrica, cronograma), lista de temas sugeridos.",
            "evaluacion": "Formativa — desempeño en lectura integradora y selección de tema del proyecto.",
        },
        # Class 9(26): Research & Project Preparation
        {
            "title": "Project Research & Preparation Workshop",
            "oa": "OA1 · OA2 · OA4",
            "bloom": f"Investigar y organizar información en inglés sobre un tema técnico de {n} para la preparación del proyecto final.",
            "inicio": """<ul>
                <li>Docente recuerda la estructura del proyecto y los criterios de evaluación.</li>
                <li><em>\"Today is your research and writing workshop. Use your time wisely!\"</em></li>
                <li>Se reparten materiales de referencia adaptados según los temas elegidos.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Research reading (25 min):</b> Los grupos leen textos adaptados sobre su tema elegido (proporcionados por el docente). Toman notas organizadas: Main ideas, Key vocabulary, Data/statistics, Opinions/analysis.</li>
                <li><b>Report writing (20 min):</b> Los grupos redactan su informe escrito (1 página) usando la plantilla: Introduction, Background, Analysis, Conclusion, Recommendations.</li>
                <li><b>Presentation preparation (10 min):</b> Crear fichas de apoyo para la presentación oral (keywords only, no complete sentences).</li>
                <li><b>Practice (5 min):</b> Ensayo rápido en el grupo: ¿Quién dice qué? ¿Cuánto tiempo toma cada parte?</li>
            </ol>""",
            "cierre": """<ul>
                <li>Check-in con cada grupo: ¿Están listos? ¿Necesitan ayuda?</li>
                <li>Recordatorio: <em>\"Next class: reading evaluation. Class after that: your project presentation!\"</em></li>
            </ul>""",
            "recursos": "Textos de referencia adaptados por tema, plantilla de informe, fichas de apoyo para presentación, rúbricas.",
            "evaluacion": "Formativa — progreso del informe escrito y preparación de la presentación.",
        },
    ]
    return classes


# ================= UNIT 4: Innovation, Project Defense & Closure =================

def u4_classes(sp):
    """Unit 4: Innovation, Project Defense & Closure — 8 classes, October-November (ends Nov 12)"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        innovation_text = "<em>The Future of Automotive Technology</em> — autonomous vehicles, hydrogen fuel cells, advanced driver assistance systems (ADAS), connected cars, and their impact on the mechanic's role. Focus on what skills will be needed in 2030."
        video_innov = "a YouTube video about Tesla's manufacturing process and how it's changing the automotive industry (adapted, 5 min)"
        case_final = "Case Study: <em>The Traditional Workshop vs. The Digital Dealership</em> — comparing two approaches to automotive repair: a small family workshop using traditional methods vs. a high-tech dealership with computer diagnostics. Students evaluate pros, cons, and the future direction of the industry."
        debate_final = "Should all mechanics be required to learn electric vehicle technology, or should it remain a specialization?"
        project_topics = "electric vehicle maintenance, ADAS calibration procedures, hybrid engine systems, autonomous driving technology, connected car diagnostics, hydrogen fuel cell vehicles"
    elif sp == "electricidad":
        innovation_text = "<em>The Future of Electrical Engineering</em> — smart grids, energy storage (batteries), microgrids, vehicle-to-grid technology, home automation, and the changing role of electricians in a decarbonized world."
        video_innov = "a YouTube video about a smart grid implementation project in a European city (adapted, 5 min)"
        case_final = "Case Study: <em>Traditional Grid vs. Smart Grid</em> — comparing Chile's current electrical infrastructure with a smart grid model: costs, benefits, reliability, environmental impact, and job implications for electricians."
        debate_final = "Should Chile invest in nuclear energy or continue expanding solar and wind power?"
        project_topics = "smart grid technology, battery storage systems, solar panel installation, electric vehicle charging infrastructure, home automation, microgrid design"
    elif sp == "electronica":
        innovation_text = "<em>The Future of Electronics</em> — flexible electronics, quantum computing basics, neuromorphic chips, advanced sensors, wearable medical devices, and the growing role of electronics in healthcare and agriculture."
        video_innov = "a YouTube video about wearable health technology and how electronic sensors monitor vital signs (adapted, 5 min)"
        case_final = "Case Study: <em>Consumer Electronics vs. Industrial Electronics</em> — comparing career paths: working in consumer device repair (smartphones, computers) vs. industrial electronics (automation, robotics). Salary, job satisfaction, growth potential."
        debate_final = "Should schools teach IoT programming to all students, or should it remain a technical specialty?"
        project_topics = "IoT applications in agriculture, wearable health devices, drone technology, flexible electronics, 3D-printed circuits, smart sensors in industry"
    elif sp == "grafica":
        innovation_text = "<em>The Future of Graphic Production</em> — 3D printing for packaging, augmented reality in print, sustainable materials, personalized printing (variable data), and the convergence of digital and physical media."
        video_innov = "a YouTube video about augmented reality packaging and interactive print media (adapted, 5 min)"
        case_final = "Case Study: <em>Print-Only Shop vs. Multi-Media Production House</em> — comparing a traditional print shop that only does offset printing with a modern production house that offers digital, 3D, and interactive print solutions. Business viability, skills needed, future prospects."
        debate_final = "Will 3D printing replace traditional manufacturing, or will they coexist?"
        project_topics = "3D printing in packaging, sustainable printing materials, augmented reality in print, digital vs. offset printing, print personalization, eco-friendly inks"
    else:  # industrial
        innovation_text = "<em>The Future of Industrial Manufacturing</em> — collaborative robots (cobots), additive manufacturing (3D metal printing), digital twins, predictive maintenance with AI, and the evolution of the industrial mechanic's role."
        video_innov = "a YouTube video about a collaborative robot (cobot) working alongside human operators in a factory (adapted, 5 min)"
        case_final = "Case Study: <em>The Automated Factory vs. The Skilled Workshop</em> — comparing a fully automated production line (minimal workers, maximum robots) with a precision workshop (skilled mechanics, custom jobs). Students evaluate: Which model is better for Chile? For workers? For the economy?"
        debate_final = "Will automation eliminate more jobs than it creates in Chile's industrial sector?"
        project_topics = "collaborative robots, 3D metal printing, digital twin technology, predictive maintenance, Industry 5.0, smart factories"

    classes = [
        # Class 1(27): Innovation Reading
        {
            "title": "Innovation & New Trends in the Field",
            "oa": "OA1",
            "bloom": f"Identificar y comprender las principales tendencias de innovación en {n} a partir de un texto técnico en inglés.",
            "inicio": f"""<ul>
                <li>Warm-up: imágenes de innovaciones tecnológicas del área. <em>\"What do you know about these technologies? Which one excites you most?\"</em></li>
                <li>Brainstorm: <em>\"What will {n.lower()} look like in 10 years?\"</em> — mapa conceptual en pizarra.</li>
                <li>Vocabulario: <em>innovation, disruption, automation, sustainability, efficiency, breakthrough, emerging technology</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {innovation_text} Texto adaptado A2-B1 (1.5 páginas).
                    <ul>
                        <li>Pre-reading: predicciones.</li>
                        <li>Lectura guiada con pausas para vocabulario.</li>
                        <li>Completar tabla: <b>Innovation → How it works → Impact on profession → Required skills → My opinion</b></li>
                    </ul>
                </li>
                <li><b>Comprehension (15 min):</b> 6 preguntas: 3 explícitas + 3 de opinión.</li>
                <li><b>Discussion (15 min):</b> En parejas: <em>\"Which innovation will most affect your career? How are you preparing for it?\"</em></li>
                <li><b>Vocabulary log (5 min):</b> 10 palabras nuevas con oración propia.</li>
            </ol>""",
            "cierre": """<ul>
                <li>3 estudiantes comparten su opinión sobre la innovación más importante.</li>
                <li>Conexión con proyecto final: <em>\"These topics could be great for your final project!\"</em></li>
            </ul>""",
            "recursos": f"Texto de innovación en {n.lower()} impreso, ficha de análisis, imágenes de innovaciones, pizarra.",
            "evaluacion": "Formativa — calidad de la tabla de análisis y participación en discusión.",
        },
        # Class 2(28): Video + Critical Analysis
        {
            "title": "Video: Innovation in Action",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender un video en inglés sobre innovación en {n} y construir una postura crítica personal fundamentada.",
            "inicio": f"""<ul>
                <li>Warm-up: <em>\"Imagine your workplace in 2035. What technology will you use daily?\"</em> — quick-write (3 min).</li>
                <li>Pre-viewing: preguntas guía y vocabulario clave del video.</li>
                <li>Predicción a partir del título.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Video (15 min):</b> {video_innov} Primera reproducción completa; segunda con pausas.</li>
                <li><b>Comprehension (10 min):</b> Responder preguntas guía. Corrección en parejas.</li>
                <li><b>Critical discussion (25 min):</b> Mesa redonda:
                    <ul>
                        <li><em>\"Is this innovation positive or negative for workers?\"</em></li>
                        <li><em>\"How will this affect job opportunities in Chile?\"</em></li>
                        <li><em>\"What new skills will technicians need?\"</em></li>
                    </ul>
                    Los estudiantes deben usar evidencia del video y de textos anteriores para argumentar.
                </li>
                <li><b>Written opinion (10 min):</b> Párrafo: <em>\"In my opinion, [innovation] will [positively/negatively] affect my career because...\"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>3-4 estudiantes leen su opinión escrita.</li>
                <li>Vocabulario nuevo registrado.</li>
            </ul>""",
            "recursos": f"Video sobre innovación en {n.lower()} (YouTube, 5 min adaptado), preguntas guía, ficha de opinión.",
            "evaluacion": "Formativa — calidad del análisis crítico y del párrafo de opinión.",
        },
        # Class 3(29): Comparative Case Study
        {
            "title": "Case Study: Comparing Approaches",
            "oa": "OA1 · OA3",
            "bloom": f"Comparar y evaluar críticamente dos modelos profesionales dentro de {n}, argumentando ventajas y desventajas en inglés.",
            "inicio": """<ul>
                <li>Warm-up: <em>\"Would you prefer to work in a traditional workplace or a high-tech one? Why?\"</em> — quick poll.</li>
                <li>Se introduce el concepto de análisis comparativo: pros, cons, conclusion.</li>
                <li>Vocabulario: <em>advantage, disadvantage, whereas, on the other hand, in contrast, similarly, overall</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {case_final} Texto adaptado A2-B1 (1.5 páginas).
                    <ul>
                        <li>Los estudiantes completan una tabla comparativa doble: <b>Aspect / Model A / Model B / My preference</b></li>
                        <li>Aspectos: cost, skills needed, job satisfaction, salary, future prospects, environmental impact.</li>
                    </ul>
                </li>
                <li><b>Debate preparation (15 min):</b> La clase se divide en dos: defensores del Modelo A y defensores del Modelo B. Cada grupo prepara 3 argumentos.</li>
                <li><b>Mini-debate (15 min):</b> Intercambio estructurado de argumentos. El docente modera.</li>
                <li><b>Individual conclusion (5 min):</b> Cada estudiante escribe: <em>\"After analyzing both models, I believe... because...\"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Votación final: ¿Qué modelo tiene mejor futuro?</li>
                <li>Conexión con su propia carrera y decisiones futuras.</li>
            </ul>""",
            "recursos": "Texto comparativo impreso, tabla de análisis doble, vocabulario de comparación en pizarra.",
            "evaluacion": "Formativa — calidad de la tabla comparativa, argumentos del debate y conclusión escrita.",
        },
        # Class 4(30): Debate + Eval Prep
        {
            "title": "Full Debate & Evaluation Preparation",
            "oa": "OA3 · OA4",
            "bloom": f"Defender una postura personal fundamentada sobre el futuro de {n} en un debate estructurado en inglés.",
            "inicio": f"""<ul>
                <li>Docente presenta el tema del debate final: <em>\"{debate_final}\"</em></li>
                <li>Los estudiantes eligen su postura y forman grupos.</li>
                <li>Se repasan las reglas y vocabulario de debate.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Argument preparation (10 min):</b> Los grupos finalizan sus argumentos con evidencia de todos los textos del semestre.</li>
                <li><b>Debate (30 min):</b> Estructura completa:
                    <ul>
                        <li>Opening statements (2 min).</li>
                        <li>Arguments (3 por lado).</li>
                        <li>Rebuttals (5 min).</li>
                        <li>Open questions (5 min).</li>
                        <li>Closing statements (2 min).</li>
                    </ul>
                </li>
                <li><b>Evaluation prep (15 min):</b> Docente prepara a los estudiantes para la prueba de lectura:
                    <ul>
                        <li>Repaso de estrategias: scanning, inference, vocabulary in context, critical opinion.</li>
                        <li>Formato de la prueba: vocabulario (8 pts) + comprensión (12 pts) + análisis crítico (10 pts) = 30 pts.</li>
                    </ul>
                </li>
                <li><b>Practice (5 min):</b> Mini-ejercicio de scanning con un texto breve.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Reflexión del debate: <em>\"Did anyone change their opinion after hearing the other side?\"</em></li>
                <li>Recordatorio de la evaluación de lectura de la próxima clase.</li>
            </ul>""",
            "recursos": "Vocabulario de debate, textos de referencia, ficha de preparación para evaluación.",
            "evaluacion": "Formativa — participación en debate y preparación para evaluación.",
        },
        # Class 5(31): EVALUACION — Reading Comprehension (Nota 2 S2)
        {
            "title": "EVALUACIÓN: Advanced Reading Comprehension",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender y analizar críticamente un texto técnico avanzado en inglés sobre innovación en {n}, demostrando competencias de lectura desarrolladas durante el año.",
            "inicio": """<ul>
                <li>Docente recuerda estrategias de lectura: <em>\"Use everything you have learned: scan first, then read for detail, then analyze.\"</em></li>
                <li>Se distribuye la prueba. Formato: Sección A (vocabulario, 8 pts), Sección B (comprensión, 12 pts), Sección C (análisis crítico, 10 pts).</li>
                <li>Tiempo: 70 minutos.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Evaluación escrita (70 min):</b> Texto sobre innovación y futuro de {n.lower()} (1.5 páginas, adaptado A2-B1).
                    <ul>
                        <li><b>Sección A — Vocabulario (8 pts):</b> 8 palabras técnicas: matching con definiciones.</li>
                        <li><b>Sección B — Comprensión (12 pts):</b> 4 preguntas explícitas (2 pts c/u) + 2 preguntas inferenciales (2 pts c/u).</li>
                        <li><b>Sección C — Análisis crítico (10 pts):</b> 2 preguntas de postura personal fundamentada (5 pts c/u): <em>\"Do you agree with the author? Why?\"</em>, <em>\"How will this innovation affect your career? Give specific reasons.\"</em></li>
                    </ul>
                    Total: 30 puntos.
                </li>
            </ol>""",
            "cierre": """<ul>
                <li>Entrega de pruebas.</li>
                <li><em>\"How did it go? We will review results next class along with your project presentations.\"</em></li>
            </ul>""",
            "recursos": "Prueba impresa (texto + preguntas en 3 secciones).",
            "evaluacion": "<b>SUMATIVA — Nota 2 Semestre 2:</b> Prueba de comprensión lectora avanzada. 30 pts (8 + 12 + 10). Exigencia 60%.",
        },
        # Class 6(32): Project Workshop + Results
        {
            "title": "Final Project Workshop & Evaluation Results",
            "oa": "OA1 · OA2 · OA4",
            "bloom": f"Finalizar la preparación del proyecto final de {n}, incorporando retroalimentación y ensayando la presentación oral.",
            "inicio": """<ul>
                <li>Devolución de resultados de la prueba de lectura con retroalimentación general.</li>
                <li>Recordatorio del proyecto final: <em>\"Your presentation is next class. Today is your last preparation session.\"</em></li>
                <li>Se repasan criterios: contenido técnico (5 pts), organización (5 pts), vocabulario (3 pts), pronunciación (4 pts), capacidad de responder preguntas (3 pts) = 20 pts.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Report finalization (20 min):</b> Los grupos finalizan su informe escrito (1 página). El docente revisa y da feedback rápido a cada grupo.</li>
                <li><b>Presentation rehearsal (25 min):</b> Cada grupo ensaya su presentación oral (5 min) frente a otro grupo. El grupo observador da feedback constructivo:
                    <ul>
                        <li>¿Se entiende el contenido?</li>
                        <li>¿El vocabulario técnico es correcto?</li>
                        <li>¿Hablan con claridad?</li>
                        <li>¿Pueden responder preguntas?</li>
                    </ul>
                </li>
                <li><b>Visual aids (10 min):</b> Los grupos preparan su material visual: póster, diapositivas o ficha resumen.</li>
                <li><b>Final check (5 min):</b> Docente confirma orden de presentaciones para la próxima clase.</li>
            </ol>""",
            "cierre": """<ul>
                <li><em>\"You are ready! Remember: speak clearly, use your vocabulary, and be confident. I believe in you!\"</em></li>
                <li>Orden de presentaciones publicado.</li>
            </ul>""",
            "recursos": "Informes de los grupos, rúbrica de proyecto final, materiales para visual aids, cronómetro.",
            "evaluacion": "Formativa — progreso del proyecto y calidad del ensayo.",
        },
        # Class 7(33): EVALUACION — Final Project Presentation (Nota 3 S2)
        {
            "title": "EVALUACIÓN: Final Project Defense",
            "oa": "OA1 · OA2 · OA3 · OA4",
            "bloom": f"Presentar y defender oralmente un proyecto de investigación técnica en inglés sobre {n}, demostrando dominio de vocabulario, comprensión lectora y pensamiento crítico.",
            "inicio": """<ul>
                <li>Docente organiza el aula para presentaciones: espacio para el grupo, proyector/pizarra, sillas tipo auditorio.</li>
                <li>Se repasan criterios de evaluación y reglas: 5 min de presentación + 2 min de preguntas por grupo.</li>
                <li>Se entregan fichas de peer feedback a la audiencia.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Project presentations (55 min):</b> Los grupos presentan en orden:
                    <ul>
                        <li>Cada grupo presenta su investigación (5 min): tema, investigación, análisis, conclusiones.</li>
                        <li>Después de cada presentación: 2 preguntas del docente + 1-2 del público.</li>
                        <li>La audiencia completa fichas de peer feedback.</li>
                    </ul>
                    Temas posibles: {project_topics}.
                </li>
                <li><b>Peer evaluation (5 min):</b> La audiencia vota: mejor presentación, vocabulario más impresionante, mejor uso de evidencia.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación general: destacar logros del grupo y aspectos memorables.</li>
                <li>Entrega de fichas de peer feedback a cada grupo.</li>
                <li><em>\"This is what professional English communication looks like. You should be proud!\"</em></li>
            </ul>""",
            "recursos": "Rúbrica de proyecto final (5 criterios = 20 pts), fichas de peer feedback, proyector, cronómetro.",
            "evaluacion": "<b>SUMATIVA — Nota 3 Semestre 2:</b> Proyecto final — Defensa de proyecto en inglés. 20 pts, 60% exigencia.",
            "sugerencia": "<b>Nota:</b> Si no alcanzan todas las presentaciones, continuar al inicio de la clase siguiente."
        },
        # Class 8(34): Year-End Closure
        {
            "title": "Year-End Review, Reflection & Farewell",
            "oa": "OA1 · OA2 · OA3 · OA4",
            "bloom": f"Sintetizar, reflexionar y evaluar el progreso personal en inglés técnico a lo largo de los dos años de formación en {n}.",
            "inicio": """<ul>
                <li>Si quedan presentaciones pendientes, se completan primero.</li>
                <li>Devolución de rúbricas del proyecto final y notas finales del año.</li>
                <li><em>\"This is our last class together. Let's celebrate and reflect on everything you have achieved.\"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Year review game (15 min):</b> <em>\"The Grand Finale Quiz\"</em> — equipos compiten con preguntas de todo el año: vocabulario, lectura, entrevistas, procedimientos, innovación, escritura. Formato <em>\"Who Wants to Be a Millionaire\"</em>.</li>
                <li><b>Reflection writing (15 min):</b> Cada estudiante escribe un párrafo en inglés: <em>\"When I started 3° Medio, I could... Now, finishing 4° Medio, I can... The most important thing I learned in English was... English will help me in my career because... My advice for future students is...\"</em></li>
                <li><b>Sharing circle (15 min):</b> Voluntarios leen sus reflexiones. El grupo aplaude cada contribución. El docente comparte sus propias reflexiones sobre el curso.</li>
                <li><b>Final self-assessment (10 min):</b> Ficha comparativa: <em>\"Beginning of 3° Medio vs. End of 4° Medio: what can I do now in English?\"</em> — vocabulary, reading, speaking, writing.</li>
                <li><b>Certificate ceremony (5 min):</b> Entrega simbólica de certificados: <em>\"Technical English Communicator — {n}\"</em>.</li>
            </ol>""",
            "cierre": f"""<ul>
                <li>Mensaje de cierre del docente: <em>\"You are leaving this school with a skill that many don't have: the ability to communicate in English in your profession. Never stop learning. I am very proud of each one of you.\"</em></li>
                <li>Foto grupal y despedida.</li>
            </ul>""",
            "recursos": "Quiz final en PPT/pizarra, ficha de reflexión, ficha de autoevaluación comparativa, certificados impresos.",
            "evaluacion": "Formativa — reflexión escrita y autoevaluación de cierre de ciclo.",
            "sugerencia": "<b>Sugerencia:</b> Preparar certificados personalizados de <em>Technical English Communicator</em> como reconocimiento del esfuerzo de dos años (3° y 4° Medio)."
        },
    ]
    return classes


# ============ HTML GENERATION ============

def generate_html(sp, unit_num, unit_title, classes_data, date_range, class_range, semester, focus):
    S = SPECIALTIES[sp]
    n = S["name"]
    c1 = S["color1"]
    c2 = S["color2"]
    bg = S["bg_light"]
    bg_acc = S["bg_accent"]
    tc = S["text_color"]

    class_start = class_range[0]

    # OA by unit (4to Medio OA)
    oa_map = {
        1: ["OA1: Comprender textos orales y escritos que contengan información relevante para un propósito específico.",
            "OA2: Producir textos orales y escritos claros para comunicar información.",
            "OA4: Producir y comprender con fluidez textos orales y escritos claros."],
        2: ["OA1: Comprender textos orales y escritos que contengan información relevante.",
            "OA3: Utilizar su conocimiento del inglés para construir postura personal crítica.",
            "OA4: Producir y comprender con fluidez textos orales y escritos claros."],
        3: ["OA1: Comprender textos orales y escritos que contengan información relevante.",
            "OA2: Producir textos orales y escritos claros para comunicar información.",
            "OA4: Producir y comprender con fluidez textos orales y escritos claros."],
        4: ["OA1: Comprender textos orales y escritos que contengan información relevante.",
            "OA3: Utilizar su conocimiento del inglés para construir postura personal crítica.",
            "OA4: Producir y comprender con fluidez textos orales y escritos claros."],
    }

    # Build eval summary
    eval_map = {
        1: f"""<ul>
            <li>Clase {class_start + 4}: <b>Nota 1 S1</b> — Mock Job Interview (entrevista laboral simulada). 20 pts.</li>
        </ul>""",
        2: f"""<ul>
            <li>Clase {class_start + 4}: <b>Nota 2 S1</b> — Prueba de comprensión lectora técnica. 30 pts.</li>
            <li>Clase {class_start + 5}: <b>Nota 3 S1</b> — Evaluación integradora semestral. 45 pts.</li>
        </ul>""",
        3: f"""<ul>
            <li>Clase {class_start + 6}: <b>Nota 1 S2</b> — Evaluación oral: explicar un procedimiento técnico. 20 pts.</li>
        </ul>""",
        4: f"""<ul>
            <li>Clase {class_start + 4}: <b>Nota 2 S2</b> — Prueba de comprensión lectora avanzada. 30 pts.</li>
            <li>Clase {class_start + 6}: <b>Nota 3 S2</b> — Proyecto final: defensa de proyecto en inglés. 20 pts.</li>
        </ul>"""
    }

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>4° Medio {n} - Unidad {unit_num}: {unit_title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; color: #333; line-height: 1.6; }}
        .header {{ background: linear-gradient(135deg, {c1}, {c2}); color: white; padding: 30px; text-align: center; }}
        .header h1 {{ font-size: 1.8em; margin-bottom: 5px; }}
        .header h2 {{ font-size: 1.3em; font-weight: 300; margin-bottom: 10px; }}
        .header .subtitle {{ font-size: 0.95em; opacity: 0.9; }}
        .meta-info {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 15px; }}
        .meta-info span {{ background: rgba(255,255,255,0.15); padding: 5px 15px; border-radius: 20px; font-size: 0.85em; }}
        .container {{ max-width: 1100px; margin: 20px auto; padding: 0 15px; }}
        .unit-overview {{ background: white; border-radius: 10px; padding: 25px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
        .unit-overview h3 {{ color: {tc}; margin-bottom: 15px; font-size: 1.2em; border-bottom: 2px solid {tc}; padding-bottom: 8px; }}
        .overview-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }}
        .overview-item {{ padding: 10px; background: {bg}; border-radius: 6px; }}
        .overview-item strong {{ color: {tc}; }}
        .overview-item ul {{ margin-left: 20px; margin-top: 5px; }}
        .overview-item ul li {{ margin-bottom: 3px; font-size: 0.9em; }}
        .clase-card {{ background: white; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow: hidden; }}
        .clase-card.evaluacion {{ border-left: 5px solid #c62828; }}
        .clase-header {{ padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }}
        .clase-header.normal {{ background: {bg_acc}; }}
        .clase-header.eval {{ background: #ffebee; }}
        .clase-header .clase-num {{ font-size: 1.1em; font-weight: 700; color: {tc}; }}
        .clase-header .clase-fecha {{ font-size: 0.85em; color: #666; }}
        .clase-header .badge {{ padding: 3px 10px; border-radius: 12px; font-size: 0.75em; font-weight: 600; }}
        .badge-oa {{ background: {bg}; color: {tc}; }}
        .badge-eval {{ background: #ffcdd2; color: #c62828; }}
        .clase-body {{ padding: 20px; }}
        .objetivo {{ background: #fff3e0; border-left: 4px solid #ef6c00; padding: 12px 15px; margin-bottom: 15px; border-radius: 0 6px 6px 0; }}
        .objetivo strong {{ color: #ef6c00; }}
        .fase {{ margin-bottom: 12px; }}
        .fase-title {{ display: inline-block; padding: 3px 12px; border-radius: 4px; font-weight: 600; font-size: 0.85em; color: white; margin-bottom: 6px; }}
        .fase-inicio {{ background: #2e7d32; }}
        .fase-desarrollo {{ background: #1565c0; }}
        .fase-cierre {{ background: #6a1b9a; }}
        .fase-content {{ padding-left: 15px; font-size: 0.92em; }}
        .fase-content ol, .fase-content ul {{ margin-left: 15px; }}
        .fase-content li {{ margin-bottom: 4px; }}
        .recursos {{ background: #f1f8e9; padding: 10px 15px; border-radius: 6px; margin-top: 10px; font-size: 0.88em; }}
        .recursos strong {{ color: #33691e; }}
        .evaluacion-box {{ background: #fce4ec; padding: 10px 15px; border-radius: 6px; margin-top: 10px; font-size: 0.88em; }}
        .evaluacion-box strong {{ color: #c62828; }}
        .sugerencia {{ background: #e8f5e9; border-left: 4px solid #2e7d32; padding: 10px 15px; border-radius: 0 6px 6px 0; margin-top: 10px; font-size: 0.88em; }}
        .sugerencia strong {{ color: #2e7d32; }}
        .notas-dist {{ background: white; border-radius: 10px; padding: 25px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
        .notas-dist h3 {{ color: #c62828; margin-bottom: 15px; font-size: 1.1em; }}
        table.notas {{ width: 100%; border-collapse: collapse; }}
        table.notas th {{ background: {c1}; color: white; padding: 8px 12px; text-align: left; font-size: 0.9em; }}
        table.notas td {{ padding: 8px 12px; border-bottom: 1px solid #e0e0e0; font-size: 0.88em; }}
        table.notas tr:nth-child(even) {{ background: {bg}; }}
        .footer {{ text-align: center; padding: 20px; color: #999; font-size: 0.8em; }}
        @media print {{
            body {{ background: white; }}
            .clase-card {{ break-inside: avoid; page-break-inside: avoid; box-shadow: none; border: 1px solid #ddd; }}
            .header {{ background: {c1} !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
        }}
        @media (max-width: 768px) {{
            .overview-grid {{ grid-template-columns: 1fr; }}
            .meta-info {{ flex-direction: column; align-items: center; }}
        }}
    </style>
</head>
<body>

<div class="header">
    <h1>PLANIFICACIÓN CLASE A CLASE — 4° MEDIO — {n.upper()}</h1>
    <h2>Unidad {unit_num}: {unit_title}</h2>
    <p class="subtitle">Inglés — Liceo Técnico Profesional — Año Escolar 2026 — {semester}</p>
    <div class="meta-info">
        <span>📅 {date_range}</span>
        <span>⏱ {len(classes_data)} clases de 90 min (Clases {class_range[0]}–{class_range[1]})</span>
        <span>📚 2 hrs/semana (1 sesión)</span>
        <span>🎯 Foco: {focus}</span>
    </div>
</div>

<div class="container">

    <div class="unit-overview">
        <h3>Visión General de la Unidad {unit_num}</h3>
        <div class="overview-grid">
            <div class="overview-item">
                <strong>OA Basales trabajados (4° Medio):</strong>
                <ul>
                    {"".join('<li><b>' + oa.split(":")[0] + ':</b>' + oa.split(":")[1] + '</li>' for oa in oa_map[unit_num])}
                </ul>
            </div>
            <div class="overview-item">
                <strong>Evaluaciones de la unidad:</strong>
                {eval_map[unit_num]}
            </div>
            <div class="overview-item">
                <strong>Habilidades priorizadas:</strong>
                <ul>
                    <li><b>Lectura:</b> Textos técnicos avanzados, estudios de caso, manuales e informes de {n.lower()}.</li>
                    <li><b>Expresión Oral:</b> Entrevistas, explicaciones de procedimientos, debates y defensa de proyectos.</li>
                </ul>
            </div>
            <div class="overview-item">
                <strong>Especialidad:</strong>
                <ul><li>{n}</li></ul>
                <strong>Nivel de los estudiantes:</strong>
                <ul><li>A1-A2 (Básico)</li></ul>
            </div>
        </div>
    </div>
"""

    # Generate class cards
    for i, cls in enumerate(classes_data):
        class_num = class_start + i
        is_eval = "EVALUACIÓN" in cls["title"] or "PROYECTO FINAL" in cls["title"].upper()
        eval_class = ' evaluacion' if is_eval else ""
        header_class = "eval" if is_eval else "normal"

        # Badges
        oa_badges = "".join('<span class="badge badge-oa">' + oa.strip() + '</span> ' for oa in cls["oa"].split("·"))
        eval_badge = '<span class="badge badge-eval">EVALUACIÓN</span>' if is_eval else ""

        # Sugerencia
        sug_html = ""
        if cls.get("sugerencia"):
            sug_html = '<div class="sugerencia"><strong>💡 Sugerencia:</strong> ' + cls["sugerencia"] + '</div>'

        html += f"""
    <!-- ==================== CLASE {class_num} ==================== -->
    <div class="clase-card{eval_class}">
        <div class="clase-header {header_class}">
            <span class="clase-num">Clase {class_num}</span>
            {oa_badges} {eval_badge}
        </div>
        <div class="clase-body">
            <div class="objetivo">
                <strong>Objetivo de la clase (Bloom):</strong> {cls["bloom"]}
            </div>
            <div class="fase">
                <span class="fase-title fase-inicio">INICIO (15 min)</span>
                <div class="fase-content">
                    {cls["inicio"]}
                </div>
            </div>
            <div class="fase">
                <span class="fase-title fase-desarrollo">DESARROLLO (60 min)</span>
                <div class="fase-content">
                    {cls["desarrollo"]}
                </div>
            </div>
            <div class="fase">
                <span class="fase-title fase-cierre">CIERRE (15 min)</span>
                <div class="fase-content">
                    {cls["cierre"]}
                </div>
            </div>
            <div class="recursos">
                <strong>📦 Recursos:</strong> {cls["recursos"]}
            </div>
            <div class="evaluacion-box">
                <strong>📋 Evaluación:</strong> {cls["evaluacion"]}
            </div>
            {sug_html}
        </div>
    </div>
"""

    # Footer
    html += f"""
    <div class="footer">
        <p>Planificación elaborada para Liceo Técnico Profesional — Inglés 4° Medio — Especialidad: {n} — 2026</p>
        <p>Basada en OA de Bases Curriculares 3°-4° Medio (Decreto N°193/2019) y Programa de Estudio (Decreto N°496/2020)</p>
    </div>
</div>
</body>
</html>
"""
    return html


# =============== MAIN ===============

def adapt_classes_for_unit(classes_data, target_classes):
    adjusted = [dict(item) for item in classes_data]

    def is_eval_class(item):
        title = (item.get("title") or "").upper()
        return "EVALUACIÓN" in title or "PROYECTO FINAL" in title

    if len(adjusted) > target_classes:
        eval_items = [item for item in adjusted if is_eval_class(item)]
        normal_items = [item for item in adjusted if not is_eval_class(item)]

        normal_slots = max(0, target_classes - len(eval_items))
        adjusted = normal_items[:normal_slots] + eval_items

        indexed = []
        for item in adjusted:
            try:
                indexed.append((classes_data.index(item), item))
            except ValueError:
                indexed.append((9999, item))
        return [item for _, item in sorted(indexed, key=lambda x: x[0])][:target_classes]

    if len(adjusted) < target_classes:
        for extra_idx in range(len(adjusted) + 1, target_classes + 1):
            adjusted.append({
                "title": f"Consolidation & Reinforcement Workshop {extra_idx}",
                "oa": "OA1 · OA4",
                "bloom": "Consolidar aprendizajes de la unidad mediante actividades integradas de lectura técnica, producción oral y transferencia al contexto laboral.",
                "inicio": "<ul><li>Activación de conocimientos previos con repaso focalizado de vocabulario técnico.</li><li>Presentación de objetivo de consolidación y criterios de desempeño.</li></ul>",
                "desarrollo": "<ol><li><b>Revisión guiada:</b> análisis de un insumo técnico breve en inglés.</li><li><b>Aplicación:</b> actividad colaborativa orientada a resolución de situaciones profesionales.</li><li><b>Comunicación:</b> presentación oral breve de resultados con retroalimentación docente.</li></ol>",
                "cierre": "<ul><li>Síntesis de aprendizajes logrados.</li><li>Autoevaluación y compromiso de mejora para la siguiente sesión.</li></ul>",
                "recursos": "Guías de consolidación, texto técnico breve, pizarra y recursos digitales de apoyo.",
                "evaluacion": "Formativa — desempeño en aplicación, comunicación y reflexión.",
                "sugerencia": None,
            })

    return adjusted

UNITS = [
    {
        "num": 1,
        "title": "Professional Profile & Workplace English",
        "classes_fn": u1_classes,
        "target_classes": 8,
        "date_range": "10 marzo – 3 mayo (8 sesiones)",
        "class_range": (1, 8),
        "semester": "Semestre 1",
        "focus": "Perfil profesional, CV en inglés, entrevista laboral, comunicación en el trabajo"
    },
    {
        "num": 2,
        "title": "Advanced Technical Reading & Critical Thinking",
        "classes_fn": u2_classes,
        "target_classes": 7,
        "date_range": "4 mayo – 18 junio (7 sesiones)",
        "class_range": (9, 15),
        "semester": "Semestre 1",
        "focus": "Estudios de caso avanzados, debate estructurado, evaluación integradora"
    },
    {
        "num": 3,
        "title": "Technical Documentation & Procedures",
        "classes_fn": u3_classes,
        "target_classes": 8,
        "date_range": "6 julio – 30 agosto (8 sesiones)",
        "class_range": (16, 23),
        "semester": "Semestre 2",
        "focus": "Manuales técnicos, redacción de informes, explicación de procedimientos"
    },
    {
        "num": 4,
        "title": "Innovation, Project Defense & Closure",
        "classes_fn": u4_classes,
        "target_classes": 10,
        "date_range": "31 agosto – 13 noviembre (10 sesiones; sin clases 14–20 sept.)",
        "class_range": (24, 33),
        "semester": "Semestre 2",
        "focus": "Innovación tecnológica, debate final, defensa de proyecto, cierre del año"
    },
]

# Generate all files
count = 0
for unit in UNITS:
    for sp_key in SPECIALTIES:
        # Create directory
        folder = os.path.join(BASE, f"Unidad {unit['num']}")
        os.makedirs(folder, exist_ok=True)

        # Generate classes
        classes_data = unit["classes_fn"](sp_key)
        classes_data = adapt_classes_for_unit(classes_data, target_classes=unit["target_classes"])

        # Generate HTML
        html = generate_html(
            sp=sp_key,
            unit_num=unit["num"],
            unit_title=unit["title"],
            classes_data=classes_data,
            date_range=unit["date_range"],
            class_range=unit["class_range"],
            semester=unit["semester"],
            focus=unit["focus"]
        )

        # Write file
        filename = f"planificacion_u{unit['num']}_{sp_key}.html"
        filepath = os.path.join(folder, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        count += 1
        print(f"✓ Created: 4to Medio/Unidad {unit['num']}/{filename}")

print(f"\n✅ {count} archivos generados exitosamente para 4° Medio")
