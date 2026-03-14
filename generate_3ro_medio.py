#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generates all 20 HTML planificación files for 3° Medio (5 specialties × 4 units).
"""
import os

BASE = r"c:\Users\crist\OneDrive\Escritorio\2026\3ro Medio"

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
    "grafica": {
        "name": "Gráfica",
        "adj": "gráfica",
        "color1": "#4a148c", "color2": "#6a1b9a",
        "bg_light": "#f3e5f5", "bg_accent": "#e1bee7",
        "text_color": "#4a148c",
    },
    "industrial": {
        "name": "Mecánica Industrial",
        "adj": "industrial",
        "color1": "#263238", "color2": "#455a64",
        "bg_light": "#eceff1", "bg_accent": "#cfd8dc",
        "text_color": "#263238",
    },
}

# ================= UNIT CONTENT =================
# Structure: per unit, per specialty, list of classes
# Each class: (title, oa_badges, bloom_objective, inicio, desarrollo, cierre, recursos, evaluacion_or_none, sugerencia_or_none)

def u1_classes(sp):
    """Unit 1: Technical Skills & Career Paths — 9 classes, March–April"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        vocab_area = "engine parts, tools (wrench, jack, screwdriver), vehicle systems (brakes, transmission, suspension)"
        reading1 = "a short adapted text: <em>'A Day in an Automotive Workshop'</em> describing the daily routine of a mechanic: checking engines, changing oil, testing brakes."
        case_study = "Case Study: <em>'The Overheating Engine'</em> — A client brings a car with an overheating problem. Students read the diagnostic steps: check coolant level, inspect thermostat, test radiator fan."
        oral_topic = "Describe the main systems of a car (engine, brakes, transmission, electrical) and one tool used for each."
        video_desc = "YouTube video: 'How a Car Engine Works' (animated, 5 min) — students watch with subtitles and answer guided questions."
        reading2 = "<em>'Safety in the Automotive Workshop'</em> — PPE (gloves, goggles, boots), handling chemicals, lifting procedures."
        project_desc = "Present 'My Automotive Skills': describe 3 tools you know how to use, 2 car systems you understand, and why automotive mechanics is important."
        vocab_list = "engine, brake pad, transmission, coolant, wrench, jack, spark plug, oil filter, radiator, exhaust, tire, battery, alternator, diagnostic scanner"
    elif sp == "electricidad":
        vocab_area = "electrical components (wire, circuit breaker, panel, switch), tools (multimeter, pliers, wire stripper), systems (residential, industrial)"
        reading1 = "a short adapted text: <em>'A Day as an Electrician'</em> describing tasks: installing wiring, checking circuits, replacing panels."
        case_study = "Case Study: <em>'The Power Outage'</em> — A home loses power in the kitchen. Students read the diagnostic steps: check circuit breaker, test outlets with multimeter, inspect wiring."
        oral_topic = "Describe the main components of a residential electrical system (panel, circuit breaker, wiring, outlets) and one tool used for each."
        video_desc = "YouTube video: 'How Electricity Works — Basics' (animated, 5 min) — students watch with subtitles and identify key vocabulary."
        reading2 = "<em>'Electrical Safety Rules'</em> — PPE, lockout/tagout procedures, working with live circuits, grounding."
        project_desc = "Present 'My Electrical Skills': describe 3 tools you know how to use, 2 electrical systems you understand, and why electrical work is important."
        vocab_list = "wire, circuit, breaker, panel, switch, outlet, voltage, current, resistance, multimeter, pliers, conduit, transformer, grounding"
    elif sp == "electronica":
        vocab_area = "electronic components (resistor, capacitor, transistor, LED, PCB), tools (soldering iron, oscilloscope, multimeter), systems (digital, analog)"
        reading1 = "a short adapted text: <em>'A Day in an Electronics Lab'</em> describing tasks: assembling circuits, soldering components, testing devices."
        case_study = "Case Study: <em>'The Faulty Circuit Board'</em> — A device stops working. Students read the diagnostic steps: visual inspection, continuity test, component replacement."
        oral_topic = "Describe the main components of an electronic circuit (resistor, capacitor, transistor, LED) and their basic functions."
        video_desc = "YouTube video: 'How Electronic Components Work' (animated, 5 min) — students watch and match components to their functions."
        reading2 = "<em>'Safety in the Electronics Workshop'</em> — ESD protection, soldering safety, handling chemicals, proper ventilation."
        project_desc = "Present 'My Electronics Skills': describe 3 components you know, 2 tools you can use, and why electronics is important today."
        vocab_list = "resistor, capacitor, transistor, LED, PCB, soldering iron, oscilloscope, diode, integrated circuit, sensor, amplifier, frequency, signal, voltage"
    elif sp == "grafica":
        vocab_area = "printing components (ink, paper, plate, press), tools (color guide, densitometer, cutter), processes (offset, digital, binding)"
        reading1 = "a short adapted text: <em>'A Day in a Print Shop'</em> describing tasks: preparing files, operating the press, checking color quality."
        case_study = "Case Study: <em>'The Color Mismatch'</em> — A client complains that printed colors don't match the original design. Students read the diagnostic steps: check color profiles, inspect plates, calibrate press."
        oral_topic = "Describe the main stages of the printing process (prepress, press, postpress) and one tool used in each stage."
        video_desc = "YouTube video: 'How Offset Printing Works' (animated, 5 min) — students watch and sequence the printing steps."
        reading2 = "<em>'Safety in the Print Shop'</em> — chemical handling (inks, solvents), machine safety, noise protection, ventilation."
        project_desc = "Present 'My Graphic Skills': describe 3 printing processes you know, 2 tools you can use, and why the graphic industry matters."
        vocab_list = "ink, paper, plate, press, offset, digital printing, binding, color profile, CMYK, resolution, prepress, cutter, laminator, densitometer"
    else:  # industrial
        vocab_area = "machine parts (lathe, mill, drill press, welder), tools (caliper, micrometer, file), processes (welding, turning, milling)"
        reading1 = "a short adapted text: <em>'A Day in an Industrial Workshop'</em> describing tasks: operating a lathe, welding metal pieces, measuring with a caliper."
        case_study = "Case Study: <em>'The Defective Weld'</em> — A welded joint fails inspection. Students read the diagnostic steps: visual inspection, check welding parameters, test joint strength."
        oral_topic = "Describe the main machines in an industrial workshop (lathe, mill, drill press, welder) and what each one does."
        video_desc = "YouTube video: 'How a Lathe Works' (animated, 5 min) — students watch and label parts of the machine."
        reading2 = "<em>'Safety in the Industrial Workshop'</em> — PPE (helmet, face shield, gloves), machine guards, welding safety, lifting procedures."
        project_desc = "Present 'My Industrial Skills': describe 3 machines you know, 2 tools you can use, and why industrial mechanics is essential."
        vocab_list = "lathe, mill, drill press, welder, caliper, micrometer, file, grinding wheel, vise, clamp, blueprint, tolerance, steel, aluminum"

    classes = [
        # Class 1: Introduction
        {
            "title": f"Introduction to Technical English for {n}",
            "oa": "OA1",
            "bloom": f"Identificar vocabulario técnico básico en inglés relacionado con la especialidad de {n} mediante la exploración de textos e imágenes del campo profesional.",
            "inicio": f"""<ul>
                <li>Docente saluda en inglés y presenta el objetivo: <em>"This year, we will learn English for your career in {n}."</em></li>
                <li>Activación de conocimientos previos: <em>"What English words do you already know from your specialty?"</em> — Lluvia de ideas en la pizarra.</li>
                <li>Se muestran 3-4 imágenes reales de talleres/laboratorios de {n.lower()} y se pregunta: <em>"What do you see? Can you name anything in English?"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Vocabulary introduction (20 min):</b> Presentación visual de 14 palabras clave del área: {vocab_list}. Los estudiantes copian en sus cuadernos con dibujo/imagen asociada.</li>
                <li><b>Matching activity (15 min):</b> Ficha con imágenes de herramientas/componentes — los estudiantes asocian imagen con palabra en inglés. Trabajo en parejas.</li>
                <li><b>Listening & Reading (15 min):</b> Docente lee {reading1} Los estudiantes siguen la lectura en una ficha y subrayan las palabras nuevas.</li>
                <li><b>Comprehension check (10 min):</b> 5 preguntas True/False sobre el texto leído. Corrección grupal.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Ticket de salida: los estudiantes escriben 5 palabras nuevas que aprendieron hoy y su significado.</li>
                <li>Pregunta de reflexión: <em>"Why is it important to know English in your career?"</em> — 2-3 estudiantes comparten oralmente.</li>
            </ul>""",
            "recursos": f"Imágenes impresas/proyectadas de talleres de {n.lower()}, ficha de vocabulario con 14 palabras, ficha de lectura impresa, pizarra.",
            "evaluacion": "Diagnóstica informal — el docente observa nivel de reconocimiento de vocabulario y capacidad de lectura.",
            "sugerencia": None
        },
        # Class 2: Reading workshop
        {
            "title": "Reading Workshop: Job Profiles & Daily Routines",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender información explícita en un texto adaptado sobre el perfil laboral y la rutina diaria de un profesional de {n}.",
            "inicio": f"""<ul>
                <li>Warm-up: Repaso rápido del vocabulario de la clase anterior con flashcards (docente muestra imagen, estudiantes dicen la palabra en inglés).</li>
                <li>Pre-reading: <em>"What does a {n.lower().split()[0] if ' ' in n.lower() else n.lower()} professional do every day? What tasks do they perform?"</em> — Lluvia de ideas en español e inglés.</li>
                <li>Se enseñan 3 expresiones de rutina: <em>"Every day, he/she checks…", "He/she uses… to…", "First…, then…, finally…"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Pre-reading strategies (10 min):</b> Los estudiantes observan el título, imágenes y subtítulos del texto. Hacen predicciones: <em>"What is this text about?"</em></li>
                <li><b>Reading (20 min):</b> Lectura guiada de {reading1} El docente lee en voz alta primero; luego los estudiantes releen en silencio. Subrayan verbos de acción y vocabulario técnico.</li>
                <li><b>Comprehension tasks (20 min):</b>
                    <ul>
                        <li>a) Responder 6 preguntas de comprensión (3 explícitas + 3 inferenciales).</li>
                        <li>b) Completar una tabla: Task / Tool used / Time of day.</li>
                        <li>c) Identificar el propósito del texto: informar, instruir o persuadir.</li>
                    </ul>
                </li>
                <li><b>Oral practice (10 min):</b> En parejas, los estudiantes se turnan describiendo una tarea del texto: <em>"The mechanic/electrician/technician checks the… every morning."</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Post-reading: los estudiantes resumen el texto en 3 oraciones simples en inglés (pueden usar el texto como apoyo).</li>
                <li>Reflexión oral: <em>"What was the most interesting task mentioned in the text? Why?"</em></li>
            </ul>""",
            "recursos": "Ficha de lectura impresa (texto adaptado A1-A2), ficha de preguntas de comprensión, tabla para completar, pizarra.",
            "evaluacion": "Formativa — revisión de respuestas de comprensión y observación de producción oral en parejas.",
            "sugerencia": "Si los estudiantes terminan rápido la actividad de comprensión, pueden crear 2 preguntas adicionales sobre el texto para intercambiar con otro compañero."
        },
        # Class 3: Vocabulary deep dive & grammar intro
        {
            "title": f"Technical Vocabulary & Simple Present for Routines",
            "oa": "OA1 · OA4",
            "bloom": f"Aplicar vocabulario técnico de {n} en oraciones simples utilizando Simple Present para describir rutinas laborales.",
            "inicio": f"""<ul>
                <li>Vocabulary warm-up: Juego <em>"Word Race"</em> — dos equipos compiten por escribir la mayor cantidad de palabras técnicas en inglés en 2 minutos.</li>
                <li>Docente presenta el objetivo: <em>"Today we will learn to describe what professionals do every day using Simple Present."</em></li>
                <li>Repaso rápido de Simple Present: <em>"He checks / She uses / They repair"</em> — estructura en la pizarra.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Vocabulary expansion (15 min):</b> Se introducen 8 verbos de acción comunes en el área: </li>
                <ul><li>Ej: <em>check, repair, install, measure, test, replace, adjust, calibrate</em></li></ul>
                <li>Los estudiantes completan oraciones: <em>"A {n.lower().split()[-1] if ' ' in n else n.lower()} technician _____ (verb) the _____ (tool/part) every day."</em></li>
                <li><b>Sentence building (20 min):</b> Con tarjetas recortables (sujeto + verbo + objeto), los estudiantes construyen 8 oraciones correctas sobre rutinas del área. Trabajo en parejas.</li>
                <li><b>Oral drill (15 min):</b> Actividad <em>"Interview a Technician"</em> — En parejas, A es un periodista y B es un técnico. A pregunta: <em>"What do you do every day?"</em> B responde usando Simple Present y vocabulario técnico. Luego cambian roles.</li>
                <li><b>Writing (10 min):</b> Cada estudiante escribe un párrafo de 5 oraciones: <em>"My name is… I study {n}. Every day at the workshop, I…"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>3 estudiantes leen sus párrafos frente al curso.</li>
                <li>Corrección colaborativa: el docente y los compañeros ayudan a mejorar la pronunciación y gramática.</li>
                <li>Ticket de salida: escribir 3 oraciones nuevas sobre rutinas técnicas.</li>
            </ul>""",
            "recursos": "Tarjetas recortables (sujetos, verbos, objetos), ficha de ejercicios de completación, pizarra, cuaderno.",
            "evaluacion": "Formativa — revisión de párrafos escritos; observación de producción oral en actividad de entrevista.",
            "sugerencia": None
        },
        # Class 4: Case Study
        {
            "title": f"Case Study: Problem Diagnosis in {n}",
            "oa": "OA1 · OA3",
            "bloom": f"Analizar un estudio de caso técnico en inglés identificando el problema, las causas posibles y los pasos de diagnóstico en el contexto de {n}.",
            "inicio": f"""<ul>
                <li>Docente proyecta una imagen de un problema técnico (ej: máquina dañada, falla visible) y pregunta: <em>"What do you think happened? What is the problem?"</em></li>
                <li>Se introduce vocabulario clave para resolución de problemas: <em>problem, cause, symptom, diagnosis, solution, step, check, inspect, test, replace</em>.</li>
                <li>Pre-reading: <em>"Today we will read a real case study. You will be the technician who solves the problem."</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading the case study (25 min):</b> {case_study}
                    <ul>
                        <li>Primera lectura silenciosa (5 min). Estudiantes subrayan palabras desconocidas.</li>
                        <li>Segunda lectura guiada por el docente. Se aclara vocabulario en contexto.</li>
                        <li>Completar ficha de análisis: <b>Problem → Symptoms → Diagnostic Steps → Solution</b></li>
                    </ul>
                </li>
                <li><b>Group discussion (15 min):</b> En grupos de 3-4, los estudiantes discuten:
                    <ul>
                        <li><em>"What was the problem?"</em></li>
                        <li><em>"What steps did the technician follow?"</em></li>
                        <li><em>"Do you agree with the solution? Why or why not?"</em></li>
                    </ul>
                </li>
                <li><b>Sequencing activity (10 min):</b> Los estudiantes reciben los pasos del diagnóstico desordenados y deben ponerlos en orden correcto usando: <em>First… Then… After that… Finally…</em></li>
                <li><b>Oral report (10 min):</b> Un representante de cada grupo explica al curso: <em>"The problem was… First, the technician… Then… The solution was…"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Reflexión: <em>"Was this case study similar to situations you have seen in your workshop? Tell us."</em></li>
                <li>Los estudiantes escriben en su cuaderno una oración sobre lo que aprendieron: <em>"Today I learned that…"</em></li>
            </ul>""",
            "recursos": "Ficha de estudio de caso impresa, ficha de análisis (Problem/Symptoms/Steps/Solution), tarjetas de secuencia recortables, pizarra.",
            "evaluacion": "Formativa — revisión de ficha de análisis completada; evaluación de participación oral en grupo.",
            "sugerencia": "<b>Actividad de extensión:</b> Los estudiantes pueden inventar su propio caso de estudio breve (5 oraciones) describiendo un problema diferente del área, para compartir en la siguiente clase."
        },
        # Class 5: Video & Oral Practice
        {
            "title": "Video Comprehension & Oral Description",
            "oa": "OA1 · OA4",
            "bloom": f"Comprender información específica en un video técnico en inglés y producir descripciones orales breves sobre equipos y procesos de {n}.",
            "inicio": f"""<ul>
                <li>Warm-up: repaso del caso de estudio de la clase anterior — <em>"Who remembers the problem? What was the solution?"</em> 2-3 estudiantes recuentan oralmente.</li>
                <li>Pre-viewing: el docente introduce el video: {video_desc}</li>
                <li>Se entregan 5 preguntas guía que los estudiantes deben responder durante el video.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>First viewing (10 min):</b> Estudiantes miran el video completo con subtítulos en inglés para comprensión general. No responden preguntas aún.</li>
                <li><b>Second viewing (10 min):</b> Se reproduce el video por segmentos, pausando para que los estudiantes respondan las 5 preguntas guía en su ficha.</li>
                <li><b>Vocabulary from video (10 min):</b> Docente extrae 8-10 palabras/frases clave del video y las presenta en contexto. Estudiantes las registran con definición simple.</li>
                <li><b>Oral practice — Describe & Explain (20 min):</b> Actividad en parejas: {oral_topic} Cada estudiante tiene 2 minutos para su descripción. El compañero toma notas y hace 1 pregunta.</li>
                <li><b>Class sharing (10 min):</b> 3-4 voluntarios presentan su descripción al curso. Retroalimentación del docente en pronunciación y contenido.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Quick quiz oral: el docente dice una definición y los estudiantes deben decir la palabra técnica correspondiente.</li>
                <li>Reflexión: <em>"What new thing did you learn from the video?"</em> — Ticket de salida escrito (2-3 oraciones).</li>
            </ul>""",
            "recursos": "Video proyectado (YouTube, 5 min con subtítulos), ficha de preguntas guía, ficha de vocabulario del video, pizarra.",
            "evaluacion": "Formativa — revisión de respuestas del video; observación de producción oral en actividad de descripción.",
            "sugerencia": None
        },
        # Class 6: Reading - Safety & Procedures
        {
            "title": f"Reading: Safety Rules in the {n} Workshop",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender y evaluar reglas de seguridad escritas en inglés relevantes al taller de {n}, identificando información explícita e implícita.",
            "inicio": f"""<ul>
                <li>Docente muestra imágenes de EPP (PPE) y pregunta: <em>"What are these items? When do you use them?"</em> — Lluvia de ideas.</li>
                <li>Vocabulario previo: <em>safety goggles, gloves, helmet, boots, fire extinguisher, first aid kit, warning sign</em>.</li>
                <li>Pregunta de activación: <em>"Have you ever seen a safety manual in English? What information does it contain?"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> Lectura del texto {reading2}
                    <ul>
                        <li>Estrategia de lectura: <b>scanning</b> — los estudiantes buscan información específica: <em>"Find 3 rules about protective equipment"</em> y <em>"Find 2 emergency procedures."</em></li>
                        <li>Segunda lectura para comprensión global. Completar tabla: <b>Safety Rule → Reason → Equipment Needed</b>.</li>
                    </ul>
                </li>
                <li><b>Critical thinking (15 min):</b> En grupos de 3, los estudiantes discuten:
                    <ul>
                        <li><em>"Which rule is the most important? Why?"</em></li>
                        <li><em>"What happens if you don't follow this rule?"</em></li>
                        <li><em>"Are there rules missing? What would you add?"</em></li>
                    </ul>
                </li>
                <li><b>Poster creation (20 min):</b> Cada grupo crea un mini-póster de seguridad en inglés (en papel A3) con 5 reglas ilustradas: <em>"Always wear…", "Never touch…", "In case of emergency…"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Cada grupo presenta su póster brevemente al curso (1 min por grupo).</li>
                <li>Votación: <em>"Which poster is the clearest? The most creative?"</em></li>
                <li>Docente recuerda que la próxima clase es preparación para la evaluación oral.</li>
            </ul>""",
            "recursos": "Texto de seguridad impreso, fichas de análisis, papel A3, marcadores de colores, imágenes de EPP, pizarra.",
            "evaluacion": "Formativa — revisión de tabla de comprensión; evaluación de pósters de seguridad (contenido + uso del inglés).",
            "sugerencia": "<b>Sugerencia de evaluación:</b> Los pósters pueden exhibirse en el taller de la especialidad como recurso visual permanente."
        },
        # Class 7: Preparation for oral evaluation
        {
            "title": "Preparing My Oral Presentation",
            "oa": "OA4",
            "bloom": f"Organizar y ensayar una presentación oral en inglés sobre las habilidades técnicas y conocimientos adquiridos en {n}.",
            "inicio": f"""<ul>
                <li>Docente presenta la evaluación oral (Nota 1 S1) con la rúbrica: <em>"{project_desc}"</em></li>
                <li>Se revisan criterios de evaluación: contenido (4 pts), vocabulario técnico (4 pts), pronunciación (4 pts), fluidez (4 pts), estructura (4 pts). Total: 20 puntos.</li>
                <li>Se muestra un modelo de presentación (docente hace una demo breve).</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Planning (15 min):</b> Cada estudiante completa una ficha de planificación:
                    <ul>
                        <li>Introduction: Name, specialty, why I chose it</li>
                        <li>Body: 3 tools/equipment + 2 systems/processes I know</li>
                        <li>Conclusion: Why {n.lower()} is important for society</li>
                    </ul>
                </li>
                <li><b>Script writing (20 min):</b> Los estudiantes escriben un guion de 8-12 oraciones. El docente circula apoyando con vocabulario y estructura.</li>
                <li><b>Peer rehearsal (20 min):</b> En parejas, los estudiantes practican su presentación. El compañero da retroalimentación usando una checklist: <em>"Did they mention 3 tools? Was the pronunciation clear? Did they use technical vocabulary?"</em></li>
                <li><b>Final adjustments (5 min):</b> Los estudiantes ajustan su guion basándose en la retroalimentación recibida.</li>
            </ol>""",
            "cierre": """<ul>
                <li>El docente resuelve dudas finales de pronunciación (practica palabras difíciles con todo el grupo).</li>
                <li>Recordatorio: <em>"Next class is your oral presentation. Bring your notes but try to speak without reading."</em></li>
            </ul>""",
            "recursos": "Ficha de planificación de presentación, rúbrica impresa (una por estudiante), modelo de presentación (escrito en PPT o pizarra), checklist de retroalimentación entre pares.",
            "evaluacion": "Preparación — no calificada. El docente revisa borradores y da retroalimentación individual.",
            "sugerencia": "<b>Sugerencia:</b> Permitir que los estudiantes usen apoyo visual (imágenes, diagramas) en su presentación para reducir la dependencia del texto escrito."
        },
        # Class 8: ORAL EVALUATION (Nota 1)
        {
            "title": f"EVALUACIÓN ORAL — Nota 1 S1: 'My Technical Skills in {n}'",
            "oa": "OA4",
            "bloom": f"Producir una presentación oral breve y clara en inglés describiendo sus habilidades técnicas y conocimientos en {n}.",
            "inicio": f"""<ul>
                <li>Docente recuerda los criterios de evaluación y la estructura esperada.</li>
                <li>Warm-up de pronunciación grupal: se practican 5 palabras técnicas difíciles del área.</li>
                <li>Se establece el orden de presentaciones y las normas de audiencia (escuchar con respeto, no interrumpir).</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Presentaciones orales (55 min):</b> Cada estudiante presenta durante 2-3 minutos. {project_desc}
                    <ul>
                        <li>El docente evalúa con la rúbrica (contenido, vocabulario, pronunciación, fluidez, estructura).</li>
                        <li>Los compañeros completan una ficha de <em>peer feedback</em> por cada presentador (1 fortaleza + 1 sugerencia).</li>
                    </ul>
                </li>
                <li><b>Si sobra tiempo:</b> Ronda de preguntas breves del docente a algunos presentadores: <em>"Which tool is the most useful? Why?"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación general del docente: aspectos positivos y áreas de mejora del grupo.</li>
                <li>Los estudiantes entregan sus fichas de <em>peer feedback</em>.</li>
                <li>Reflexión: <em>"How did you feel presenting in English? What can you improve?"</em></li>
            </ul>""",
            "recursos": "Rúbrica de evaluación oral, fichas de peer feedback, cronómetro, proyector (para apoyo visual de estudiantes).",
            "evaluacion": f"<b>SUMATIVA — Nota 1 Semestre 1:</b> Presentación oral 'My Technical Skills in {n}'. Rúbrica de 5 criterios × 4 puntos = 20 pts. Exigencia 60%.",
            "sugerencia": "<b>Consideración:</b> Para estudiantes con alta ansiedad, permitir presentar en parejas o en formato grabado (video). Mantener los mismos criterios de evaluación."
        },
        # Class 9: Wrap-up & transition
        {
            "title": "Unit Review & Moving Forward",
            "oa": "OA1 · OA3 · OA4",
            "bloom": f"Sintetizar los aprendizajes de vocabulario técnico, lectura y expresión oral adquiridos en la Unidad 1 sobre {n}.",
            "inicio": """<ul>
                <li>Docente felicita por las presentaciones orales y comparte resultados generales (sin notas individuales).</li>
                <li>Actividad de activación: <em>"Word Cloud"</em> — cada estudiante escribe en un papelito 3 palabras que resumen lo que aprendió en la unidad. Se pegan en la pizarra.</li>
                <li>Pregunta: <em>"How many technical words in English can you remember from this unit?"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Vocabulary review game (20 min):</b> Juego tipo <em>"Jeopardy"</em> con categorías: Tools, Safety, Processes, Job Descriptions. Equipos de 4-5 compiten por puntos respondiendo en inglés.</li>
                <li><b>Reading review (15 min):</b> Mini-lectura nueva (media página): un breve artículo sobre una innovación reciente en {n.lower()}. Los estudiantes practican estrategias aprendidas: predicción, scanning, inferencia.</li>
                <li><b>Speaking circle (15 min):</b> Actividad <em>"Hot Seat"</em>: un estudiante se sienta al frente y los compañeros le hacen preguntas en inglés sobre la especialidad. El estudiante responde improvisando.</li>
                <li><b>Self-assessment (10 min):</b> Los estudiantes completan una ficha de autoevaluación: <em>"I can name ___ tools in English. I can describe ___. I need to practice more on ___."</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Docente introduce brevemente la Unidad 2: <em>"Next unit, we will explore technical challenges and global issues related to your field."</em></li>
                <li>Distribución de resultados individuales de la evaluación oral (rúbricas con retroalimentación).</li>
            </ul>""",
            "recursos": "Papelitos para Word Cloud, juego Jeopardy (PPT o pizarra), mini-lectura impresa, ficha de autoevaluación.",
            "evaluacion": "Formativa — autoevaluación y observación de participación en actividades de revisión.",
            "sugerencia": None
        },
    ]
    return classes


def u2_classes(sp):
    """Unit 2: Technical Challenges & Global Issues — 8 classes, May–June"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        global_topic = "environmental impact of vehicles and the shift to electric cars"
        case2 = "<em>'The Electric Vehicle Revolution'</em> — How the automotive industry is changing: hybrid vs. electric vs. hydrogen cars."
        debate_topic = "Are electric cars better for the environment than traditional cars?"
        reading_eval = "A text about the comparison between combustion engines and electric motors — 8 questions (explicit + inferential)."
        tech_challenge = "reducing carbon emissions from vehicles"
        opinion_vocab = "pollution, emissions, sustainable, renewable, efficiency, carbon footprint"
    elif sp == "electricidad":
        global_topic = "renewable energy sources and the future of power generation"
        case2 = "<em>'Solar vs. Wind Energy'</em> — Comparing two renewable energy sources: installation, efficiency, cost, and environmental impact."
        debate_topic = "Should Chile invest more in solar or wind energy?"
        reading_eval = "A text about how solar panels work and their installation process — 8 questions (explicit + inferential)."
        tech_challenge = "transitioning from fossil fuels to clean energy"
        opinion_vocab = "solar panel, wind turbine, renewable, fossil fuel, grid, carbon neutral"
    elif sp == "electronica":
        global_topic = "electronic waste (e-waste) and its impact on the environment"
        case2 = "<em>'The E-Waste Crisis'</em> — What happens to old phones, computers, and electronics. Recycling vs. landfill."
        debate_topic = "Should companies be required to take back old electronics for recycling?"
        reading_eval = "A text about e-waste recycling processes and their challenges — 8 questions (explicit + inferential)."
        tech_challenge = "reducing electronic waste through better design and recycling"
        opinion_vocab = "e-waste, recycling, landfill, toxic, sustainable design, circular economy"
    elif sp == "grafica":
        global_topic = "the environmental impact of the printing industry and sustainable alternatives"
        case2 = "<em>'Green Printing'</em> — How the graphic industry is reducing waste: soy-based inks, recycled paper, digital alternatives."
        debate_topic = "Will digital media completely replace printed materials?"
        reading_eval = "A text about eco-friendly printing practices and their benefits — 8 questions (explicit + inferential)."
        tech_challenge = "reducing paper waste and chemical use in printing"
        opinion_vocab = "sustainable, eco-friendly, recycled, digital media, carbon footprint, soy-based ink"
    else:  # industrial
        global_topic = "automation and robotics in manufacturing: opportunities and challenges"
        case2 = "<em>'Robots in the Factory'</em> — How automation is changing industrial manufacturing: CNC machines, robotic welding, 3D printing."
        debate_topic = "Will robots replace industrial workers, or create new jobs?"
        reading_eval = "A text about CNC machines and their role in modern manufacturing — 8 questions (explicit + inferential)."
        tech_challenge = "balancing automation with employment in the manufacturing sector"
        opinion_vocab = "automation, robot, CNC, efficiency, unemployment, productivity"

    classes = [
        # Class 10
        {
            "title": f"Global Issues in {n}: Introduction",
            "oa": "OA3",
            "bloom": f"Identificar temas globales actuales relacionados con la especialidad de {n} a partir de un texto introductorio en inglés.",
            "inicio": f"""<ul>
                <li>Docente presenta el tema de la unidad: <em>"This unit connects your specialty with global issues: {global_topic}."</em></li>
                <li>Brainstorm: <em>"What global problems are connected to {n.lower()}?"</em> — Se recogen ideas en mapa conceptual en la pizarra.</li>
                <li>Vocabulario nuevo: {opinion_vocab} — presentación con imágenes y definiciones simples.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading introduction (20 min):</b> Texto adaptado (A2) sobre {global_topic}. Primera lectura silenciosa, luego lectura guiada con pausas para aclarar vocabulario.</li>
                <li><b>Comprehension (15 min):</b> Responder 6 preguntas: 3 de información explícita + 3 de opinión (<em>"Do you think this is a serious problem? Why?"</em>).</li>
                <li><b>Vocabulary in context (10 min):</b> Los estudiantes buscan las 6 palabras nuevas en el texto y escriben una oración propia con cada una.</li>
                <li><b>Discussion (15 min):</b> En parejas, los estudiantes comparten sus opiniones usando sentence starters: <em>"I think… because…", "In my opinion…", "I agree/disagree because…"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>3 estudiantes comparten su opinión con la clase.</li>
                <li>Introducción de expresiones de opinión para la unidad: <em>"I believe that…", "According to the text…", "On the other hand…"</em></li>
            </ul>""",
            "recursos": "Texto impreso sobre tema global del área, ficha de vocabulario, ficha de preguntas, pizarra.",
            "evaluacion": "Formativa — revisión de preguntas y observación de discusión oral.",
            "sugerencia": None
        },
        # Class 11
        {
            "title": "Case Study: " + (case2.split("'")[1] if "'" in case2 else "Technical Challenge"),
            "oa": "OA1 · OA3",
            "bloom": f"Analizar un estudio de caso sobre un desafío técnico global relacionado con {n}, identificando causas, consecuencias y posibles soluciones.",
            "inicio": f"""<ul>
                <li>Repaso rápido del vocabulario de la clase anterior con juego de definiciones (docente dice definición, estudiantes dicen la palabra).</li>
                <li>Pre-reading: Docente muestra 2-3 imágenes/estadísticas impactantes sobre {tech_challenge} y pregunta: <em>"What do these images tell us?"</em></li>
                <li>Se introducen conectores de causa-efecto: <em>"because", "as a result", "therefore", "so"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading the case study (25 min):</b> {case2} Texto de 1 página adaptado (A2). 
                    <ul>
                        <li>Lectura guiada con paradas para verificar comprensión.</li>
                        <li>Completar organizador gráfico: <b>Problem → Causes → Effects → Possible Solutions</b></li>
                    </ul>
                </li>
                <li><b>Group analysis (15 min):</b> En grupos de 3-4, responder: <em>"Which solution is the best? Why? What are the advantages and disadvantages?"</em> Cada grupo prepara 3 oraciones con conectores de causa-efecto.</li>
                <li><b>Oral report (15 min):</b> Cada grupo presenta sus conclusiones: <em>"We believe the best solution is… because… As a result…"</em></li>
                <li><b>Reflection writing (5 min):</b> Cada estudiante escribe 2 oraciones: <em>"I think the biggest challenge is… because…"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Docente sistematiza las ideas principales del caso de estudio.</li>
                <li>Pregunta de cierre: <em>"How does this global issue affect YOUR future career?"</em></li>
            </ul>""",
            "recursos": "Estudio de caso impreso, organizador gráfico, ficha de conectores, pizarra.",
            "evaluacion": "Formativa — revisión del organizador gráfico y evaluación de presentación grupal.",
            "sugerencia": "<b>Diferenciación:</b> Para estudiantes con mayor dificultad, proporcionar un glosario con las palabras clave del texto y oraciones modelo para completar."
        },
        # Class 12
        {
            "title": "Debate Preparation: Building Arguments",
            "oa": "OA3 · OA4",
            "bloom": f"Construir argumentos a favor y en contra sobre un tema técnico-ambiental relacionado con {n} utilizando expresiones de opinión en inglés.",
            "inicio": f"""<ul>
                <li>Docente presenta el tema del debate: <em>"{debate_topic}"</em></li>
                <li>Quick poll: los estudiantes votan a mano alzada (a favor / en contra / no sé). Se registra en la pizarra.</li>
                <li>Se enseñan expresiones para debatir: <em>"I strongly believe…", "On the other hand…", "However…", "For example…", "In conclusion…"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading for arguments (15 min):</b> Ficha con mini-textos (3-4 párrafos) presentando argumentos a favor y en contra. Los estudiantes los leen e identifican los puntos principales.</li>
                <li><b>Argument building (20 min):</b> La clase se divide en dos grupos (For / Against). Cada grupo genera 4-5 argumentos en inglés usando las expresiones de debate. Escriben en papelógrafo.</li>
                <li><b>Mini-debate (20 min):</b> Formato simple: un representante de cada lado presenta 2 argumentos (1 min c/u), luego réplica (30 seg c/u). Se repite con 2 parejas más de debatientes.</li>
                <li><b>Vote again (5 min):</b> Se repite la votación. <em>"Did anyone change their opinion? Why?"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Reflexión: el docente destaca los mejores argumentos de ambos lados.</li>
                <li>Se conecta con la evaluación de lectura: <em>"Next classes we'll read more about these issues and then have a reading test."</em></li>
            </ul>""",
            "recursos": "Ficha de argumentos (mini-textos), ficha de expresiones de debate, papelógrafo, marcadores, pizarra.",
            "evaluacion": "Formativa — observación de participación en debate y calidad de argumentos en inglés.",
            "sugerencia": "<b>Sugerencia:</b> Grabar el mini-debate para reproducirlo después y que los estudiantes identifiquen sus propias fortalezas y errores."
        },
        # Class 13
        {
            "title": "Reading Comprehension Practice for Evaluation",
            "oa": "OA1 · OA3",
            "bloom": f"Aplicar estrategias de lectura (skimming, scanning, inferencia) en textos técnicos sobre {n} como preparación para la evaluación de comprensión lectora.",
            "inicio": """<ul>
                <li>Docente repasa las estrategias de lectura trabajadas en la unidad: <em>skimming (idea general), scanning (información específica), inference (deducir significado), prediction</em>.</li>
                <li>Warm-up: <em>"What do you do BEFORE reading a text? WHILE reading? AFTER reading?"</em> — Se completa un cuadro de 3 columnas en la pizarra.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Practice text 1 (20 min):</b> Texto similar al formato de evaluación sobre un tema técnico del área. Los estudiantes aplican:
                    <ul>
                        <li>Skimming: <em>"What is the main idea?"</em> (2 min)</li>
                        <li>Scanning: <em>"Find 3 specific pieces of information"</em> (5 min)</li>
                        <li>6 preguntas de comprensión con respuestas escritas (13 min)</li>
                    </ul>
                </li>
                <li><b>Corrección colaborativa (10 min):</b> Se revisan las respuestas en conjunto, discutiendo cómo se encontró cada respuesta.</li>
                <li><b>Practice text 2 (20 min):</b> Segundo texto de práctica con formato similar a la evaluación. Los estudiantes trabajan de manera individual.</li>
                <li><b>Peer check (10 min):</b> Los estudiantes intercambian fichas y se corrigen mutuamente usando una pauta de respuestas.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Docente aclara dudas frecuentes y recuerda: <em>"The reading test is next class. Review your vocabulary and practice the strategies."</em></li>
                <li>Tips para la prueba: <em>"Read the questions first. Underline key words. Don't translate everything — focus on understanding the main idea."</em></li>
            </ul>""",
            "recursos": "2 textos de práctica impresos (formato similar a evaluación), fichas de preguntas, pauta de respuestas para corrección entre pares.",
            "evaluacion": "Formativa — revisión de ejercicios de práctica; diagnóstico de áreas débiles antes de la evaluación.",
            "sugerencia": None
        },
        # Class 14: READING EVALUATION (Nota 2)
        {
            "title": "EVALUACIÓN DE LECTURA — Nota 2 S1",
            "oa": "OA1 · OA3",
            "bloom": f"Demostrar comprensión de información central y específica en un texto técnico en inglés sobre {n} mediante una evaluación escrita.",
            "inicio": """<ul>
                <li>Docente organiza la sala en disposición de evaluación.</li>
                <li>Instrucciones claras: <em>"You have 60 minutes. Read carefully. Answer in English. You can underline the text."</em></li>
                <li>Repaso final de 2 minutos: <em>"Remember: read the questions first, then the text."</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Evaluación escrita (60 min):</b> {reading_eval}
                    <ul>
                        <li>Sección A: Verdadero/Falso con justificación (3 ítems — 9 pts)</li>
                        <li>Sección B: Preguntas de comprensión explícita (3 preguntas — 12 pts)</li>
                        <li>Sección C: Preguntas de inferencia y opinión (2 preguntas — 9 pts)</li>
                        <li>Total: 30 puntos — Exigencia 60%</li>
                    </ul>
                </li>
            </ol>""",
            "cierre": """<ul>
                <li>Recogida de evaluaciones. Retroalimentación inmediata: <em>"Was the text easy or difficult? Which part was the hardest?"</em></li>
                <li>Adelanto: <em>"Next class we'll review the test and continue preparing for the final evaluation."</em></li>
            </ul>""",
            "recursos": "Evaluación impresa (texto + preguntas), hojas de respuesta.",
            "evaluacion": f"<b>SUMATIVA — Nota 2 Semestre 1:</b> Prueba de comprensión lectora — texto técnico de {n}. 30 pts, 60% exigencia.",
            "sugerencia": "<b>Adecuación:</b> Para estudiantes con necesidades especiales, considerar tiempo extra (+15 min) y/o reducir el número de preguntas manteniendo la misma profundidad."
        },
        # Class 15
        {
            "title": "Test Review & Integrated Practice",
            "oa": "OA1 · OA3 · OA4",
            "bloom": f"Evaluar los resultados de la prueba de lectura para consolidar estrategias efectivas y corregir errores recurrentes en la comprensión de textos técnicos.",
            "inicio": """<ul>
                <li>Docente entrega las evaluaciones corregidas con retroalimentación escrita.</li>
                <li>Se presentan los resultados generales (sin nombres): <em>"The average score was… The strongest area was… We need to improve…"</em></li>
                <li>Los estudiantes revisan sus errores individualmente (5 min).</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Error analysis (15 min):</b> El docente trabaja con los errores más comunes en la pizarra, explicando las estrategias correctas para encontrar las respuestas.</li>
                <li><b>Vocabulary consolidation (15 min):</b> Juego <em>"Vocabulary Bingo"</em> con todas las palabras de las Unidades 1 y 2. Se consolidan términos técnicos y de opinión.</li>
                <li><b>Integrated practice (20 min):</b> Actividad que combina lectura + escritura + oralidad: los estudiantes leen un mini-texto nuevo (5 oraciones), escriben 3 preguntas sobre él, y luego hacen las preguntas a un compañero oralmente.</li>
                <li><b>Self-reflection (10 min):</b> Ficha de reflexión: <em>"What reading strategies work best for me? What vocabulary do I need to review? What is my goal for next semester?"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Docente introduce la evaluación integradora: <em>"Next class is our last evaluation for Semester 1: an integrated test."</em></li>
                <li>Se explica brevemente el formato: vocabulario + gramática + mini-lectura + escritura breve.</li>
            </ul>""",
            "recursos": "Evaluaciones corregidas, Bingo de vocabulario, mini-texto para actividad integradora, ficha de reflexión.",
            "evaluacion": "Formativa — análisis de errores y observación de práctica integrada.",
            "sugerencia": None
        },
        # Class 16: INTEGRATED EVALUATION (Nota 3)
        {
            "title": "EVALUACIÓN INTEGRADORA — Nota 3 S1",
            "oa": "OA1 · OA3 · OA4",
            "bloom": f"Demostrar dominio integrado de vocabulario, comprensión lectora y producción escrita en inglés técnico de {n} en una evaluación de cierre de semestre.",
            "inicio": """<ul>
                <li>Docente organiza la sala y da instrucciones: <em>"This is your final evaluation for Semester 1. You have 70 minutes."</em></li>
                <li>Se explican las secciones: vocabulario, gramática en contexto, mini-lectura, escritura breve.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Evaluación integradora (70 min):</b>
                    <ul>
                        <li><b>Sección A — Vocabulary (10 pts):</b> Asociar 10 términos técnicos con sus definiciones/imágenes.</li>
                        <li><b>Sección B — Grammar in context (10 pts):</b> Completar 5 oraciones con la forma verbal correcta (Simple Present, connectors, opinion expressions) en contexto técnico.</li>
                        <li><b>Sección C — Reading (15 pts):</b> Texto breve sobre un tema del área + 5 preguntas de comprensión.</li>
                        <li><b>Sección D — Writing (10 pts):</b> Escribir un párrafo de 6-8 oraciones: <em>"Describe a technical problem and its solution"</em> o <em>"Give your opinion about [global issue related to specialty]."</em></li>
                        <li>Total: 45 puntos — Exigencia 60%</li>
                    </ul>
                </li>
            </ol>""",
            "cierre": """<ul>
                <li>Recogida de evaluaciones. <em>"Congratulations on finishing Semester 1! Rest during the break and come back ready for more."</em></li>
                <li>Mensaje motivador sobre los logros del semestre.</li>
            </ul>""",
            "recursos": "Evaluación integradora impresa (4 secciones), hojas de respuesta.",
            "evaluacion": f"<b>SUMATIVA — Nota 3 Semestre 1:</b> Evaluación integradora (vocabulario + gramática + lectura + escritura). 45 pts, 60% exigencia.",
            "sugerencia": "<b>Cierre de Semestre:</b> Antes de las vacaciones de invierno, entregar notas y retroalimentación general al curso. Destacar los logros y áreas de mejora para el Semestre 2."
        },
    ]
    return classes


def u3_classes(sp):
    """Unit 3: Technical Communication & Workplace Language — 10 classes, July–Sept"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        reading_main = "a technical service report from an automotive workshop, including client complaint, diagnostic findings, and repair actions"
        instruction_text = "step-by-step instructions for performing an oil change and brake inspection"
        comm_scenario = "communicating with a client about vehicle problems and repair options"
        video_topic = "YouTube video: 'How to Explain Car Problems to Customers' (adapted, 5 min)"
        roleplay = "A mechanic explains to a client what's wrong with their car and what repairs are needed, including estimated time and cost."
        oral_eval_topic = "Explain a common automotive repair procedure to a client (choose one: oil change, brake replacement, battery check, tire rotation)"
    elif sp == "electricidad":
        reading_main = "a technical inspection report for a residential electrical installation, including findings and recommendations"
        instruction_text = "step-by-step instructions for installing a circuit breaker and testing a grounding system"
        comm_scenario = "communicating with a client about electrical safety issues and necessary upgrades"
        video_topic = "YouTube video: 'Electrical Safety for Beginners' (adapted, 5 min)"
        roleplay = "An electrician explains to a homeowner what electrical problems were found during inspection and what needs to be fixed."
        oral_eval_topic = "Explain a common electrical procedure to a client (choose one: panel inspection, circuit breaker installation, outlet replacement, safety test)"
    elif sp == "electronica":
        reading_main = "a technical repair report for an electronic device, including fault description, tests performed, and components replaced"
        instruction_text = "step-by-step instructions for assembling a basic circuit on a breadboard and testing with a multimeter"
        comm_scenario = "communicating with a client about device malfunction diagnosis and repair options"
        video_topic = "YouTube video: 'How to Diagnose Electronic Faults' (adapted, 5 min)"
        roleplay = "A technician explains to a client what's wrong with their device and whether it can be repaired or needs replacement."
        oral_eval_topic = "Explain a common electronics procedure (choose one: circuit assembly, soldering, device diagnosis, component testing)"
    elif sp == "grafica":
        reading_main = "a production order and quality control report for a printing job, including specifications, issues found, and corrective actions"
        instruction_text = "step-by-step instructions for preparing a digital file for offset printing and performing a color proof"
        comm_scenario = "communicating with a client about print specifications, deadlines, and quality issues"
        video_topic = "YouTube video: 'Understanding Color Management in Printing' (adapted, 5 min)"
        roleplay = "A print technician explains to a client why their colors look different from the screen and what options they have."
        oral_eval_topic = "Explain a common printing procedure to a client (choose one: file preparation, color proofing, press setup, binding process)"
    else:  # industrial
        reading_main = "a maintenance report for an industrial machine, including fault description, parts replaced, and preventive recommendations"
        instruction_text = "step-by-step instructions for operating a lathe safely and performing basic maintenance on a milling machine"
        comm_scenario = "communicating with a supervisor about machine problems and maintenance needs"
        video_topic = "YouTube video: 'CNC Machine Operation Basics' (adapted, 5 min)"
        roleplay = "A technician reports to a supervisor about a machine malfunction, describing the problem, the diagnostic steps taken, and the recommended solution."
        oral_eval_topic = "Explain a common industrial procedure (choose one: lathe operation, welding procedure, machine maintenance, quality inspection)"

    classes = [
        # Class 17: Return from break, Unit 3 intro
        {
            "title": f"Technical Communication in {n}: Introduction",
            "oa": "OA1",
            "bloom": f"Identificar los elementos clave de la comunicación técnica profesional en inglés dentro del contexto de {n}.",
            "inicio": """<ul>
                <li>Welcome back! Breve conversación en inglés: <em>"How were your holidays? What did you do?"</em> — 3-4 estudiantes comparten.</li>
                <li>Repaso del semestre 1: <em>"What do you remember from last semester? Tell me 3 things you learned."</em></li>
                <li>Presentación de la Unidad 3: <em>"This unit focuses on professional communication — how to read reports, follow instructions, and communicate with clients/supervisors in English."</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Vocabulary activation (15 min):</b> Repaso rápido de vocabulario del S1 con actividad <em>"Quick Fire"</em>: docente muestra imagen, estudiantes dicen la palabra en 3 segundos o pierden el turno.</li>
                <li><b>Reading introduction (25 min):</b> Lectura de {reading_main}. 
                    <ul>
                        <li>Pre-reading: identificar el tipo de texto (report), su propósito y audiencia.</li>
                        <li>Lectura guiada con pausas para aclarar vocabulario técnico nuevo.</li>
                        <li>Completar ficha: <em>What? (problem) / Who? (people involved) / When? / What was done?</em></li>
                    </ul>
                </li>
                <li><b>Discussion (15 min):</b> <em>"Have you seen reports like this in your workshop? What information do they include?"</em> Conversación grupal.</li>
                <li><b>Writing (5 min):</b> Los estudiantes escriben 2 oraciones sobre lo que aprendieron hoy.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Preview: <em>"Next class, we'll learn to follow technical instructions in English."</em></li>
                <li>Vocabulario para repasar en casa: 5 palabras clave del reporte leído.</li>
            </ul>""",
            "recursos": "Reporte técnico impreso (adaptado A2), ficha de análisis, pizarra, flashcards de repaso S1.",
            "evaluacion": "Formativa — observación de participación y revisión de ficha de análisis.",
            "sugerencia": None
        },
        # Class 18
        {
            "title": "Reading & Following Technical Instructions",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender y secuenciar instrucciones técnicas escritas en inglés para procedimientos de {n}.",
            "inicio": f"""<ul>
                <li>Warm-up: <em>"Do you follow instructions in English in your workshop? Where do they come from?"</em> (manuals, labels, websites).</li>
                <li>Se introduce vocabulario de instrucciones: <em>step, first, then, next, after that, finally, make sure, be careful, do not</em>.</li>
                <li>Docente modela: lee en voz alta una instrucción simple y la ejecuta (ej: <em>"First, open the box. Then, remove the component."</em>).</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading instructions (25 min):</b> Texto: {instruction_text}.
                    <ul>
                        <li>Primera lectura individual. Subrayar verbos de acción (imperativos).</li>
                        <li>Segunda lectura: numerar los pasos en orden.</li>
                        <li>Completar tabla: <b>Step Number → Action → Tool/Material Needed → Safety Note</b></li>
                    </ul>
                </li>
                <li><b>Sequencing activity (15 min):</b> Los pasos se entregan desordenados en tarjetas. En parejas, los estudiantes los ordenan correctamente y verifican con el texto original.</li>
                <li><b>Oral practice (15 min):</b> Un estudiante lee cada paso en voz alta mientras el compañero mima la acción. Luego cambian roles. Enfoque en pronunciación de imperativos.</li>
                <li><b>Writing (5 min):</b> Cada estudiante escribe 3 instrucciones simples para un procedimiento de su especialidad que no esté en el texto.</li>
            </ol>""",
            "cierre": """<ul>
                <li>2-3 estudiantes comparten sus instrucciones escritas. La clase verifica si son claras y correctas.</li>
                <li>Reflexión: <em>"Why is it important to understand instructions in English in your job?"</em></li>
            </ul>""",
            "recursos": "Texto de instrucciones técnicas impreso, tarjetas de pasos recortables, tabla de análisis, pizarra.",
            "evaluacion": "Formativa — revisión de tabla completada y observación de actividad oral.",
            "sugerencia": None
        },
        # Class 19
        {
            "title": "Video: Professional Communication at Work",
            "oa": "OA1 · OA4",
            "bloom": f"Comprender información específica de un video en inglés sobre comunicación profesional en {n} y aplicarla en interacciones orales.",
            "inicio": f"""<ul>
                <li>Pre-viewing: <em>"Imagine you need to explain a technical problem to someone who doesn't understand. How do you do it?"</em> Discusión breve.</li>
                <li>Se introducen expresiones de comunicación profesional: <em>"The problem is…", "I recommend…", "You should…", "It will take about…", "The cost is approximately…"</em></li>
                <li>Se entregan preguntas guía para el video.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Video viewing (15 min):</b> {video_topic}. Primera reproducción completa con subtítulos. Segunda reproducción por segmentos con pausas.</li>
                <li><b>Comprehension (10 min):</b> Responder preguntas guía sobre el video. Corrección grupal.</li>
                <li><b>Role-play preparation (15 min):</b> Se presenta el escenario: {comm_scenario}. En parejas, los estudiantes preparan un diálogo de 8-10 líneas usando las expresiones profesionales aprendidas.</li>
                <li><b>Role-play practice (15 min):</b> Las parejas practican su diálogo. El docente circula dando retroalimentación.</li>
                <li><b>Presentation (5 min):</b> 2 parejas presentan su diálogo frente al curso.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación grupal sobre los diálogos presentados.</li>
                <li>Vocabulario para repasar: expresiones de comunicación profesional.</li>
            </ul>""",
            "recursos": f"Video proyectado con subtítulos, ficha de preguntas guía, ficha de expresiones profesionales, pizarra.",
            "evaluacion": "Formativa — evaluación de role-play y comprensión del video.",
            "sugerencia": "<b>Sugerencia:</b> Grabar los role-plays para que los estudiantes se autoevalúen en la siguiente clase."
        },
        # Class 20
        {
            "title": f"Writing Technical Reports (Simplified)",
            "oa": "OA3 · OA4",
            "bloom": f"Producir un reporte técnico simplificado en inglés describiendo un problema y su solución en el área de {n}.",
            "inicio": """<ul>
                <li>Warm-up: Docente muestra un reporte técnico modelo en la pizarra/proyector y pregunta: <em>"What sections does it have? What information goes in each section?"</em></li>
                <li>Se presenta la estructura: <b>Date — Problem Description — Actions Taken — Result — Recommendation</b></li>
                <li>Se revisan expresiones útiles: <em>"The problem was…", "We checked/tested/replaced…", "As a result…", "We recommend…"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Model analysis (15 min):</b> Los estudiantes leen un reporte modelo completo y etiquetan cada sección. Identifican verbos en pasado simple (<em>checked, found, replaced</em>).</li>
                <li><b>Guided writing (25 min):</b> Cada estudiante escribe su propio reporte técnico basándose en un escenario dado por el docente (problema técnico del área). Se usa la estructura del modelo.</li>
                <li><b>Peer review (15 min):</b> Intercambian reportes con un compañero. Revisan usando checklist: <em>¿Tiene todas las secciones? ¿Usa vocabulario técnico? ¿Los verbos están en pasado? ¿Es claro?</em></li>
                <li><b>Revision (5 min):</b> Los estudiantes corrigen sus reportes basándose en la retroalimentación.</li>
            </ol>""",
            "cierre": """<ul>
                <li>2 estudiantes leen sus reportes. La clase evalúa si son claros y completos.</li>
                <li>Docente recoge los reportes para revisión y retroalimentación escrita.</li>
            </ul>""",
            "recursos": "Reporte modelo impreso/proyectado, ficha de estructura de reporte, escenario para escritura, checklist de revisión entre pares.",
            "evaluacion": "Formativa — revisión de reportes técnicos escritos por los estudiantes.",
            "sugerencia": None
        },
        # Class 21
        {
            "title": f"Role-Play Workshop: Professional Scenarios in {n}",
            "oa": "OA4",
            "bloom": f"Participar en interacciones orales simuladas en inglés representando escenarios profesionales de {n} con fluidez y vocabulario apropiado.",
            "inicio": f"""<ul>
                <li>Warm-up: Juego <em>"Telephone"</em> técnico — el docente susurra una instrucción técnica al primer estudiante, quien la pasa al siguiente. El último dice lo que entendió. Se compara con el original.</li>
                <li>Presentación del taller de role-play: <em>"Today you will practice real workplace conversations."</em></li>
                <li>Se repasan expresiones de las clases anteriores (problema, solución, recomendación, cortesía).</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Scenario cards (10 min):</b> Cada pareja recibe una tarjeta con un escenario profesional diferente. Ej: {roleplay}</li>
                <li><b>Preparation (15 min):</b> Las parejas preparan su diálogo (10-12 líneas). Pueden usar la ficha de expresiones como apoyo.</li>
                <li><b>Performance (25 min):</b> Cada pareja presenta su role-play al grupo (2-3 min). Los compañeros evalúan usando una ficha de observación: claridad, vocabulario, pronunciación, naturalidad.</li>
                <li><b>Feedback round (10 min):</b> Docente y compañeros dan retroalimentación positiva y constructiva a cada pareja.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Votación: <em>"Which role-play was the most realistic? The most creative?"</em></li>
                <li>Reflexión: <em>"How confident do you feel communicating in English at work?"</em> — escala del 1-5.</li>
            </ul>""",
            "recursos": "Tarjetas de escenarios impresas, ficha de expresiones profesionales, ficha de evaluación entre pares.",
            "evaluacion": "Formativa — observación de role-plays y evaluación de ficha entre pares.",
            "sugerencia": "<b>Sugerencia:</b> Usar los mejores role-plays como modelos para la preparación de la evaluación oral."
        },
        # Class 22
        {
            "title": "Reading: Case Study — Communication Failure",
            "oa": "OA1 · OA3",
            "bloom": f"Evaluar las consecuencias de una falla de comunicación técnica en un caso real de {n} e identificar soluciones alternativas.",
            "inicio": """<ul>
                <li>Docente presenta un caso breve: <em>"A technician didn't communicate a problem correctly. What do you think happened?"</em></li>
                <li>Activación de vocabulario: <em>misunderstanding, miscommunication, error, consequence, prevention</em>.</li>
                <li>Pregunta clave: <em>"Why is clear communication important in technical work?"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (20 min):</b> Case Study sobre una falla de comunicación en {n.lower()} que provocó un error costoso o peligroso. Texto adaptado A2 (1 página).
                    <ul>
                        <li>Lectura guiada con pausas para vocabulario.</li>
                        <li>Completar ficha: <b>What happened → Why → Consequences → How to prevent</b></li>
                    </ul>
                </li>
                <li><b>Critical discussion (15 min):</b> En grupos: <em>"Who was responsible? What should they have done differently? How could this be prevented?"</em></li>
                <li><b>Solution writing (15 min):</b> Cada grupo escribe 3 recomendaciones en inglés: <em>"To prevent this, they should…", "It is important to…", "Always make sure to…"</em></li>
                <li><b>Group sharing (10 min):</b> Cada grupo presenta sus recomendaciones. La clase vota por las mejores.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Síntesis: el docente conecta el caso con la importancia de saber comunicarse en inglés en el mundo laboral.</li>
                <li>Adelanto: <em>"Next class we prepare for your oral evaluation. Start thinking about which procedure you want to explain."</em></li>
            </ul>""",
            "recursos": "Caso de estudio impreso, ficha de análisis, papel para recomendaciones, pizarra.",
            "evaluacion": "Formativa — calidad del análisis y de las recomendaciones escritas.",
            "sugerencia": None
        },
        # Class 23: Oral eval preparation
        {
            "title": "Preparing the Oral Evaluation: Explaining a Procedure",
            "oa": "OA4",
            "bloom": f"Organizar y ensayar una explicación oral en inglés de un procedimiento técnico de {n} de manera clara y secuenciada.",
            "inicio": f"""<ul>
                <li>Docente presenta la evaluación oral (Nota 1 S2): <em>"{oral_eval_topic}"</em></li>
                <li>Criterios de evaluación: contenido técnico (5 pts), vocabulario (4 pts), pronunciación (4 pts), fluidez y coherencia (4 pts), uso de secuenciadores (3 pts). Total: 20 pts.</li>
                <li>Se muestra un modelo de explicación (el docente hace una demo de 2 min).</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Topic selection (5 min):</b> Cada estudiante elige el procedimiento que explicará.</li>
                <li><b>Planning (15 min):</b> Completar ficha de planificación:
                    <ul>
                        <li>Introduction: <em>"I will explain how to…"</em></li>
                        <li>Materials/tools needed</li>
                        <li>Steps (6-8 steps using First, Then, Next, After that, Finally)</li>
                        <li>Safety notes</li>
                        <li>Conclusion: <em>"This procedure is important because…"</em></li>
                    </ul>
                </li>
                <li><b>Script writing (15 min):</b> Escribir el guion de 10-15 oraciones. Docente circula apoyando.</li>
                <li><b>Peer rehearsal (20 min):</b> En parejas, practican la presentación. El compañero evalúa con checklist y da retroalimentación.</li>
                <li><b>Pronunciation drill (5 min):</b> Práctica grupal de palabras técnicas difíciles identificadas durante los ensayos.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Dudas finales. Recordatorio: <em>"Next class is the oral evaluation. Bring your notes but try to speak naturally, not read."</em></li>
                <li>Tips: <em>"Use your hands to show the steps. Speak slowly and clearly. Look at your audience."</em></li>
            </ul>""",
            "recursos": "Ficha de planificación, rúbrica impresa, checklist de retroalimentación entre pares, pizarra.",
            "evaluacion": "Preparación — no calificada. Revisión de borradores.",
            "sugerencia": "<b>Sugerencia:</b> Permitir que los estudiantes usen apoyo visual (imágenes de herramientas, diagramas del procedimiento) durante su presentación."
        },
        # Class 24: ORAL EVALUATION (Nota 1 S2)
        {
            "title": f"EVALUACIÓN ORAL — Nota 1 S2: Explaining a {n} Procedure",
            "oa": "OA4",
            "bloom": f"Producir una explicación oral clara y secuenciada en inglés de un procedimiento técnico de {n}.",
            "inicio": """<ul>
                <li>Docente recuerda criterios y estructura esperada.</li>
                <li>Warm-up grupal de pronunciación (2 min): palabras técnicas clave.</li>
                <li>Se establece el orden de presentaciones.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Presentaciones orales (60 min):</b> Cada estudiante presenta (2-3 min): {oral_eval_topic}
                    <ul>
                        <li>Docente evalúa con rúbrica de 5 criterios.</li>
                        <li>Compañeros completan ficha de peer feedback (1 fortaleza + 1 sugerencia).</li>
                    </ul>
                </li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación general del docente.</li>
                <li>Estudiantes entregan fichas de peer feedback.</li>
                <li>Reflexión: <em>"How do you feel about explaining technical procedures in English now vs. at the beginning of the year?"</em></li>
            </ul>""",
            "recursos": "Rúbrica de evaluación, fichas de peer feedback, cronómetro.",
            "evaluacion": "<b>SUMATIVA — Nota 1 Semestre 2:</b> Evaluación oral — Explicación de procedimiento técnico. 20 pts, 60% exigencia.",
            "sugerencia": "<b>Adaptación:</b> Para estudiantes con alta ansiedad, permitir presentar sentados, en formato de conversación con el docente, o en formato video grabado previamente."
        },
        # Class 25
        {
            "title": "Review & Vocabulary Consolidation",
            "oa": "OA1 · OA3",
            "bloom": f"Sintetizar el vocabulario y las estructuras de comunicación técnica profesional en inglés trabajados en la Unidad 3.",
            "inicio": """<ul>
                <li>Docente felicita por las evaluaciones orales y comparte observaciones generales positivas.</li>
                <li>Actividad: <em>"Word Wall"</em> — cada estudiante escribe una palabra/expresión clave de la Unidad 3 en un post-it y lo pega en la pared.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Vocabulary game (20 min):</b> <em>"Taboo"</em> con términos técnicos y de comunicación profesional. Un estudiante describe la palabra sin decirla, su equipo adivina.</li>
                <li><b>Mini reading (15 min):</b> Texto nuevo breve sobre comunicación profesional en {n.lower()}. Ejercicio rápido de comprensión (4 preguntas).</li>
                <li><b>Writing consolidation (15 min):</b> Cada estudiante escribe un mini-reporte técnico de 6-8 oraciones sobre un escenario nuevo (sin apoyo).</li>
                <li><b>Peer sharing (10 min):</b> Intercambian reportes y se dan retroalimentación mutua.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Autoevaluación: <em>"Rate your progress this unit: vocabulary (1-5), reading (1-5), speaking (1-5)."</em></li>
                <li>Preview de la Unidad 4: <em>"Next unit: Innovation and new trends in your field. Get ready!"</em></li>
            </ul>""",
            "recursos": "Post-its, fichas de Taboo, mini-texto impreso, ficha de autoevaluación.",
            "evaluacion": "Formativa — observación de participación y revisión de mini-reportes.",
            "sugerencia": None
        },
        # Class 26
        {
            "title": "Unit 3 Wrap-up & Transition",
            "oa": "OA1 · OA3 · OA4",
            "bloom": f"Reflexionar sobre los aprendizajes de comunicación técnica profesional adquiridos y su aplicabilidad en el campo laboral de {n}.",
            "inicio": """<ul>
                <li>Quick review: <em>"Name 3 things you learned in Unit 3."</em> — Round robin rápido, cada estudiante dice una cosa sin repetir.</li>
                <li>Docente entrega las rúbricas de la evaluación oral con retroalimentación individualizada.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Integrated activity (25 min):</b> <em>"Professional Portfolio Entry"</em>: Cada estudiante crea una entrada para un portafolio profesional en inglés que incluya:
                    <ul>
                        <li>Un párrafo de presentación personal (quién soy, qué estudio)</li>
                        <li>3 habilidades técnicas que puedo describir en inglés</li>
                        <li>1 procedimiento que puedo explicar en inglés</li>
                    </ul>
                </li>
                <li><b>Gallery walk (15 min):</b> Los portafolios se exhiben. Los estudiantes circulan, leen y dejan comentarios positivos en post-its.</li>
                <li><b>Class discussion (15 min):</b> <em>"How will English help you in your future job? What do you still need to learn?"</em> Discusión abierta.</li>
                <li><b>Goal setting (5 min):</b> Cada estudiante escribe 2 metas de aprendizaje para la Unidad 4.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Docente introduce la Unidad 4: <em>"Innovation, technology, and the future of {specialty}. We'll explore new trends and finish with a final project."</em></li>
                <li>Mensaje motivador sobre el progreso del grupo.</li>
            </ul>""".replace("{specialty}", n.lower()),
            "recursos": "Papel para portafolio, post-its para comentarios, rúbricas de evaluación oral, ficha de metas.",
            "evaluacion": "Formativa — revisión de entradas de portafolio y participación en discusión.",
            "sugerencia": "<b>Sugerencia:</b> Las entradas del portafolio pueden guardarse y complementarse en la Unidad 4 como parte del proyecto final."
        },
    ]
    return classes


def u4_classes(sp):
    """Unit 4: Innovation & Trends in [Specialty] — 10 classes, Oct–Dec"""
    S = SPECIALTIES[sp]
    n = S["name"]

    if sp == "automotriz":
        trend_topic = "electric vehicles, autonomous driving, and smart diagnostics"
        innovation_text = "<em>'The Rise of Electric Vehicles'</em> — How EVs work, their advantages, challenges, and the future of the automotive industry."
        case_final = "<em>'Tesla vs. Traditional Automakers'</em> — Comparing business models, technology, and market impact."
        project_theme = "Research and present an innovation in the automotive industry (EV technology, autonomous cars, hybrid systems, diagnostic AI, etc.)"
        video_final = "YouTube video: 'The Future of Cars — 2030' (adapted, 5 min)"
        debate_final = "Will autonomous vehicles replace human drivers within the next 20 years?"
    elif sp == "electricidad":
        trend_topic = "smart grids, renewable energy integration, and home automation"
        innovation_text = "<em>'Smart Grids and the Future of Electricity'</em> — How the power grid is becoming intelligent: renewable integration, demand response, and distributed generation."
        case_final = "<em>'Chile's Renewable Energy Boom'</em> — How Chile became a leader in solar energy and the challenges ahead."
        project_theme = "Research and present an innovation in the electrical field (smart grids, solar installation, wind energy, home automation, energy storage, etc.)"
        video_final = "YouTube video: 'How Smart Grids Work' (adapted, 5 min)"
        debate_final = "Can Chile become 100% renewable energy by 2050?"
    elif sp == "electronica":
        trend_topic = "IoT (Internet of Things), wearable technology, and smart home systems"
        innovation_text = "<em>'The Internet of Things Revolution'</em> — How everyday objects connect to the internet: smart homes, wearables, and industrial IoT."
        case_final = "<em>'Smart Homes: Convenience or Surveillance?'</em> — The benefits and privacy concerns of IoT devices."
        project_theme = "Research and present an electronics innovation (IoT device, wearable tech, smart home system, drone technology, AI chips, etc.)"
        video_final = "YouTube video: 'How IoT Works — Simply Explained' (adapted, 5 min)"
        debate_final = "Are smart home devices making our lives better or putting our privacy at risk?"
    elif sp == "grafica":
        trend_topic = "3D printing, augmented reality in design, and sustainable packaging"
        innovation_text = "<em>'3D Printing: The Next Revolution in Manufacturing'</em> — How 3D printing works, its applications, and how it's changing the graphic and manufacturing industries."
        case_final = "<em>'Print vs. Digital: Is the Paper Industry Dying?'</em> — The future of printed media in a digital world."
        project_theme = "Research and present an innovation in the graphic industry (3D printing, AR packaging, sustainable inks, digital textile printing, etc.)"
        video_final = "YouTube video: 'How 3D Printing Works' (adapted, 5 min)"
        debate_final = "Will 3D printing replace traditional manufacturing and printing methods?"
    else:  # industrial
        trend_topic = "Industry 4.0, robotic manufacturing, and additive manufacturing"
        innovation_text = "<em>'Industry 4.0: The Fourth Industrial Revolution'</em> — Smart factories, IoT in manufacturing, predictive maintenance, and collaborative robots."
        case_final = "<em>'Collaborative Robots (Cobots): Friend or Foe?'</em> — How cobots work alongside humans and the debate about job displacement."
        project_theme = "Research and present an innovation in industrial mechanics (cobots, CNC 5-axis, 3D metal printing, predictive maintenance, Industry 4.0, etc.)"
        video_final = "YouTube video: 'Industry 4.0 — Simply Explained' (adapted, 5 min)"
        debate_final = "Will Industry 4.0 create more jobs than it eliminates?"

    classes = [
        # Class 27
        {
            "title": f"New Trends in {n}: Introduction",
            "oa": "OA1",
            "bloom": f"Identificar tendencias tecnológicas actuales relacionadas con {n} a partir de un texto introductorio en inglés.",
            "inicio": f"""<ul>
                <li>Docente muestra 3-4 imágenes impactantes sobre innovaciones del área (ej: {trend_topic}) y pregunta: <em>"What do you see? What do you know about these technologies?"</em></li>
                <li>Brainstorm: <em>"What new technologies are changing {n.lower()}?"</em> — mapa conceptual en la pizarra.</li>
                <li>Vocabulario clave: <em>innovation, trend, technology, artificial intelligence, automation, sustainable, efficiency, future</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {innovation_text} Texto adaptado A2 (1 página).
                    <ul>
                        <li>Pre-reading: predicciones a partir del título e imágenes.</li>
                        <li>Lectura guiada con pausas para vocabulario nuevo.</li>
                        <li>Completar tabla: <b>Technology → How it works → Advantages → Challenges</b></li>
                    </ul>
                </li>
                <li><b>Comprehension (15 min):</b> 6 preguntas: 3 explícitas + 3 de opinión.</li>
                <li><b>Discussion (15 min):</b> En parejas: <em>"Which technology is the most interesting? Why? How will it affect your career?"</em> Usar sentence starters: <em>"I think… because…", "This technology is important because…"</em></li>
                <li><b>Vocabulary log (5 min):</b> Registrar 8 nuevas palabras con definición y oración propia.</li>
            </ol>""",
            "cierre": """<ul>
                <li>3 estudiantes comparten su opinión con la clase.</li>
                <li>Preview: <em>"This unit we will explore innovations, debate about them, and finish with your final project presentation."</em></li>
            </ul>""",
            "recursos": "Texto impreso sobre innovación del área, ficha de análisis, imágenes/fotos de innovaciones, pizarra.",
            "evaluacion": "Formativa — revisión de tabla de análisis y participación en discusión.",
            "sugerencia": None
        },
        # Class 28
        {
            "title": f"Video & Discussion: The Future of {n}",
            "oa": "OA1 · OA3",
            "bloom": f"Comprender un video en inglés sobre el futuro de {n} y expresar una postura crítica fundamentada sobre las tendencias presentadas.",
            "inicio": f"""<ul>
                <li>Warm-up: <em>"Imagine your job in 10 years. What will be different?"</em> — quick-write (3 min): escribir 3 predicciones.</li>
                <li>Pre-viewing: se entregan preguntas guía para el video.</li>
                <li>Vocabulario nuevo del video: 5 palabras clave presentadas con contexto.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Video (15 min):</b> {video_final} Primera reproducción completa; segunda por segmentos con pausas para preguntas.</li>
                <li><b>Comprehension (10 min):</b> Responder preguntas guía. Corrección en parejas.</li>
                <li><b>Critical discussion (20 min):</b> Mesa redonda guiada por el docente:
                    <ul>
                        <li><em>"Do you agree with the predictions in the video? Why/why not?"</em></li>
                        <li><em>"What opportunity does this create for technicians like you?"</em></li>
                        <li><em>"What skills will you need in the future?"</em></li>
                    </ul>
                    Expresiones: <em>"I agree/disagree because…", "On the other hand…", "I believe that…"</em>
                </li>
                <li><b>Written reflection (15 min):</b> Párrafo de 6-8 oraciones: <em>"My opinion about the future of {n.lower()}"</em> — usar vocabulario del video y expresiones de opinión.</li>
            </ol>""",
            "cierre": """<ul>
                <li>2-3 voluntarios leen sus párrafos. Retroalimentación positiva.</li>
                <li>Preview del caso de estudio de la próxima clase.</li>
            </ul>""",
            "recursos": "Video con subtítulos, ficha de preguntas guía, ficha de expresiones de opinión, cuaderno.",
            "evaluacion": "Formativa — observación de participación en discusión; revisión de párrafos reflexivos.",
            "sugerencia": None
        },
        # Class 29
        {
            "title": "Case Study: " + (case_final.split("'")[1] if "'" in case_final else "Innovation Analysis"),
            "oa": "OA1 · OA3",
            "bloom": f"Evaluar un estudio de caso sobre innovación en {n} comparando perspectivas diferentes y formulando una opinión fundamentada.",
            "inicio": """<ul>
                <li>Warm-up: <em>"What do you already know about this topic?"</em> — 2-3 estudiantes comparten.</li>
                <li>Vocabulario de comparación: <em>compared to, while, whereas, on the other hand, similarly, in contrast, advantage, disadvantage</em>.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Reading (25 min):</b> {case_final} Texto de 1 página (A2+).
                    <ul>
                        <li>Lectura guiada con pausas para aclarar vocabulario.</li>
                        <li>Completar tabla comparativa: <b>Aspect — Option A — Option B</b></li>
                    </ul>
                </li>
                <li><b>Group analysis (15 min):</b> Grupos de 3-4 discuten: <em>"Which option is better? What are the pros and cons?"</em> Preparan 3 argumentos.</li>
                <li><b>Presentations (15 min):</b> Cada grupo presenta sus argumentos usando vocabulario de comparación.</li>
                <li><b>Individual opinion (5 min):</b> Cada estudiante escribe: <em>"I prefer… because… However…"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Síntesis: el docente resume las diferentes posturas presentadas.</li>
                <li>Conexión con el proyecto final: <em>"You will research and present an innovation like this for your final project."</em></li>
            </ul>""",
            "recursos": "Caso de estudio impreso, ficha de tabla comparativa, fichas de vocabulario de comparación, pizarra.",
            "evaluacion": "Formativa — calidad de tabla comparativa y argumentos presentados.",
            "sugerencia": None
        },
        # Class 30
        {
            "title": f"Debate: {debate_final[:50]}...",
            "oa": "OA3 · OA4",
            "bloom": f"Construir y defender argumentos en inglés a favor y en contra de una tendencia tecnológica clave en {n}.",
            "inicio": f"""<ul>
                <li>Docente presenta el tema del debate: <em>"{debate_final}"</em></li>
                <li>Quick poll: a favor / en contra / no sé.</li>
                <li>Repaso de expresiones de debate: <em>"I strongly believe…", "The evidence shows…", "However, we must consider…", "In conclusion…"</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Preparation (15 min):</b> Clase dividida en dos equipos. Leen mini-textos con argumentos (a favor y en contra). Cada equipo construye 4-5 argumentos.</li>
                <li><b>Debate (30 min):</b> Formato estructurado:
                    <ul>
                        <li>Round 1: Equipo A presenta 2 argumentos (2 min). Equipo B responde (1 min).</li>
                        <li>Round 2: Equipo B presenta 2 argumentos (2 min). Equipo A responde (1 min).</li>
                        <li>Round 3: Libre — cualquier miembro puede dar un argumento o réplica.</li>
                        <li>Conclusiones: 1 representante por equipo resume (1 min c/u).</li>
                    </ul>
                </li>
                <li><b>Final vote (10 min):</b> Nueva votación. <em>"Did anyone change their opinion? Why?"</em> Discusión abierta.</li>
                <li><b>Reflection (5 min):</b> Escribir 2-3 oraciones: <em>"The best argument was… because…"</em></li>
            </ol>""",
            "cierre": """<ul>
                <li>Docente destaca los mejores argumentos y el uso del inglés durante el debate.</li>
                <li>Adelanto: <em>"Next classes: reading evaluation and then your final project."</em></li>
            </ul>""",
            "recursos": "Mini-textos con argumentos, ficha de expresiones de debate, pizarra, cronómetro.",
            "evaluacion": "Formativa — participación en debate, calidad de argumentos en inglés.",
            "sugerencia": None
        },
        # Class 31: Reading practice
        {
            "title": "Reading Practice for Final Evaluation",
            "oa": "OA1 · OA3",
            "bloom": f"Aplicar estrategias de lectura consolidadas en textos sobre innovación y tendencias en {n} como preparación para la evaluación final.",
            "inicio": """<ul>
                <li>Repaso de estrategias: <em>"What strategies do you use before, during, and after reading?"</em></li>
                <li>Tips para la evaluación: <em>"Read questions first. Underline key words. Use context clues for unknown words."</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Practice text (25 min):</b> Texto similar al formato de evaluación sobre una tendencia tecnológica del área. 6 preguntas de comprensión. Trabajo individual.</li>
                <li><b>Correction (10 min):</b> Revisión grupal — se analiza cómo encontrar cada respuesta.</li>
                <li><b>Second practice (20 min):</b> Segundo texto de práctica. Los estudiantes trabajan solos, cronometrados (simular condiciones de evaluación).</li>
                <li><b>Self-check (5 min):</b> Se entrega pauta de respuestas. Los estudiantes se autoevalúan.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Dudas finales. <em>"The reading test is next class. Review vocabulary from Units 3 and 4."</em></li>
                <li>Recordatorio del formato de evaluación.</li>
            </ul>""",
            "recursos": "2 textos de práctica impresos, fichas de preguntas, pauta de respuestas.",
            "evaluacion": "Formativa — práctica de evaluación.",
            "sugerencia": None
        },
        # Class 32: READING EVALUATION (Nota 2 S2)
        {
            "title": "EVALUACIÓN DE LECTURA — Nota 2 S2",
            "oa": "OA1 · OA3",
            "bloom": f"Demostrar comprensión de información central y específica en un texto sobre innovación y tendencias en {n}.",
            "inicio": """<ul>
                <li>Organización de la sala en disposición de evaluación.</li>
                <li>Instrucciones: <em>"You have 60 minutes. Read carefully. Answer in English."</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Evaluación escrita (60 min):</b> Texto sobre una innovación o tendencia tecnológica de {n.lower()} + 8 preguntas.
                    <ul>
                        <li>Sección A: Verdadero/Falso con justificación (3 ítems — 9 pts)</li>
                        <li>Sección B: Preguntas de comprensión explícita (3 preguntas — 12 pts)</li>
                        <li>Sección C: Preguntas de análisis y opinión (2 preguntas — 9 pts)</li>
                        <li>Total: 30 pts — 60% exigencia</li>
                    </ul>
                </li>
            </ol>""",
            "cierre": """<ul>
                <li>Recogida de evaluaciones.</li>
                <li><em>"Next classes: your final project. Start thinking about your topic!"</em></li>
            </ul>""",
            "recursos": "Evaluación impresa (texto + preguntas).",
            "evaluacion": "<b>SUMATIVA — Nota 2 Semestre 2:</b> Prueba de comprensión lectora — texto de innovación técnica. 30 pts, 60% exigencia.",
            "sugerencia": None
        },
        # Class 33: Final project preparation
        {
            "title": f"Final Project: Research & Planning",
            "oa": "OA3 · OA4",
            "bloom": f"Planificar una presentación oral sobre una innovación tecnológica en {n}, organizando la investigación y el guion en inglés.",
            "inicio": f"""<ul>
                <li>Docente presenta el proyecto final (Nota 3 S2): <em>"{project_theme}"</em></li>
                <li>Criterios: contenido e investigación (6 pts), vocabulario técnico (4 pts), pronunciación y fluidez (4 pts), apoyo visual (3 pts), estructura y coherencia (3 pts). Total: 20 pts.</li>
                <li>Se muestran ejemplos de presentaciones modelo.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Topic selection (10 min):</b> Cada estudiante elige su tema de innovación. El docente aprueba para asegurar variedad.</li>
                <li><b>Research (25 min):</b> Los estudiantes investigan su tema usando textos proporcionados por el docente y/o búsqueda guiada. Completan ficha:
                    <ul>
                        <li>What is the innovation?</li>
                        <li>How does it work?</li>
                        <li>What are the advantages and challenges?</li>
                        <li>How will it affect {n.lower()} professionals?</li>
                        <li>My opinion about this innovation</li>
                    </ul>
                </li>
                <li><b>Script drafting (20 min):</b> Escribir el guion de 12-15 oraciones. El docente circula apoyando con vocabulario y estructura.</li>
                <li><b>Visual support planning (5 min):</b> Planificar el apoyo visual (imágenes, diagrama, poster, PPT básico).</li>
            </ol>""",
            "cierre": """<ul>
                <li>Revisión rápida de avances: <em>"Who has their topic? Who has started their script?"</em></li>
                <li><em>"Next class: rehearsal and final preparation."</em></li>
            </ul>""",
            "recursos": "Ficha de investigación, textos/artículos de referencia sobre innovaciones del área, rúbrica del proyecto, acceso a computadores si es posible.",
            "evaluacion": "Preparación — el docente revisa avances y da retroalimentación.",
            "sugerencia": "<b>Sugerencia:</b> Si no hay acceso a computadores, preparar un set de mini-artículos impresos sobre diferentes innovaciones del área para que los estudiantes investiguen a partir de ellos."
        },
        # Class 34: Rehearsal
        {
            "title": "Final Project: Rehearsal & Peer Feedback",
            "oa": "OA4",
            "bloom": f"Ensayar y perfeccionar la presentación oral del proyecto final sobre innovación en {n} incorporando retroalimentación de pares.",
            "inicio": """<ul>
                <li>Estado de avance: <em>"How is your project going? Any questions?"</em> El docente resuelve dudas comunes.</li>
                <li>Tips finales de presentación: <em>"Eye contact, clear voice, use your visual aid, don't read — speak."</em></li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Final script revision (15 min):</b> Los estudiantes completan y pulen su guion. El docente revisa los guiones pendientes.</li>
                <li><b>Peer rehearsal round 1 (20 min):</b> En parejas, practican la presentación completa. El compañero evalúa con la rúbrica y da retroalimentación específica.</li>
                <li><b>Adjustments (10 min):</b> Los estudiantes incorporan la retroalimentación recibida.</li>
                <li><b>Peer rehearsal round 2 (15 min):</b> Con una pareja diferente. Segunda ronda de retroalimentación.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Pronunciation practice grupal: palabras técnicas difíciles identificadas durante los ensayos.</li>
                <li>Recordatorio: <em>"Next class is your FINAL presentation. Bring your visual support. Be ready!"</em></li>
            </ul>""",
            "recursos": "Guiones de los estudiantes, rúbrica, checklist de retroalimentación entre pares, material visual de los estudiantes.",
            "evaluacion": "Preparación — el docente da retroalimentación final individual.",
            "sugerencia": None
        },
        # Class 35: FINAL PROJECT PRESENTATIONS (Nota 3 S2)
        {
            "title": f"PROYECTO FINAL — Nota 3 S2: Innovation in {n}",
            "oa": "OA3 · OA4",
            "bloom": f"Producir una presentación oral fundamentada en inglés sobre una innovación tecnológica en {n}, demostrando investigación, vocabulario técnico y postura crítica.",
            "inicio": """<ul>
                <li>Docente recuerda criterios y estructura.</li>
                <li>Se establece el orden de presentaciones.</li>
                <li>Normas de audiencia: escuchar, tomar notas, respetar.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Presentaciones (60 min):</b> Cada estudiante presenta (3-4 min): {project_theme}
                    <ul>
                        <li>Docente evalúa con rúbrica de 5 criterios (20 pts).</li>
                        <li>Compañeros completan ficha de peer feedback.</li>
                        <li>Después de cada presentación, 1-2 preguntas del público.</li>
                    </ul>
                </li>
            </ol>""",
            "cierre": """<ul>
                <li>Retroalimentación general: logros del grupo, aspectos destacados.</li>
                <li>Entrega de fichas de peer feedback.</li>
            </ul>""",
            "recursos": "Rúbrica, fichas de peer feedback, proyector para apoyo visual, cronómetro.",
            "evaluacion": "<b>SUMATIVA — Nota 3 Semestre 2:</b> Proyecto final — Presentación oral sobre innovación técnica. 20 pts, 60% exigencia.",
            "sugerencia": "<b>Nota:</b> Si no alcanzan todas las presentaciones en esta clase, continuar en la siguiente."
        },
        # Class 36: Closure
        {
            "title": "Year-End Review & Closure",
            "oa": "OA1 · OA3 · OA4",
            "bloom": f"Sintetizar y reflexionar sobre los aprendizajes del año en inglés técnico de {n}, evaluando el progreso personal y las metas alcanzadas.",
            "inicio": """<ul>
                <li>Si quedan presentaciones pendientes, se completan primero.</li>
                <li>Docente entrega rúbricas del proyecto final y notas del semestre.</li>
                <li>Actividad de memoria: <em>"What is your best memory from English class this year?"</em> — round robin.</li>
            </ul>""",
            "desarrollo": f"""<ol>
                <li><b>Year review game (20 min):</b> <em>"The Big Quiz"</em> — equipos compiten respondiendo preguntas de vocabulario, gramática, lectura y conocimiento técnico de todo el año.</li>
                <li><b>Reflection writing (15 min):</b> Cada estudiante escribe un párrafo en inglés: <em>"This year I learned… My biggest achievement was… I need to improve… English will help me in my career because…"</em></li>
                <li><b>Sharing circle (15 min):</b> Voluntarios leen sus reflexiones. El grupo aplaude cada contribución.</li>
                <li><b>Final self-assessment (10 min):</b> Ficha: <em>"At the beginning of the year I could… Now I can…"</em> — comparar con la evaluación diagnóstica del inicio.</li>
            </ol>""",
            "cierre": """<ul>
                <li>Mensaje de cierre del docente: valoración del esfuerzo y los logros del curso.</li>
                <li><em>"Remember: English is a lifelong tool. Keep practicing. I'm proud of your progress."</em></li>
                <li>Despedida y buenos deseos para el futuro.</li>
            </ul>""",
            "recursos": "Quiz en PPT/pizarra, ficha de reflexión, ficha de autoevaluación, rúbricas y notas.",
            "evaluacion": "Formativa — reflexión escrita y autoevaluación de cierre.",
            "sugerencia": "<b>Sugerencia:</b> Crear un certificado simbólico de 'Technical English Communicator' para cada estudiante como reconocimiento de su esfuerzo durante el año."
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

    # OA by unit
    oa_map = {
        1: ["OA1: Comprender información central de textos orales y escritos en contextos de interés.",
            "OA4: Producir y comprender con fluidez textos orales y escritos breves y claros."],
        2: ["OA1: Comprender información central de textos orales y escritos.",
            "OA3: Utilizar su conocimiento del inglés para construir postura personal crítica.",
            "OA4: Producir y comprender con fluidez textos orales y escritos."],
        3: ["OA1: Comprender información central de textos orales y escritos.",
            "OA3: Utilizar su conocimiento del inglés para construir postura personal crítica.",
            "OA4: Producir y comprender con fluidez textos orales y escritos."],
        4: ["OA1: Comprender información central de textos orales y escritos.",
            "OA3: Utilizar su conocimiento del inglés para construir postura personal crítica.",
            "OA4: Producir y comprender con fluidez textos orales y escritos."],
    }

    # Build eval summary
    eval_map = {
        1: f"""<ul>
            <li>Clase {class_start + 6}: <b>Nota 1 S1</b> — Presentación oral: describir habilidades técnicas en {n}. 20 pts.</li>
        </ul>""",
        2: f"""<ul>
            <li>Clase {class_start + 4}: <b>Nota 2 S1</b> — Prueba de comprensión lectora: texto técnico-global. 30 pts.</li>
            <li>Clase {class_start + 6}: <b>Nota 3 S1</b> — Evaluación integradora semestral. 45 pts.</li>
        </ul>""",
        3: f"""<ul>
            <li>Clase {class_start + 7}: <b>Nota 1 S2</b> — Evaluación oral: explicar un procedimiento técnico. 20 pts.</li>
        </ul>""",
        4: f"""<ul>
            <li>Clase {class_start + 5}: <b>Nota 2 S2</b> — Prueba de comprensión lectora: texto de innovación. 30 pts.</li>
            <li>Clase {class_start + 8}: <b>Nota 3 S2</b> — Proyecto final: presentación de innovación tecnológica. 20 pts.</li>
        </ul>"""
    }

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3° Medio {n} - Unidad {unit_num}: {unit_title}</title>
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
    <h1>PLANIFICACIÓN CLASE A CLASE — 3° MEDIO — {n.upper()}</h1>
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
                <strong>OA Basales trabajados (3° Medio):</strong>
                <ul>
                    {"".join(f'<li><b>{oa.split(":")[0]}:</b>{oa.split(":")[1]}</li>' for oa in oa_map[unit_num])}
                </ul>
            </div>
            <div class="overview-item">
                <strong>Evaluaciones de la unidad:</strong>
                {eval_map[unit_num]}
            </div>
            <div class="overview-item">
                <strong>Habilidades priorizadas:</strong>
                <ul>
                    <li><b>Lectura:</b> Textos técnicos, estudios de caso, reportes e instrucciones de {n.lower()}.</li>
                    <li><b>Expresión Oral:</b> Descripciones, explicaciones de procedimientos, debates y presentaciones.</li>
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
        is_eval = "EVALUACIÓN" in cls["title"] or "PROYECTO FINAL" in cls["title"]
        eval_class = ' evaluacion' if is_eval else ""
        header_class = "eval" if is_eval else "normal"

        # Badges
        oa_badges = "".join(f'<span class="badge badge-oa">{oa.strip()}</span> ' for oa in cls["oa"].split("·"))
        eval_badge = '<span class="badge badge-eval">EVALUACIÓN</span>' if is_eval else ""

        # Sugerencia
        sug_html = ""
        if cls.get("sugerencia"):
            sug_html = f'<div class="sugerencia"><strong>💡 Sugerencia:</strong> {cls["sugerencia"]}</div>'

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
        <p>Planificación elaborada para Liceo Técnico Profesional — Inglés 3° Medio — Especialidad: {n} — 2026</p>
        <p>Basada en OA de Bases Curriculares 3° Medio (Decreto N°193/2019) y Programa de Estudio (Decreto N°496/2020)</p>
    </div>
</div>
</body>
</html>
"""
    return html


# =============== MAIN ===============

def adapt_classes_for_unit(classes_data, target_classes, optional_last_for_thursday=False):
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
        adjusted = [item for _, item in sorted(indexed, key=lambda x: x[0])][:target_classes]
    elif len(adjusted) < target_classes:
        for extra_idx in range(len(adjusted) + 1, target_classes + 1):
            adjusted.append({
                "title": f"Consolidation & Reinforcement Workshop {extra_idx}",
                "oa": "OA1 · OA4",
                "bloom": "Consolidar aprendizajes de la unidad mediante actividades integradas de lectura técnica, producción oral y reflexión metacognitiva.",
                "inicio": "<ul><li>Activación breve de aprendizajes previos con preguntas guiadas de repaso.</li><li>Recordatorio de objetivos y criterios de desempeño esperados.</li></ul>",
                "desarrollo": "<ol><li><b>Repaso guiado:</b> lectura breve y extracción de ideas clave.</li><li><b>Aplicación práctica:</b> actividad colaborativa de resolución de tarea técnica en inglés.</li><li><b>Producción oral:</b> socialización de resultados con retroalimentación del docente.</li></ol>",
                "cierre": "<ul><li>Síntesis de aprendizajes de la sesión.</li><li>Autoevaluación rápida: fortalezas y aspectos a mejorar.</li></ul>",
                "recursos": "Guías de repaso, material de lectura breve, pizarra y recursos multimodales.",
                "evaluacion": "Formativa — evidencia de consolidación y participación activa.",
                "sugerencia": None,
            })

    if optional_last_for_thursday and adjusted:
        optional_idx = None
        for idx in range(len(adjusted) - 1, -1, -1):
            if not is_eval_class(adjusted[idx]):
                optional_idx = idx
                break
        if optional_idx is not None:
            adjusted[optional_idx]["title"] = f"{adjusted[optional_idx]['title']} (Sesión opcional para cursos con clase los jueves)"
            adjusted[optional_idx]["sugerencia"] = "Aplicar esta sesión como extensión para cursos de miércoles o convertirla en actividad de recuperación si el patrón horario es jueves."

    return adjusted

UNITS = [
    {
        "num": 1,
        "title": "Technical Skills & Career Paths",
        "classes_fn": u1_classes,
        "target_classes": 9,
        "date_range": "4 marzo – 3 mayo (9 sesiones efectivas)",
        "class_range": (1, 9),
        "semester": "Semestre 1",
        "focus": "Vocabulario técnico, lectura de perfiles laborales y presentación oral de habilidades"
    },
    {
        "num": 2,
        "title": "Technical Challenges & Global Issues",
        "classes_fn": u2_classes,
        "target_classes": 7,
        "optional_last_for_thursday": True,
        "date_range": "4 mayo – 21 junio (7 sesiones; 1 opcional para patrón jueves)",
        "class_range": (10, 16),
        "semester": "Semestre 1",
        "focus": "Lectura de estudios de caso globales, debate y evaluación integradora"
    },
    {
        "num": 3,
        "title": "Technical Communication & Professional Language",
        "classes_fn": u3_classes,
        "target_classes": 10,
        "optional_last_for_thursday": True,
        "date_range": "6 julio – 20 septiembre (10 sesiones; 1 opcional para patrón jueves; sin clases 14–20 sept.)",
        "class_range": (17, 26),
        "semester": "Semestre 2",
        "focus": "Reportes técnicos, instrucciones, comunicación profesional y role-play"
    },
    {
        "num": 4,
        "title": "Innovation & New Trends",
        "classes_fn": u4_classes,
        "target_classes": 12,
        "date_range": "21 septiembre – 12 diciembre (12 sesiones)",
        "class_range": (27, 38),
        "semester": "Semestre 2",
        "focus": "Tendencias tecnológicas, debate, proyecto final de investigación"
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
        classes_data = adapt_classes_for_unit(
            classes_data,
            target_classes=unit["target_classes"],
            optional_last_for_thursday=unit.get("optional_last_for_thursday", False),
        )

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
        print(f"✓ Created: 3ro Medio/Unidad {unit['num']}/{filename}")

print(f"\n✅ {count} archivos generados exitosamente para 3° Medio")
