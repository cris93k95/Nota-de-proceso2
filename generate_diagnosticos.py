#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generates 11 diagnostic PDF tests in KET Reading format.
- 1 for 1ro Medio (mixed)
- 5 for 3ro Medio (one per specialty)
- 5 for 4to Medio (one per specialty)
Each test: 30 questions across 5 parts.
"""
import os, glob
from fpdf import FPDF

BASE = r"c:\Users\crist\OneDrive\Escritorio\2026"

# Find images dynamically to avoid encoding issues
_logos = glob.glob(os.path.join(BASE, "Logo Colegio*.png"))
_cuadros = glob.glob(os.path.join(BASE, "Cuadro Encabezado*.png"))
LOGO = _logos[0] if _logos else ""
CUADRO = _cuadros[0] if _cuadros else ""
OUT_DIR = os.path.join(BASE, "Pruebas Diagnostico")


# ========== TEST CONTENT DATA ==========

def get_1ro_medio_content():
    return {
        "level": "1ro Medio",
        "specialty": "",
        "filename": "diagnostico_1ro_medio.pdf",
        "part1": {
            "instructions": "Questions 1-6\nWhich notice (A, B or C) says this?\nFor each question, choose the correct letter.",
            "questions": [
                {
                    "q": "1. You cannot use this entrance today.",
                    "options": [
                        "A) PUSH - Do not pull this door",
                        "B) MAIN ENTRANCE CLOSED - Please use side door",
                        "C) OPEN 24 HOURS - Come in anytime"
                    ]
                },
                {
                    "q": "2. You can buy things here for less money.",
                    "options": [
                        "A) NO REFUNDS on sale items",
                        "B) SPECIAL OFFER - 50% OFF all items this week",
                        "C) NEW PRODUCTS arriving next Monday"
                    ]
                },
                {
                    "q": "3. Be careful when you walk here.",
                    "options": [
                        "A) CAUTION - Wet floor",
                        "B) EXIT - Please close the door",
                        "C) WELCOME - Please take a seat"
                    ]
                },
                {
                    "q": "4. You must wear something on your head in this area.",
                    "options": [
                        "A) SAFETY GLASSES required at all times",
                        "B) HARD HAT AREA - No entry without helmet",
                        "C) KEEP THIS AREA CLEAN"
                    ]
                },
                {
                    "q": "5. This place is not open on Sundays.",
                    "options": [
                        "A) OPENING HOURS: Mon-Sat 9am-6pm",
                        "B) OPEN EVERY DAY from 8am to 9pm",
                        "C) CLOSED FOR HOLIDAYS - Back January 3rd"
                    ]
                },
                {
                    "q": "6. Students can get food here.",
                    "options": [
                        "A) LIBRARY - Silence please",
                        "B) SCHOOL CAFETERIA - Lunch 12:30 - 1:30 pm",
                        "C) COMPUTER LAB - No food or drinks"
                    ]
                },
            ]
        },
        "part2": {
            "instructions": "Questions 7-13\nRead the text below about three students at a technical school.\nFor each question, choose the correct answer (A, B or C).",
            "text": "Pedro, Ana and Miguel are students at a technical school in Chile.\n\nPedro is 15 years old and he is in first year. He likes working with his hands. His favourite subject is the workshop class where he learns to use tools. He wants to be a mechanic in the future. After school, he usually helps his father fix things at home. He thinks English is important because many car manuals are in English.\n\nAna is also 15 and in the same school. She is very good with computers and technology. She enjoys learning about circuits and electronics. In her free time, she watches YouTube videos about how to build robots. She says English helps her understand the videos and read instructions online.\n\nMiguel is 16 years old. He loves drawing and design. He is interested in graphic design and printing. He spends a lot of time using design software on his computer. He wants to work in advertising when he finishes school. He reads many design blogs and most of them are in English.",
            "questions": [
                {"q": "7. Who wants to work with cars?", "options": ["A) Pedro", "B) Ana", "C) Miguel"]},
                {"q": "8. Who watches videos about building robots?", "options": ["A) Pedro", "B) Ana", "C) Miguel"]},
                {"q": "9. Who is older than the other two?", "options": ["A) Pedro", "B) Ana", "C) Miguel"]},
                {"q": "10. Who likes using design software?", "options": ["A) Pedro", "B) Ana", "C) Miguel"]},
                {"q": "11. Who helps fix things at home?", "options": ["A) Pedro", "B) Ana", "C) Miguel"]},
                {"q": "12. Who reads blogs in English?", "options": ["A) Pedro", "B) Ana", "C) Miguel"]},
                {"q": "13. Who thinks English is important for reading manuals?", "options": ["A) Pedro", "B) Ana", "C) Miguel"]},
            ]
        },
        "part3": {
            "instructions": "Questions 14-18\nRead the text below and choose the correct answer (A, B or C) for each question.",
            "text": "My name is Carlos Munoz and I am a mechanic. I work at a small workshop in Santiago. I started learning about cars when I was a student at a technical school, just like you.\n\nEvery day, I arrive at work at 8:00 in the morning. First, I put on my safety clothes: gloves, glasses and special shoes. Then I check which cars need to be repaired. I usually fix about three or four cars a day.\n\nThe most common problems are brakes, engines and electrical systems. I use many tools, like wrenches, screwdrivers and diagnostic scanners. Some of the newer scanners have instructions only in English, so I need to understand basic English to use them.\n\nI love my job because every day is different. Sometimes I work on old cars, sometimes on new ones. The best part is when a customer is happy because their car works perfectly again.\n\nMy advice for students is: study hard, learn English, and always follow safety rules in the workshop. These three things will help you have a great career.",
            "questions": [
                {"q": "14. What does Carlos do first when he arrives at work?",
                 "options": ["A) He checks which cars need to be repaired.", "B) He puts on his safety clothes.", "C) He fixes the first car."]},
                {"q": "15. How many cars does Carlos usually fix in a day?",
                 "options": ["A) One or two", "B) Three or four", "C) Five or six"]},
                {"q": "16. Why does Carlos need to understand English?",
                 "options": ["A) Because his customers speak English.", "B) Because some tool instructions are only in English.", "C) Because he wants to work in another country."]},
                {"q": "17. What does Carlos like about his job?",
                 "options": ["A) He earns a lot of money.", "B) He works only in the morning.", "C) Every day is different."]},
                {"q": "18. What is Carlos's advice for students?",
                 "options": ["A) Study hard, learn English, and follow safety rules.", "B) Work with old cars because they are easier.", "C) Use only new tools and scanners."]},
            ]
        },
        "part4": {
            "instructions": "Questions 19-24\nRead the text below and choose the correct word (A, B or C) for each space.",
            "text_before": "A Day at the Workshop",
            "sentences": [
                {"pre": "Every morning, the students arrive at the workshop and (19) _____ their safety equipment.",
                 "options": ["A) put on", "B) take off", "C) look at"]},
                {"pre": "The teacher (20) _____ them which tools they will need for the day.",
                 "options": ["A) asks", "B) tells", "C) gives"]},
                {"pre": "First, they (21) _____ the names of different tools in English and Spanish.",
                 "options": ["A) learn", "B) teach", "C) forget"]},
                {"pre": "Then, they start working (22) _____ pairs on their projects.",
                 "options": ["A) at", "B) on", "C) in"]},
                {"pre": "At the end of the class, they must (23) _____ all the tools and clean the area.",
                 "options": ["A) return", "B) break", "C) buy"]},
                {"pre": "The workshop class is the (24) _____ popular class in the school because students love practical work.",
                 "options": ["A) less", "B) more", "C) most"]},
            ]
        },
        "part5": {
            "instructions": "Questions 25-30\nRead the text below and write the missing word for each space.\nUse only ONE word for each space.",
            "sentences": [
                {"text": "25. A mechanic _____ tools to fix cars.", "hint": "(uses / needs)"},
                {"text": "26. Students must wear safety glasses to protect their _____.", "hint": "(eyes)"},
                {"text": "27. The workshop is _____ the first floor of the school.", "hint": "(on)"},
                {"text": "28. English _____ an important language for technical professionals.", "hint": "(is)"},
                {"text": "29. _____ you speak English? - A little.", "hint": "(Do / Can)"},
                {"text": "30. The students work in groups _____ three.", "hint": "(of)"},
            ]
        }
    }


def get_3ro_content(specialty):
    sp_data = {
        "automotriz": {
            "name": "Mecanica Automotriz",
            "part1_questions": [
                {"q": "1. You must not start this machine without permission.",
                 "options": ["A) WARNING: Authorized personnel only - Do not operate without supervisor approval",
                             "B) PARKING AREA - For staff vehicles only",
                             "C) OPEN - Workshop hours 8am to 5pm"]},
                {"q": "2. Your car is ready to pick up.",
                 "options": ["A) LEAVE YOUR KEYS at the reception desk",
                             "B) VEHICLE READY FOR COLLECTION - Please bring your receipt",
                             "C) CARS MUST BE PARKED in designated areas only"]},
                {"q": "3. You need to protect your hands here.",
                 "options": ["A) SAFETY GLOVES REQUIRED in this work area",
                             "B) KEEP HANDS AWAY from moving parts",
                             "C) WASH YOUR HANDS before leaving the workshop"]},
                {"q": "4. This product could be dangerous if you touch it.",
                 "options": ["A) HANDLE WITH CARE - Fragile parts inside",
                             "B) HAZARDOUS MATERIAL - Avoid skin contact with coolant",
                             "C) STORE IN A COOL PLACE - Keep away from sunlight"]},
                {"q": "5. You can learn new skills at this event.",
                 "options": ["A) WORKSHOP CLOSED for maintenance this weekend",
                             "B) AUTOMOTIVE TRAINING COURSE - Register now, limited spaces",
                             "C) NO FOOD OR DRINKS allowed in the workshop"]},
                {"q": "6. Vehicles must not go faster than this speed.",
                 "options": ["A) SPEED LIMIT 20 KM/H inside the workshop area",
                             "B) PARKING - Maximum 2 hours",
                             "C) FUEL STATION - Open 24 hours"]},
            ],
            "part2_text": "Rodrigo, Sofia and Tomas are all studying automotive mechanics.\n\nRodrigo has been working part-time at his uncle's repair shop since last year. He is very good at finding problems in engines. He can already use a basic diagnostic scanner, but he wants to learn more about electronic fuel injection systems. He reads English car forums to find solutions to difficult problems.\n\nSofia is the only girl in her class, but she is one of the best students. She is very interested in electric vehicles and hybrid technology. She watches English YouTube channels about Tesla and other electric car companies. Her dream is to work at an electric vehicle service centre.\n\nTomas prefers working with his hands rather than reading. He is excellent at brake repairs and suspension work. He learned most of his skills from his grandfather, who was also a mechanic. He finds English difficult, but he knows he needs it to read the technical manuals for newer cars.",
            "part2_questions": [
                {"q": "7. Who already has experience working in a real workshop?", "options": ["A) Rodrigo", "B) Sofia", "C) Tomas"]},
                {"q": "8. Who is interested in electric cars?", "options": ["A) Rodrigo", "B) Sofia", "C) Tomas"]},
                {"q": "9. Who learned mechanical skills from a family member?", "options": ["A) Rodrigo", "B) Sofia", "C) Tomas"]},
                {"q": "10. Who reads online forums in English?", "options": ["A) Rodrigo", "B) Sofia", "C) Tomas"]},
                {"q": "11. Who is very good at brake repairs?", "options": ["A) Rodrigo", "B) Sofia", "C) Tomas"]},
                {"q": "12. Who wants to work with electric vehicles?", "options": ["A) Rodrigo", "B) Sofia", "C) Tomas"]},
                {"q": "13. Who finds English difficult?", "options": ["A) Rodrigo", "B) Sofia", "C) Tomas"]},
            ],
            "part3_text": "Engine Oil: Why It Matters\n\nEngine oil is one of the most important fluids in any vehicle. It has several functions: it lubricates the moving parts inside the engine, it helps cool the engine, and it keeps the engine clean by collecting dirt and small particles.\n\nThere are different types of engine oil. The most common are mineral oil, semi-synthetic oil, and fully synthetic oil. Synthetic oil is more expensive, but it lasts longer and protects the engine better, especially in extreme temperatures.\n\nEvery car has a recommended oil change interval. Most modern cars need an oil change every 10,000 to 15,000 kilometres, but older cars may need it more frequently - every 5,000 kilometres. If you do not change the oil on time, the engine can overheat and parts can wear out faster.\n\nTo check the oil level, you use the dipstick. The oil should be between the minimum and maximum marks. If the oil is very dark or smells burnt, it needs to be changed. A good mechanic always checks the oil as part of a routine inspection.\n\nCar owners often ask mechanics: \"What oil should I use?\" The answer depends on the car model, the climate, and how the car is used. The owner's manual always has this information, usually in English for imported cars.",
            "part3_questions": [
                {"q": "14. What is one function of engine oil?",
                 "options": ["A) It makes the car go faster.", "B) It lubricates the moving parts inside the engine.", "C) It changes the colour of the engine."]},
                {"q": "15. Which type of oil is the most expensive?",
                 "options": ["A) Mineral oil", "B) Semi-synthetic oil", "C) Fully synthetic oil"]},
                {"q": "16. How often do modern cars usually need an oil change?",
                 "options": ["A) Every 1,000 km", "B) Every 10,000 to 15,000 km", "C) Every 50,000 km"]},
                {"q": "17. What tool is used to check the oil level?",
                 "options": ["A) A wrench", "B) A scanner", "C) A dipstick"]},
                {"q": "18. Where can you find information about which oil to use?",
                 "options": ["A) On the internet only", "B) In the owner's manual", "C) At any petrol station"]},
            ],
            "part4_sentences": [
                {"pre": "When a customer brings a car to the workshop, the mechanic first does a visual (19) _____ of the vehicle.",
                 "options": ["A) inspection", "B) invention", "C) invitation"]},
                {"pre": "Then, the mechanic connects the diagnostic (20) _____ to the car's computer system.",
                 "options": ["A) television", "B) scanner", "C) telephone"]},
                {"pre": "The scanner shows error (21) _____ that help identify the problem.",
                 "options": ["A) songs", "B) codes", "C) colours"]},
                {"pre": "After finding the problem, the mechanic (22) _____ the customer what repairs are needed.",
                 "options": ["A) tells", "B) sells", "C) hides"]},
                {"pre": "The customer must (23) _____ before the mechanic starts working on the car.",
                 "options": ["A) disagree", "B) leave", "C) approve"]},
                {"pre": "A good mechanic always (24) _____ the car before returning it to the customer.",
                 "options": ["A) tests", "B) paints", "C) sells"]},
            ],
            "part5_sentences": [
                {"text": "25. A mechanic uses a _____ to lift a car.", "hint": "(jack)"},
                {"text": "26. You should always wear safety _____ to protect your eyes.", "hint": "(glasses / goggles)"},
                {"text": "27. The engine _____ not start because the battery was dead.", "hint": "(did / would)"},
                {"text": "28. Brake pads need to be _____ when they are worn out.", "hint": "(replaced / changed)"},
                {"text": "29. The mechanic checked the oil _____ using the dipstick.", "hint": "(level)"},
                {"text": "30. This car runs _____ diesel, not petrol.", "hint": "(on)"},
            ],
        },
        "electricidad": {
            "name": "Electricidad",
            "part1_questions": [
                {"q": "1. It is dangerous to touch this equipment.",
                 "options": ["A) DANGER: HIGH VOLTAGE - Do not touch",
                             "B) ELECTRICAL SUPPLIES - Available at reception",
                             "C) LIGHT SWITCH - Please turn off when leaving"]},
                {"q": "2. You cannot enter this room without special training.",
                 "options": ["A) STAFF ROOM - Open during breaks only",
                             "B) RESTRICTED AREA - Authorized electricians only",
                             "C) CLASSROOM 5 - English class at 10am"]},
                {"q": "3. Remember to turn off the power before you start working.",
                 "options": ["A) LOCKOUT/TAGOUT - De-energize before maintenance",
                             "B) EMERGENCY EXIT - Keep clear at all times",
                             "C) SWITCH ON - Press the green button to start"]},
                {"q": "4. You can buy electrical materials here.",
                 "options": ["A) DANGER - Electrical panel, keep away",
                             "B) ELECTRICAL SUPPLIES STORE - Open Mon-Fri 9am-6pm",
                             "C) NO PARKING - Loading zone for equipment only"]},
                {"q": "5. This event will teach you about new technology.",
                 "options": ["A) POWER OUTAGE - Scheduled for Friday 2pm-4pm",
                             "B) RENEWABLE ENERGY SEMINAR - Free entry, Saturday 10am",
                             "C) CAUTION - Wet paint on walls"]},
                {"q": "6. You must disconnect this before repairing it.",
                 "options": ["A) UNPLUG EQUIPMENT before cleaning or servicing",
                             "B) PLUG IN HERE - 220V socket available",
                             "C) BATTERIES INCLUDED - Ready to use"]},
            ],
            "part2_text": "Luis, Camila and Matias are studying electricity at a technical school.\n\nLuis loves working with residential electrical installations. He has already helped his father install lights and sockets at home. He wants to get his SEC (Superintendencia de Electricidad y Combustibles) licence after school. He finds English useful for reading about international electrical codes.\n\nCamila is very interested in renewable energy, especially solar panels. She has watched many videos about solar installation in English and can understand most of the technical vocabulary. Her dream is to start her own solar energy installation company in the future.\n\nMatias is fascinated by industrial electricity. He wants to work in a big factory or a mining company. He knows that these companies often use equipment with manuals in English. He is also interested in programmable logic controllers (PLCs) and automation.",
            "part2_questions": [
                {"q": "7. Who has helped install electrical equipment at home?", "options": ["A) Luis", "B) Camila", "C) Matias"]},
                {"q": "8. Who wants to work in a factory or mine?", "options": ["A) Luis", "B) Camila", "C) Matias"]},
                {"q": "9. Who is interested in solar energy?", "options": ["A) Luis", "B) Camila", "C) Matias"]},
                {"q": "10. Who wants to get a professional licence?", "options": ["A) Luis", "B) Camila", "C) Matias"]},
                {"q": "11. Who wants to start their own company?", "options": ["A) Luis", "B) Camila", "C) Matias"]},
                {"q": "12. Who is interested in automation?", "options": ["A) Luis", "B) Camila", "C) Matias"]},
                {"q": "13. Who reads about international electrical codes?", "options": ["A) Luis", "B) Camila", "C) Matias"]},
            ],
            "part3_text": "Electrical Safety: The Basics\n\nWorking with electricity is dangerous. Every year, thousands of people around the world are injured or killed in electrical accidents. Most of these accidents can be prevented by following basic safety rules.\n\nThe most important rule is: always turn off the power before working on any electrical system. This process is called \"lockout/tagout.\" It means you must disconnect the power supply and put a lock on the switch so nobody can turn it on while you are working.\n\nAnother essential safety practice is testing before touching. Even after turning off the power, you should use a voltage tester to make sure there is no electricity flowing. Equipment can sometimes hold a charge even when it is disconnected.\n\nPersonal Protective Equipment (PPE) is also very important. Electricians must wear insulated gloves, safety glasses, and appropriate footwear. In some situations, they also need arc flash protection.\n\nFinally, never work alone on a dangerous electrical system. Always have a partner nearby who can help in an emergency. If someone receives an electric shock, do not touch them directly - use a non-conductive material to separate them from the power source, and call emergency services immediately.",
            "part3_questions": [
                {"q": "14. What is the most important safety rule when working with electricity?",
                 "options": ["A) Always work quickly.", "B) Always turn off the power before working.", "C) Always use new tools."]},
                {"q": "15. What does 'lockout/tagout' mean?",
                 "options": ["A) Locking the door of the workshop.", "B) Disconnecting power and locking the switch.", "C) Testing the equipment after repair."]},
                {"q": "16. Why should you test before touching?",
                 "options": ["A) To check if the tools are clean.", "B) Because equipment can still hold a charge.", "C) To see if the lights are working."]},
                {"q": "17. What PPE should an electrician wear?",
                 "options": ["A) A hard hat and steel boots only.", "B) Insulated gloves, safety glasses, and appropriate footwear.", "C) Regular clothes and sunglasses."]},
                {"q": "18. What should you do if someone gets an electric shock?",
                 "options": ["A) Touch them to pull them away.", "B) Use a non-conductive material to separate them from the power source.", "C) Wait until the power goes off automatically."]},
            ],
            "part4_sentences": [
                {"pre": "Before starting any electrical work, you must always check that the (19) _____ is turned off.",
                 "options": ["A) water", "B) power", "C) radio"]},
                {"pre": "An electrician uses a (20) _____ to measure the voltage in a circuit.",
                 "options": ["A) hammer", "B) screwdriver", "C) multimeter"]},
                {"pre": "Copper is used in electrical wiring because it is a good (21) _____.",
                 "options": ["A) conductor", "B) insulator", "C) colour"]},
                {"pre": "A circuit breaker (22) _____ the circuit if there is too much current flowing.",
                 "options": ["A) opens", "B) closes", "C) breaks"]},
                {"pre": "Solar panels convert sunlight (23) _____ electrical energy.",
                 "options": ["A) from", "B) into", "C) with"]},
                {"pre": "Electricians must always (24) _____ safety rules to avoid accidents.",
                 "options": ["A) ignore", "B) follow", "C) forget"]},
            ],
            "part5_sentences": [
                {"text": "25. An electrician must wear insulated _____ to protect their hands.", "hint": "(gloves)"},
                {"text": "26. Electricity flows through a _____ from the source to the load.", "hint": "(circuit / wire)"},
                {"text": "27. You must turn _____ the power before repairing any equipment.", "hint": "(off)"},
                {"text": "28. A multimeter is used _____ measure voltage, current and resistance.", "hint": "(to)"},
                {"text": "29. The electrical _____ shows which wires connect to which components.", "hint": "(diagram)"},
                {"text": "30. Solar panels work _____ converting sunlight into electricity.", "hint": "(by)"},
            ],
        },
        "electronica": {
            "name": "Electronica",
            "part1_questions": [
                {"q": "1. You must be careful with these small parts.",
                 "options": ["A) CAUTION: Sensitive electronic components - Handle with care",
                             "B) RECYCLING BIN - Place paper here",
                             "C) COMPUTER LAB - Open until 5pm"]},
                {"q": "2. This device should not get wet.",
                 "options": ["A) KEEP DRY - Do not expose to moisture",
                             "B) SWIMMING POOL - Open during summer",
                             "C) WATER FOUNTAIN - Press button to drink"]},
                {"q": "3. You need to wear special protection for your wrists when working here.",
                 "options": ["A) ESD WRIST STRAP REQUIRED - Static-sensitive area",
                             "B) WATCH REPAIR - Bring your watch to reception",
                             "C) FIRST AID KIT - Located behind the door"]},
                {"q": "4. This course will teach you to build electronic circuits.",
                 "options": ["A) ELECTRONICS WORKSHOP - Soldering & PCB Assembly Course",
                             "B) PHOTOGRAPHY CLUB - Meetings every Wednesday",
                             "C) MUSIC ROOM - Instruments available for practice"]},
                {"q": "5. These old electronic devices must go in a special container.",
                 "options": ["A) E-WASTE COLLECTION POINT - Recycle your old electronics here",
                             "B) LOST AND FOUND - Check at the office",
                             "C) GIFT SHOP - Electronic accessories on sale"]},
                {"q": "6. Do not use a lot of heat when connecting these parts.",
                 "options": ["A) HEATER - Temperature setting: Low, Medium, High",
                             "B) CAUTION: Low-temperature soldering required for these components",
                             "C) OVEN - Do not leave unattended while cooking"]},
            ],
            "part2_text": "Valentina, Diego and Francisca are studying electronics at a technical school.\n\nValentina is passionate about programming microcontrollers. She has already built several projects using Arduino boards at home. She likes to read documentation online, which is almost always in English. Her latest project is a temperature sensor that sends data to her phone.\n\nDiego is more interested in the hardware side. He loves soldering components onto circuit boards and is very skilled at reading electronic schematics. He wants to work in a factory that manufactures printed circuit boards (PCBs). He practices reading component datasheets in English.\n\nFrancisca is interested in telecommunications. She wants to understand how mobile phone networks and internet systems work. She has been learning about radio frequencies and signal processing. She watches English tutorials about networking and communication systems.",
            "part2_questions": [
                {"q": "7. Who has built projects with Arduino at home?", "options": ["A) Valentina", "B) Diego", "C) Francisca"]},
                {"q": "8. Who is interested in mobile phone networks?", "options": ["A) Valentina", "B) Diego", "C) Francisca"]},
                {"q": "9. Who is very good at soldering?", "options": ["A) Valentina", "B) Diego", "C) Francisca"]},
                {"q": "10. Who reads online documentation in English?", "options": ["A) Valentina", "B) Diego", "C) Francisca"]},
                {"q": "11. Who wants to work in PCB manufacturing?", "options": ["A) Valentina", "B) Diego", "C) Francisca"]},
                {"q": "12. Who studies signal processing?", "options": ["A) Valentina", "B) Diego", "C) Francisca"]},
                {"q": "13. Who has a project that sends data to a phone?", "options": ["A) Valentina", "B) Diego", "C) Francisca"]},
            ],
            "part3_text": "What is a Printed Circuit Board (PCB)?\n\nA printed circuit board, or PCB, is a flat board made of insulating material (usually fiberglass) with thin copper tracks on its surface. These copper tracks connect electronic components to each other, replacing the need for individual wires.\n\nPCBs are found in almost every electronic device: phones, computers, televisions, medical equipment, and even cars. Without PCBs, modern electronics would not exist.\n\nThe process of making a PCB starts with a design. Engineers use special software (like Eagle or KiCad) to draw the circuit layout. Then, the design is transferred to the board using a chemical process called etching, which removes unwanted copper.\n\nAfter the board is ready, components are placed on it. This can be done by hand (for prototypes) or by machines (for mass production). The components are then soldered to the board to create permanent connections.\n\nQuality control is the final step. Technicians inspect the PCB visually and use testing equipment to make sure all connections work correctly. If there is a defect, the board must be repaired or discarded.",
            "part3_questions": [
                {"q": "14. What material are most PCBs made of?",
                 "options": ["A) Plastic and aluminium", "B) Fiberglass with copper tracks", "C) Wood and metal"]},
                {"q": "15. What is the first step in making a PCB?",
                 "options": ["A) Soldering the components", "B) Designing the circuit layout", "C) Testing the connections"]},
                {"q": "16. What does the etching process do?",
                 "options": ["A) It adds more copper to the board.", "B) It removes unwanted copper.", "C) It paints the board green."]},
                {"q": "17. How are components placed on PCBs in mass production?",
                 "options": ["A) By hand", "B) By machines", "C) By customers"]},
                {"q": "18. What is the last step in PCB production?",
                 "options": ["A) Designing the circuit", "B) Buying the components", "C) Quality control and testing"]},
            ],
            "part4_sentences": [
                {"pre": "Electronic components are very small, so you need to (19) _____ carefully when soldering.",
                 "options": ["A) sing", "B) work", "C) sleep"]},
                {"pre": "A (20) _____ is used to see very small components and connections on a PCB.",
                 "options": ["A) telescope", "B) magnifying glass", "C) mirror"]},
                {"pre": "Before touching electronic components, you should discharge any (21) _____ electricity from your body.",
                 "options": ["A) static", "B) dynamic", "C) kinetic"]},
                {"pre": "The Arduino microcontroller needs to be (22) _____ with the correct code to work.",
                 "options": ["A) painted", "B) programmed", "C) broken"]},
                {"pre": "A multimeter can measure voltage, current, and (23) _____.",
                 "options": ["A) temperature", "B) weight", "C) resistance"]},
                {"pre": "Soldering requires a special iron that heats up to a very high (24) _____.",
                 "options": ["A) speed", "B) temperature", "C) price"]},
            ],
            "part5_sentences": [
                {"text": "25. A diode allows electricity to flow in only one _____.", "hint": "(direction)"},
                {"text": "26. You need a soldering _____ to connect components to a PCB.", "hint": "(iron)"},
                {"text": "27. The LED will not work if it is connected the wrong way _____.", "hint": "(around / round)"},
                {"text": "28. This sensor _____ designed to measure temperature.", "hint": "(is / was)"},
                {"text": "29. The technician tested _____ circuit before connecting it to the power supply.", "hint": "(the)"},
                {"text": "30. Electronic waste should be recycled _____ reduce pollution.", "hint": "(to)"},
            ],
        },
        "grafica": {
            "name": "Grafica",
            "part1_questions": [
                {"q": "1. You must not eat or drink near the machines.",
                 "options": ["A) CAFETERIA - Hot meals available from 12pm",
                             "B) NO FOOD OR BEVERAGES near printing equipment",
                             "C) VENDING MACHINE - Snacks and drinks, ground floor"]},
                {"q": "2. This ink could be harmful to your skin.",
                 "options": ["A) CAUTION: Wear protective gloves when handling ink",
                             "B) INK CARTRIDGES - Available at the supply room",
                             "C) ART EXHIBITION - Student works on display this week"]},
                {"q": "3. You can get your documents printed here.",
                 "options": ["A) RECYCLING - Paper and cardboard only",
                             "B) PRINT SHOP - Copies, binding, and large format printing",
                             "C) LIBRARY - Return books by Friday"]},
                {"q": "4. The air in this room needs special care.",
                 "options": ["A) ADEQUATE VENTILATION REQUIRED - Chemical fumes present",
                             "B) AIR CONDITIONING - Temperature set to 22 C",
                             "C) OPEN WINDOW - Fresh air welcome"]},
                {"q": "5. You must check the colours before printing many copies.",
                 "options": ["A) COLOUR PROOF REQUIRED before starting production run",
                             "B) COLOUR PENCILS - Available at the art supply store",
                             "C) PAINT THIS WALL - Volunteers needed Saturday"]},
                {"q": "6. These files must be in a specific format.",
                 "options": ["A) SUBMIT FILES IN PDF/X FORMAT for printing",
                             "B) DOWNLOAD FREE SOFTWARE from our website",
                             "C) USB DRIVES - On sale at the bookshop"]},
            ],
            "part2_text": "Martin, Isidora and Joaquin are studying graphic production at a technical school.\n\nMartin is very interested in digital printing. He loves working with large-format printers and learning about different types of paper and substrates. He has already done an internship at a local print shop. He uses English to understand the settings on the printing software.\n\nIsidora is passionate about design and prepress. She is excellent with Adobe Illustrator and Photoshop. She spends hours watching tutorials in English on YouTube to learn new techniques. Her dream is to work in packaging design for an international company.\n\nJoaquin is interested in the production side of graphic arts. He wants to learn how to operate offset printing presses. He is very practical and prefers working with the machines rather than on a computer. He knows that many press manuals are written in English or German.",
            "part2_questions": [
                {"q": "7. Who has already done an internship?", "options": ["A) Martin", "B) Isidora", "C) Joaquin"]},
                {"q": "8. Who is excellent with Adobe software?", "options": ["A) Martin", "B) Isidora", "C) Joaquin"]},
                {"q": "9. Who wants to operate offset presses?", "options": ["A) Martin", "B) Isidora", "C) Joaquin"]},
                {"q": "10. Who uses English for printing software?", "options": ["A) Martin", "B) Isidora", "C) Joaquin"]},
                {"q": "11. Who watches design tutorials in English?", "options": ["A) Martin", "B) Isidora", "C) Joaquin"]},
                {"q": "12. Who prefers machines over computers?", "options": ["A) Martin", "B) Isidora", "C) Joaquin"]},
                {"q": "13. Who wants to work in packaging design?", "options": ["A) Martin", "B) Isidora", "C) Joaquin"]},
            ],
            "part3_text": "The CMYK Colour Model\n\nIn the printing industry, colours are created using the CMYK model: Cyan, Magenta, Yellow, and Key (Black). This is different from the RGB model (Red, Green, Blue) used on computer screens.\n\nWhen you design something on a computer, the screen shows colours in RGB. But when you print it, the printer uses CMYK inks. This is why colours sometimes look different on paper compared to the screen. This problem is called \"colour shift.\"\n\nTo avoid colour shift, graphic technicians use colour management tools. They calibrate their monitors, use ICC colour profiles, and always make a test print (called a \"proof\") before starting a large production run.\n\nThe quality of the final print also depends on the resolution. Resolution is measured in DPI (dots per inch). For professional printing, the standard is 300 DPI. Images with low resolution (72 DPI, for example) will look blurry when printed.\n\nUnderstanding CMYK, colour management, and resolution are essential skills for any graphic production technician. These concepts are used daily in print shops around the world.",
            "part3_questions": [
                {"q": "14. What does CMYK stand for?",
                 "options": ["A) Computer, Monitor, Yellow, Keyboard", "B) Cyan, Magenta, Yellow, Key (Black)", "C) Colour, Mixing, Your, Kit"]},
                {"q": "15. What is 'colour shift'?",
                 "options": ["A) When colours change from summer to winter.", "B) When colours look different on paper compared to the screen.", "C) When the printer runs out of ink."]},
                {"q": "16. What is a 'proof'?",
                 "options": ["A) A certificate of quality", "B) A test print before large production", "C) A colour pencil drawing"]},
                {"q": "17. What is the standard resolution for professional printing?",
                 "options": ["A) 72 DPI", "B) 150 DPI", "C) 300 DPI"]},
                {"q": "18. Why do images with low resolution look bad when printed?",
                 "options": ["A) Because the paper is too thin.", "B) Because they look blurry.", "C) Because the ink runs out."]},
            ],
            "part4_sentences": [
                {"pre": "Before printing a large order, you should always make a colour (19) _____ first.",
                 "options": ["A) movie", "B) proof", "C) song"]},
                {"pre": "The designer saved the (20) _____ in PDF format for the printing press.",
                 "options": ["A) music", "B) food", "C) file"]},
                {"pre": "Offset printing uses four (21) _____: cyan, magenta, yellow and black.",
                 "options": ["A) inks", "B) papers", "C) screens"]},
                {"pre": "The print resolution must be at (22) _____ 300 DPI for good quality.",
                 "options": ["A) most", "B) first", "C) least"]},
                {"pre": "The paper (23) _____ through the press at high speed during production.",
                 "options": ["A) flies", "B) runs", "C) sleeps"]},
                {"pre": "After printing, the pages need to dry (24) _____ they can be cut and bound.",
                 "options": ["A) before", "B) because", "C) although"]},
            ],
            "part5_sentences": [
                {"text": "25. The opposite of a dark colour is a _____ colour.", "hint": "(light / bright)"},
                {"text": "26. A graphic designer uses a computer to create _____ and layouts.", "hint": "(designs / images)"},
                {"text": "27. The printer is _____ of ink. We need to replace the cartridges.", "hint": "(out)"},
                {"text": "28. This image is too small. We need to make it _____.", "hint": "(bigger / larger)"},
                {"text": "29. The paper _____ cut into the correct size before printing.", "hint": "(is / was)"},
                {"text": "30. Offset printing is used _____ large quantities of books and magazines.", "hint": "(for)"},
            ],
        },
        "industrial": {
            "name": "Mecanica Industrial",
            "part1_questions": [
                {"q": "1. This machine is very noisy.",
                 "options": ["A) EAR PROTECTION REQUIRED - Noise level exceeds 85 dB",
                             "B) MUSIC ROOM - Please keep door closed",
                             "C) QUIET ZONE - Hospital area, silence please"]},
                {"q": "2. Only specially trained people can use this equipment.",
                 "options": ["A) CNC MACHINE - Certified operators only",
                             "B) COFFEE MACHINE - Free for all staff",
                             "C) PHOTOCOPIER - Insert card to use"]},
                {"q": "3. You must not stand in this area when the machine is working.",
                 "options": ["A) BUS STOP - Wait behind the line",
                             "B) DANGER ZONE - Keep clear when machine is in operation",
                             "C) QUEUE HERE - Wait for your turn"]},
                {"q": "4. Heavy things are moved using this equipment.",
                 "options": ["A) OVERHEAD CRANE - Maximum load 5 tonnes",
                             "B) ELEVATOR - Maximum 8 persons",
                             "C) SHOPPING TROLLEY - Return after use"]},
                {"q": "5. You can learn to use CNC machines at this event.",
                 "options": ["A) LIBRARY CLOSED - Reopens Monday at 9am",
                             "B) CNC PROGRAMMING WORKSHOP - Intermediate level, register online",
                             "C) SPORTS DAY - All students invited, Friday 2pm"]},
                {"q": "6. Metal pieces must be measured precisely.",
                 "options": ["A) QUALITY CONTROL - All parts must be within 0.01mm tolerance",
                             "B) WEIGHING SCALE - Place items on platform",
                             "C) RULER - 30cm, available at the office"]},
            ],
            "part2_text": "Felipe, Catalina and Nicolas are studying industrial mechanics at a technical school.\n\nFelipe loves working with CNC machines. He has learned basic G-code programming and can set up the lathe for simple turning operations. He reads English-language CNC forums to find machining tips and solutions. His goal is to work as a CNC programmer at a large manufacturing company.\n\nCatalina is interested in welding and metal fabrication. She has practiced MIG and TIG welding in the school workshop and is very precise in her work. She wants to get international welding certifications, which require understanding English technical documents.\n\nNicolas is fascinated by hydraulic and pneumatic systems. He enjoys understanding how machines move using fluid power. He has been reading about predictive maintenance using sensors and AI, mostly from English-language technical websites. He wants to work in maintenance at a mining company.",
            "part2_questions": [
                {"q": "7. Who can program CNC machines?", "options": ["A) Felipe", "B) Catalina", "C) Nicolas"]},
                {"q": "8. Who is interested in welding?", "options": ["A) Felipe", "B) Catalina", "C) Nicolas"]},
                {"q": "9. Who wants to work in mining?", "options": ["A) Felipe", "B) Catalina", "C) Nicolas"]},
                {"q": "10. Who reads CNC forums in English?", "options": ["A) Felipe", "B) Catalina", "C) Nicolas"]},
                {"q": "11. Who wants international certifications?", "options": ["A) Felipe", "B) Catalina", "C) Nicolas"]},
                {"q": "12. Who is interested in hydraulic systems?", "options": ["A) Felipe", "B) Catalina", "C) Nicolas"]},
                {"q": "13. Who reads about predictive maintenance?", "options": ["A) Felipe", "B) Catalina", "C) Nicolas"]},
            ],
            "part3_text": "CNC Machines: The Basics\n\nCNC stands for Computer Numerical Control. A CNC machine is a tool that is controlled by a computer program instead of by a human operator manually moving the tool. CNC machines can cut, drill, and shape metal and other materials with extreme precision.\n\nThe most common types of CNC machines are lathes (for turning cylindrical parts), milling machines (for cutting flat surfaces and complex shapes), and drilling machines. Modern factories also use CNC plasma cutters, laser cutters, and 3D printers.\n\nTo operate a CNC machine, you need to understand G-code, which is the programming language that tells the machine what to do. For example, G00 means \"rapid move,\" G01 means \"linear move at a set speed,\" and M06 means \"change tool.\" Most G-code documentation is written in English.\n\nSafety is extremely important when working with CNC machines. Operators must wear safety glasses, use machine guards, and never reach into the machine while it is running. The workpiece must be properly secured in the chuck or vise before starting.\n\nCNC technology is constantly improving. New machines can work faster, with greater precision, and can even be monitored remotely using internet-connected sensors. This is part of what is called Industry 4.0.",
            "part3_questions": [
                {"q": "14. What does CNC stand for?",
                 "options": ["A) Computer New Connection", "B) Computer Numerical Control", "C) Central Network Computer"]},
                {"q": "15. What is a lathe used for?",
                 "options": ["A) Cutting flat surfaces", "B) Turning cylindrical parts", "C) Painting metal"]},
                {"q": "16. What is G-code?",
                 "options": ["A) A type of metal used in machines.", "B) The programming language for CNC machines.", "C) A safety certification for operators."]},
                {"q": "17. What does M06 mean in G-code?",
                 "options": ["A) Rapid move", "B) Stop machine", "C) Change tool"]},
                {"q": "18. What is Industry 4.0?",
                 "options": ["A) A new type of CNC machine.", "B) The use of internet and sensors to monitor machines.", "C) A safety manual for factories."]},
            ],
            "part4_sentences": [
                {"pre": "The CNC operator must (19) _____ the program carefully before running the machine.",
                 "options": ["A) delete", "B) check", "C) forget"]},
                {"pre": "The metal piece is held in place by a (20) _____ while the lathe is turning.",
                 "options": ["A) rope", "B) tape", "C) chuck"]},
                {"pre": "After machining, the part must be (21) _____ to check if it meets the specifications.",
                 "options": ["A) painted", "B) measured", "C) heated"]},
                {"pre": "Welding joins two pieces of metal by (22) _____ them together at high temperature.",
                 "options": ["A) freezing", "B) fusing", "C) washing"]},
                {"pre": "Hydraulic systems use (23) _____ under pressure to move heavy objects.",
                 "options": ["A) air", "B) fluid", "C) sand"]},
                {"pre": "All tools must be (24) _____ to their correct place after use.",
                 "options": ["A) thrown", "B) returned", "C) broken"]},
            ],
            "part5_sentences": [
                {"text": "25. A CNC lathe is used to make _____ parts.", "hint": "(cylindrical / round)"},
                {"text": "26. The operator must wear safety _____ to protect their eyes.", "hint": "(glasses / goggles)"},
                {"text": "27. The machine must be turned _____ before cleaning.", "hint": "(off)"},
                {"text": "28. This tool is _____ for cutting metal, not wood.", "hint": "(used / designed)"},
                {"text": "29. The mechanic _____ the measurements with a calliper.", "hint": "(took / checked)"},
                {"text": "30. Steel is stronger _____ aluminium.", "hint": "(than)"},
            ],
        },
    }
    
    d = sp_data[specialty]
    return {
        "level": "3ro Medio",
        "specialty": d["name"],
        "filename": f"diagnostico_3ro_{specialty}.pdf",
        "part1": {
            "instructions": "Questions 1-6\nWhich notice (A, B or C) says this?\nFor each question, choose the correct letter.",
            "questions": d["part1_questions"],
        },
        "part2": {
            "instructions": "Questions 7-13\nRead the text below about three students.\nFor each question, choose the correct answer (A, B or C).",
            "text": d["part2_text"],
            "questions": d["part2_questions"],
        },
        "part3": {
            "instructions": "Questions 14-18\nRead the text below and choose the correct answer (A, B or C) for each question.",
            "text": d["part3_text"],
            "questions": d["part3_questions"],
        },
        "part4": {
            "instructions": "Questions 19-24\nRead the text below and choose the correct word (A, B or C) for each space.",
            "text_before": "",
            "sentences": d["part4_sentences"],
        },
        "part5": {
            "instructions": "Questions 25-30\nRead the text below and write the missing word for each space.\nUse only ONE word for each space.",
            "sentences": d["part5_sentences"],
        }
    }


def get_4to_content(specialty):
    sp_data = {
        "automotriz": {
            "name": "Mecanica Automotriz",
            "part1_questions": [
                {"q": "1. You need a special qualification to do this job.",
                 "options": ["A) AUTOMOTIVE DIAGNOSTIC TECHNICIAN REQUIRED - Must hold ASE certification or equivalent",
                             "B) PARKING AVAILABLE - First come, first served",
                             "C) CAR WASH - Open weekends only"]},
                {"q": "2. The company is looking for new workers.",
                 "options": ["A) JOB VACANCY: Automotive Mechanic - Send CV to hr@workshop.com",
                             "B) CUSTOMER PARKING ONLY - Others will be towed",
                             "C) SERVICE HOURS: Monday to Saturday 8am-6pm"]},
                {"q": "3. This vehicle uses a new type of energy.",
                 "options": ["A) DIESEL ONLY - Do not use petrol",
                             "B) ELECTRIC VEHICLE CHARGING STATION - Available 24/7",
                             "C) OIL CHANGE - Special offer this month"]},
                {"q": "4. You cannot repair this vehicle without the right information.",
                 "options": ["A) TECHNICAL SERVICE MANUAL REQUIRED - Download from manufacturer website",
                             "B) GPS NAVIGATION - Update maps annually",
                             "C) RADIO STATION - Tune to 98.5 FM"]},
                {"q": "5. This system warns the driver about problems.",
                 "options": ["A) CHECK ENGINE LIGHT - Vehicle requires diagnostic scan",
                             "B) TRAFFIC LIGHT - Stop on red, go on green",
                             "C) STREET LIGHT - Automatic on at dusk"]},
                {"q": "6. Safety equipment must be used in this area.",
                 "options": ["A) MANDATORY PPE: Safety glasses, gloves, and steel-toe boots required",
                             "B) SHOE STORE - 20% discount on all footwear",
                             "C) DRESS CODE - Smart casual for office staff"]},
            ],
            "part2_text": "Interview with three automotive professionals about their career experiences.\n\nRoberto graduated from a technical school five years ago. He now works as a diagnostic specialist at a car dealership. His main job is using computer systems to find problems in modern vehicles. He says the biggest change in his field is the amount of electronics in new cars - about 40% of repairs now involve software. He uses English daily to read technical bulletins from the manufacturer.\n\nPatricia started as a general mechanic but specialized in hybrid and electric vehicles two years ago. She took an online course in English about EV systems. She now earns almost double her previous salary. She advises students to learn about electric vehicles because \"they are the future.\" She also says English is essential for accessing the best training materials.\n\nAndres has twenty years of experience and owns a small independent workshop. He focuses on traditional mechanical repairs: engines, transmissions, and suspensions. He worries that independent workshops may struggle as cars become more electronic. However, he believes there will always be demand for skilled mechanics who can do hands-on work. He has recently started learning English to read troubleshooting forums online.",
            "part2_questions": [
                {"q": "7. Who is a diagnostic specialist?", "options": ["A) Roberto", "B) Patricia", "C) Andres"]},
                {"q": "8. Who specialized in electric vehicles?", "options": ["A) Roberto", "B) Patricia", "C) Andres"]},
                {"q": "9. Who owns their own workshop?", "options": ["A) Roberto", "B) Patricia", "C) Andres"]},
                {"q": "10. Who says 40% of repairs involve software?", "options": ["A) Roberto", "B) Patricia", "C) Andres"]},
                {"q": "11. Who almost doubled their salary?", "options": ["A) Roberto", "B) Patricia", "C) Andres"]},
                {"q": "12. Who recently started learning English?", "options": ["A) Roberto", "B) Patricia", "C) Andres"]},
                {"q": "13. Who is worried about the future of independent workshops?", "options": ["A) Roberto", "B) Patricia", "C) Andres"]},
            ],
            "part3_text": "The Impact of Electric Vehicles on Automotive Workshops\n\nElectric vehicles (EVs) are rapidly growing in popularity worldwide and in Chile. In 2023, EV sales in Chile increased by over 100% compared to the previous year. This trend is changing the automotive industry in significant ways.\n\nTraditional mechanics are trained to work with internal combustion engines, which have hundreds of moving parts: pistons, valves, camshafts, and timing belts. Electric vehicles, however, have much simpler drivetrains. An electric motor has about 20 moving parts compared to over 2,000 in a combustion engine.\n\nThis means that some traditional repair skills are becoming less important, while new skills are in high demand. EV technicians need to understand high-voltage battery systems, electric motor controllers, regenerative braking, and software diagnostics. Working with high-voltage systems also requires special safety training.\n\nHowever, EVs still need traditional maintenance: tyres, suspension, brakes, and body repairs remain the same. Additionally, hybrid vehicles (which combine both systems) require mechanics who understand both technologies.\n\nExperts predict that by 2035, most new cars sold in Chile will be electric or hybrid. Mechanics who prepare for this transition now will have a significant advantage in the job market. Learning English is also important, as most EV training materials and technical documentation are published in English first.",
            "part3_questions": [
                {"q": "14. By how much did EV sales increase in Chile in 2023?",
                 "options": ["A) 50%", "B) Over 100%", "C) 200%"]},
                {"q": "15. How many moving parts does an electric motor have approximately?",
                 "options": ["A) About 20", "B) About 200", "C) About 2,000"]},
                {"q": "16. What new skill do EV technicians need?",
                 "options": ["A) Basic oil changes", "B) High-voltage battery systems", "C) Traditional engine tuning"]},
                {"q": "17. What traditional maintenance do EVs still need?",
                 "options": ["A) Engine oil changes", "B) Spark plug replacement", "C) Tyre, suspension and brake maintenance"]},
                {"q": "18. What do experts predict about 2035?",
                 "options": ["A) All petrol stations will close.", "B) Most new cars will be electric or hybrid.", "C) Mechanics will no longer be needed."]},
            ],
            "part4_sentences": [
                {"pre": "Before working on an electric vehicle, the technician must (19) _____ the high-voltage battery.",
                 "options": ["A) disconnect", "B) charge", "C) ignore"]},
                {"pre": "The diagnostic (20) _____ showed three error codes related to the battery management system.",
                 "options": ["A) manual", "B) report", "C) menu"]},
                {"pre": "Hybrid vehicles combine an electric motor (21) _____ an internal combustion engine.",
                 "options": ["A) or", "B) but", "C) and"]},
                {"pre": "The customer asked the mechanic to (22) _____ an estimate for the repairs.",
                 "options": ["A) provide", "B) receive", "C) avoid"]},
                {"pre": "Training in EV technology has become (23) _____ popular among young mechanics.",
                 "options": ["A) less", "B) increasingly", "C) never"]},
                {"pre": "The workshop invested in new (24) _____ to be able to service electric vehicles.",
                 "options": ["A) furniture", "B) equipment", "C) customers"]},
            ],
            "part5_sentences": [
                {"text": "25. An electric vehicle is powered _____ a rechargeable battery.", "hint": "(by)"},
                {"text": "26. The mechanic must wear insulated gloves when working _____ high-voltage systems.", "hint": "(on / with)"},
                {"text": "27. The car _____ been serviced three times this year.", "hint": "(has)"},
                {"text": "28. Hybrid vehicles are more fuel-_____ than traditional cars.", "hint": "(efficient)"},
                {"text": "29. The technician _____ to complete a safety course before working on EVs.", "hint": "(needs / has)"},
                {"text": "30. Most technical manuals for new cars are written _____ English.", "hint": "(in)"},
            ],
        },
        "electricidad": {
            "name": "Electricidad",
            "part1_questions": [
                {"q": "1. This job requires a professional licence.",
                 "options": ["A) ELECTRICIAN NEEDED - Must hold valid SEC Class A licence",
                             "B) FISHING LICENCE - Available at the town hall",
                             "C) DRIVING LESSONS - Book your test today"]},
                {"q": "2. The building will have no electricity for a few hours.",
                 "options": ["A) SCHEDULED POWER OUTAGE: Friday 2pm-5pm for maintenance",
                             "B) POWER BANK - Charge your phone here",
                             "C) GENERATOR FOR SALE - 5kW, barely used"]},
                {"q": "3. Workers must check this before entering.",
                 "options": ["A) VERIFY LOCKOUT/TAGOUT STATUS before entering electrical room",
                             "B) CHECK YOUR TICKET before boarding the bus",
                             "C) SCAN YOUR CARD at the library entrance"]},
                {"q": "4. This system produces energy from the sun.",
                 "options": ["A) SOLAR PANEL INSTALLATION - Completed by GreenPower Ltd.",
                             "B) SUNSCREEN - SPF 50, available at the pharmacy",
                             "C) SUNSET VIEWING POINT - Best time: 7pm"]},
                {"q": "5. Only specific cable types are acceptable here.",
                 "options": ["A) WELCOME - Please remove your shoes at the door",
                             "B) USE ONLY CERTIFIED CABLES rated for 600V in this installation",
                             "C) CABLE TV - 200 channels available"]},
                {"q": "6. This equipment must be tested regularly.",
                 "options": ["A) FIRE EXTINGUISHER - Next inspection due: March 2026",
                             "B) ELECTRICAL PANEL - Annual thermographic inspection required",
                             "C) VENDING MACHINE - Out of order, sorry"]},
            ],
            "part2_text": "Three professional electricians share their career experiences.\n\nCarmen has been a residential electrician for eight years. She specializes in smart home installations: automated lighting, security systems, and voice-controlled devices. She says the job has changed completely since she started - now she needs to understand both electrical systems and computer networks. Most smart home product documentation is in English.\n\nFernando works as an industrial electrician at a copper mine in northern Chile. His main responsibility is maintaining the high-voltage distribution system that powers the mining equipment. He works in shifts and earns a very good salary. The job requires reading English-language safety protocols and equipment manuals regularly.\n\nGabriela started her own renewable energy company three years ago. She and her team install solar panels for homes and businesses. Business is growing fast because the Chilean government offers incentives for solar energy. She uses English constantly to communicate with international solar panel suppliers and to access technical training.",
            "part2_questions": [
                {"q": "7. Who specializes in smart home installations?", "options": ["A) Carmen", "B) Fernando", "C) Gabriela"]},
                {"q": "8. Who works at a copper mine?", "options": ["A) Carmen", "B) Fernando", "C) Gabriela"]},
                {"q": "9. Who started their own company?", "options": ["A) Carmen", "B) Fernando", "C) Gabriela"]},
                {"q": "10. Who needs to understand computer networks?", "options": ["A) Carmen", "B) Fernando", "C) Gabriela"]},
                {"q": "11. Who communicates with international suppliers?", "options": ["A) Carmen", "B) Fernando", "C) Gabriela"]},
                {"q": "12. Who works in shifts?", "options": ["A) Carmen", "B) Fernando", "C) Gabriela"]},
                {"q": "13. Who benefits from government incentives?", "options": ["A) Carmen", "B) Fernando", "C) Gabriela"]},
            ],
            "part3_text": "Smart Grids: The Future of Electricity\n\nA smart grid is an electrical network that uses digital technology to monitor and manage the flow of electricity from all generation sources to meet the varying demands of consumers. Unlike the traditional grid, which only sends power in one direction (from power plant to consumer), a smart grid allows two-way communication.\n\nIn a smart grid, sensors installed throughout the network collect data about energy consumption, line voltage, equipment temperature, and weather conditions. This data is sent to a central computer system that can automatically adjust the distribution of electricity.\n\nOne major benefit of smart grids is their ability to integrate renewable energy sources like solar and wind. Since these sources produce electricity intermittently (only when the sun shines or the wind blows), the smart grid can balance supply and demand by storing excess energy in batteries or redirecting it.\n\nSmart grids also help reduce power outages. When a fault is detected, the system can automatically reroute electricity through alternative paths, restoring power in seconds instead of hours.\n\nFor electricians, smart grids mean new job opportunities. Technicians are needed to install and maintain sensors, communication equipment, and energy storage systems. Smart grid technology training is mostly available in English, making language skills increasingly valuable.",
            "part3_questions": [
                {"q": "14. What is a smart grid?",
                 "options": ["A) A new type of solar panel.", "B) An electrical network that uses digital technology to manage electricity.", "C) A computer program for designing circuits."]},
                {"q": "15. How is a smart grid different from a traditional grid?",
                 "options": ["A) It uses more coal power.", "B) It allows two-way communication.", "C) It only works at night."]},
                {"q": "16. What data do smart grid sensors collect?",
                 "options": ["A) Energy consumption, voltage, temperature and weather", "B) Customer names and addresses", "C) Television viewing habits"]},
                {"q": "17. How do smart grids handle renewable energy?",
                 "options": ["A) They reject it.", "B) They balance supply and demand using storage.", "C) They only use solar energy."]},
                {"q": "18. What new opportunity do smart grids create for electricians?",
                 "options": ["A) Working in restaurants.", "B) Installing and maintaining sensors and communication equipment.", "C) Building traditional power plants."]},
            ],
            "part4_sentences": [
                {"pre": "The electrician (19) _____ the voltage before starting the installation.",
                 "options": ["A) measured", "B) imagined", "C) ignored"]},
                {"pre": "Smart home devices are (20) _____ to a central hub via Wi-Fi.",
                 "options": ["A) disconnected", "B) connected", "C) removed"]},
                {"pre": "The capacity of a battery is measured in ampere-(21) _____.",
                 "options": ["A) metres", "B) hours", "C) litres"]},
                {"pre": "Solar panels should be installed (22) _____ a north-facing roof in Chile.",
                 "options": ["A) on", "B) under", "C) behind"]},
                {"pre": "The entire electrical installation must (23) _____ with SEC regulations.",
                 "options": ["A) disagree", "B) comply", "C) compete"]},
                {"pre": "Renewable energy is becoming more (24) _____ as technology improves.",
                 "options": ["A) expensive", "B) rare", "C) affordable"]},
            ],
            "part5_sentences": [
                {"text": "25. Solar panels generate electricity _____ sunlight.", "hint": "(from)"},
                {"text": "26. The electrician _____ to verify the wiring before turning on the power.", "hint": "(needs / has)"},
                {"text": "27. A transformer is used to change the _____ of electricity.", "hint": "(voltage)"},
                {"text": "28. Three-phase power is more _____ than single-phase for industrial use.", "hint": "(efficient / powerful)"},
                {"text": "29. The circuit breaker _____ automatically when there is a short circuit.", "hint": "(trips / opens)"},
                {"text": "30. All electrical work must be done _____ a licensed professional.", "hint": "(by)"},
            ],
        },
        "electronica": {
            "name": "Electronica",
            "part1_questions": [
                {"q": "1. You need specific training to apply for this position.",
                 "options": ["A) ELECTRONICS TECHNICIAN WANTED - Experience with PCB assembly required",
                             "B) COMPUTER FOR SALE - Intel Core i7, good condition",
                             "C) PHONE REPAIR - Screen replacement in 30 minutes"]},
                {"q": "2. The temperature in this room must be controlled.",
                 "options": ["A) CLIMATE-CONTROLLED ENVIRONMENT - Maintain 22 C +/- 2 C for component storage",
                             "B) BEACH - Water temperature: 18 C today",
                             "C) RESTAURANT - Air conditioning available"]},
                {"q": "3. This device can communicate without wires.",
                 "options": ["A) BLUETOOTH ENABLED - Pair with your smartphone",
                             "B) TELEPHONE LINE - Available for international calls",
                             "C) EXTENSION CORD - 5 metres, heavy duty"]},
                {"q": "4. Old electronic products must be disposed of properly.",
                 "options": ["A) E-WASTE RECYCLING - Bring your old electronics here. Free disposal.",
                             "B) GARBAGE COLLECTION - Tuesdays and Fridays",
                             "C) SECOND-HAND SHOP - We buy used furniture"]},
                {"q": "5. You must update this before using the device.",
                 "options": ["A) FIRMWARE UPDATE REQUIRED - Download version 3.2 from the manufacturer website",
                             "B) SOFTWARE SALE - 50% off all programs this week",
                             "C) APP STORE - New games available"]},
                {"q": "6. The information on this document tells you how to use the component.",
                 "options": ["A) RECIPE CARD - Ingredients and instructions inside",
                             "B) COMPONENT DATASHEET - Specifications, pin configuration, and application notes",
                             "C) TRAVEL BROCHURE - Destinations and prices"]},
            ],
            "part2_text": "Three electronics professionals discuss their careers and the role of English.\n\nAlejandra works as a quality control technician at a factory that makes electronic components for medical devices. She inspects PCBs using microscopes and automated testing equipment. Her job requires extreme precision - a single defective component could put a patient at risk. All quality standards and documentation at her company are in English.\n\nBruno repairs and maintains telecommunications equipment for a mobile phone company. He travels around the country to fix antenna towers and network equipment. He uses English to read equipment manuals and to communicate with the foreign engineers who designed the systems.\n\nDaniela is an IoT (Internet of Things) developer. She designs systems that connect sensors to the internet for applications like agriculture (soil moisture monitoring) and logistics (package tracking). She programs in Python and C++, and almost all programming resources and libraries have documentation in English. She works remotely and collaborates with teams in three different countries.",
            "part2_questions": [
                {"q": "7. Who works with medical device components?", "options": ["A) Alejandra", "B) Bruno", "C) Daniela"]},
                {"q": "8. Who travels around the country for work?", "options": ["A) Alejandra", "B) Bruno", "C) Daniela"]},
                {"q": "9. Who works remotely with international teams?", "options": ["A) Alejandra", "B) Bruno", "C) Daniela"]},
                {"q": "10. Who inspects PCBs with microscopes?", "options": ["A) Alejandra", "B) Bruno", "C) Daniela"]},
                {"q": "11. Who programs in Python and C++?", "options": ["A) Alejandra", "B) Bruno", "C) Daniela"]},
                {"q": "12. Who fixes antenna towers?", "options": ["A) Alejandra", "B) Bruno", "C) Daniela"]},
                {"q": "13. Who designs systems for agriculture?", "options": ["A) Alejandra", "B) Bruno", "C) Daniela"]},
            ],
            "part3_text": "The Internet of Things (IoT): How It Works\n\nThe Internet of Things refers to the network of physical objects (\"things\") that have sensors, software, and connectivity to exchange data with other devices and systems over the internet. IoT devices range from simple temperature sensors to complex industrial machines.\n\nAn IoT system typically has four components: sensors (to collect data), connectivity (Wi-Fi, Bluetooth, or cellular to transmit data), data processing (cloud computers analyse the information), and a user interface (an app or dashboard where humans can see results and take action).\n\nIoT has many applications. In agriculture, sensors monitor soil moisture, temperature, and sunlight to help farmers optimize irrigation. In healthcare, wearable devices track heart rate, blood oxygen, and sleep patterns. In industry, IoT enables predictive maintenance - sensors on machines detect problems before they cause breakdowns.\n\nSecurity is a major concern in IoT. Because these devices are connected to the internet, they can be targets for hackers. A poorly secured IoT device can give criminals access to an entire network. This is why IoT security - encryption, authentication, and regular firmware updates - is critically important.\n\nThe IoT market is expected to reach 75 billion connected devices by 2030. For electronics technicians, this means enormous job opportunities in designing, installing, maintaining, and securing IoT systems.",
            "part3_questions": [
                {"q": "14. What does IoT stand for?",
                 "options": ["A) Internet of Technology", "B) Internet of Things", "C) Integrated Online Tools"]},
                {"q": "15. What are the four components of an IoT system?",
                 "options": ["A) Camera, screen, keyboard, mouse", "B) Sensors, connectivity, data processing, user interface", "C) Battery, cable, software, manual"]},
                {"q": "16. How does IoT help in agriculture?",
                 "options": ["A) It drives tractors automatically.", "B) It monitors soil moisture and temperature.", "C) It sells products online."]},
                {"q": "17. Why is security important in IoT?",
                 "options": ["A) Because devices are expensive.", "B) Because hackers can access networks through poorly secured devices.", "C) Because the internet is slow."]},
                {"q": "18. How many IoT devices are expected by 2030?",
                 "options": ["A) 7.5 million", "B) 75 million", "C) 75 billion"]},
            ],
            "part4_sentences": [
                {"pre": "The IoT sensor was (19) _____ to send data every 30 seconds.",
                 "options": ["A) broken", "B) programmed", "C) painted"]},
                {"pre": "The technician needs to update the (20) _____ on all connected devices.",
                 "options": ["A) firmware", "B) furniture", "C) fashion"]},
                {"pre": "Wearable devices collect health data and send it to a smartphone (21) _____.",
                 "options": ["A) never", "B) slowly", "C) automatically"]},
                {"pre": "The company (22) _____ $50,000 in new IoT monitoring equipment last year.",
                 "options": ["A) invested", "B) invented", "C) invited"]},
                {"pre": "Strong (23) _____ is essential to protect IoT devices from hackers.",
                 "options": ["A) decoration", "B) encryption", "C) examination"]},
                {"pre": "The number of connected devices continues to (24) _____ every year.",
                 "options": ["A) decrease", "B) grow", "C) disappear"]},
            ],
            "part5_sentences": [
                {"text": "25. The sensor collects data and sends _____ to the cloud.", "hint": "(it)"},
                {"text": "26. This microcontroller _____ be programmed using the Arduino IDE.", "hint": "(can)"},
                {"text": "27. The technician checked all the _____ on the circuit board.", "hint": "(connections / components)"},
                {"text": "28. IoT devices need a stable internet _____ to work properly.", "hint": "(connection)"},
                {"text": "29. The firmware was updated _____ fix a security problem.", "hint": "(to)"},
                {"text": "30. Electronic components should be stored _____ a dry, cool place.", "hint": "(in)"},
            ],
        },
        "grafica": {
            "name": "Grafica",
            "part1_questions": [
                {"q": "1. The company needs someone with design experience.",
                 "options": ["A) GRAPHIC DESIGNER WANTED - Proficiency in Adobe Creative Suite required",
                             "B) ART SUPPLIES - 30% off all paints this week",
                             "C) PHOTOGRAPHY STUDIO - Passport photos available"]},
                {"q": "2. This document shows the exact colours for the job.",
                 "options": ["A) COLOUR CHART - Paint samples for interior walls",
                             "B) PANTONE COLOUR SPECIFICATION - Use PMS 286C for the logo",
                             "C) RAINBOW - Visible after rainfall"]},
                {"q": "3. The file is not in the right format.",
                 "options": ["A) ERROR: File must be saved as PDF/X-4 with embedded fonts for press",
                             "B) FORMAT YOUR USB - Warning: all data will be lost",
                             "C) WORD DOCUMENT - Template available for download"]},
                {"q": "4. This material is better for the environment.",
                 "options": ["A) ECO-FRIENDLY SUBSTRATE - Made from 100% recycled materials, FSC certified",
                             "B) ORGANIC FOOD - Fresh vegetables from local farms",
                             "C) NATURAL GAS - Clean energy for your home"]},
                {"q": "5. You need to verify the print quality before producing more.",
                 "options": ["A) APPROVE PRESS PROOF before authorizing full production run",
                             "B) EXAM RESULTS - Check the noticeboard on Friday",
                             "C) QUALITY HOTEL - 5 stars, book now"]},
                {"q": "6. Visitors can see students' work here.",
                 "options": ["A) STUDENT PORTFOLIO EXHIBITION - Print & Digital Design, Room 201",
                             "B) LOST PROPERTY - Unclaimed items, front desk",
                             "C) STAFF MEETING - Room 305, Wednesday 3pm"]},
            ],
            "part2_text": "Three graphic production professionals talk about their careers.\n\nAndrea works as a prepress technician at a large packaging company. Her job is to prepare design files for printing: checking colours, resolution, fonts, and layout. She must ensure every file is perfectly ready before it goes to the press. One mistake can cost thousands of dollars. She uses Adobe Acrobat and specialized RIP software, most of which have interfaces in English.\n\nSebastian operates a wide-format digital printer for a company that makes banners, vehicle wraps, and building graphics. He loves the variety of his work - every day brings a different project. He has learned a lot about different printing substrates (vinyl, fabric, mesh) and colour management. He reads the printer manufacturer's technical notes in English to optimize print quality.\n\nFlorencia runs her own small design and print studio. She offers graphic design, offset printing, and finishing services. Her biggest challenge is managing a business while staying current with new technology. She recently invested in a UV flatbed printer that can print on almost any material. The training course for the new equipment was entirely in English.",
            "part2_questions": [
                {"q": "7. Who works in packaging?", "options": ["A) Andrea", "B) Sebastian", "C) Florencia"]},
                {"q": "8. Who prints banners and vehicle wraps?", "options": ["A) Andrea", "B) Sebastian", "C) Florencia"]},
                {"q": "9. Who owns a design studio?", "options": ["A) Andrea", "B) Sebastian", "C) Florencia"]},
                {"q": "10. Who prepares files for printing?", "options": ["A) Andrea", "B) Sebastian", "C) Florencia"]},
                {"q": "11. Who reads manufacturer's technical notes?", "options": ["A) Andrea", "B) Sebastian", "C) Florencia"]},
                {"q": "12. Who invested in a UV flatbed printer?", "options": ["A) Andrea", "B) Sebastian", "C) Florencia"]},
                {"q": "13. Whose training course was in English?", "options": ["A) Andrea", "B) Sebastian", "C) Florencia"]},
            ],
            "part3_text": "Sustainable Printing: An Industry in Transformation\n\nThe global printing industry produces approximately 300 million tonnes of paper products every year. This has a significant environmental impact: deforestation, water pollution from chemicals, and carbon emissions from manufacturing and transport.\n\nHowever, the industry is changing. Many print companies are now adopting sustainable practices. The most common change is using FSC-certified paper, which comes from responsibly managed forests. Some companies have also switched to vegetable-based inks (made from soy or other plants) instead of petroleum-based inks.\n\nEnergy efficiency is another area of improvement. Modern printing presses use less energy than older models, and some facilities have installed solar panels to power their operations. Water-based coating systems are replacing chemical-based ones, reducing toxic waste.\n\nDigital printing technology is also contributing to sustainability. Unlike offset printing, which requires large minimum quantities, digital printing allows companies to print exactly the number of copies needed, reducing waste. Variable data printing makes it possible to personalize each print, which reduces unwanted materials.\n\nThe demand for sustainable print products is growing. Many customers now ask for environmental certifications before placing orders. For graphic technicians, understanding sustainable practices is becoming as important as knowing colour management and press operation.",
            "part3_questions": [
                {"q": "14. How much paper products does the printing industry produce yearly?",
                 "options": ["A) 30 million tonnes", "B) 300 million tonnes", "C) 3 billion tonnes"]},
                {"q": "15. What is FSC-certified paper?",
                 "options": ["A) Paper made from plastic.", "B) Paper from responsibly managed forests.", "C) The most expensive paper available."]},
                {"q": "16. What are vegetable-based inks made from?",
                 "options": ["A) Petroleum", "B) Soy or other plants", "C) Recycled ink"]},
                {"q": "17. How does digital printing reduce waste?",
                 "options": ["A) It uses no ink.", "B) It prints exactly the number of copies needed.", "C) It recycles paper automatically."]},
                {"q": "18. What do customers now ask for before placing print orders?",
                 "options": ["A) Free samples", "B) Environmental certifications", "C) Faster delivery"]},
            ],
            "part4_sentences": [
                {"pre": "The designer (19) _____ the image resolution before sending the file to print.",
                 "options": ["A) checked", "B) forgot", "C) painted"]},
                {"pre": "Vegetable-based inks are more (20) _____ than petroleum-based inks.",
                 "options": ["A) dangerous", "B) expensive", "C) environmentally friendly"]},
                {"pre": "The press operator must (21) _____ the colour proof with the digital file.",
                 "options": ["A) compare", "B) ignore", "C) photograph"]},
                {"pre": "Digital printing is ideal for short (22) _____ because there is no setup cost.",
                 "options": ["A) stories", "B) runs", "C) walks"]},
                {"pre": "The packaging design was (23) _____ by a team of three designers.",
                 "options": ["A) eaten", "B) created", "C) destroyed"]},
                {"pre": "All fonts must be (24) _____ in the PDF to avoid printing errors.",
                 "options": ["A) deleted", "B) embedded", "C) forgotten"]},
            ],
            "part5_sentences": [
                {"text": "25. The designer saved the file _____ PDF format before sending it.", "hint": "(in)"},
                {"text": "26. Offset printing is better for _____ quantities than digital printing.", "hint": "(large / big)"},
                {"text": "27. The resolution of this image is _____ low for print.", "hint": "(too)"},
                {"text": "28. A colour proof _____ be approved before starting the full print run.", "hint": "(must / should)"},
                {"text": "29. The company uses recycled paper to _____ its environmental impact.", "hint": "(reduce)"},
                {"text": "30. Good colour management depends _____ calibrated monitors and correct ICC profiles.", "hint": "(on)"},
            ],
        },
        "industrial": {
            "name": "Mecanica Industrial",
            "part1_questions": [
                {"q": "1. This position requires experience with automated machinery.",
                 "options": ["A) CNC OPERATOR REQUIRED - Minimum 2 years experience with Fanuc or Siemens controllers",
                             "B) TAXI DRIVER - Must have professional licence",
                             "C) CHEF NEEDED - Experience in international cuisine"]},
                {"q": "2. This area has strict rules about accuracy.",
                 "options": ["A) QUALITY CONTROL DEPARTMENT - All parts inspected to ISO 9001 standards",
                             "B) SPORTS FIELD - Play fair, respect the rules",
                             "C) KITCHEN - Measure ingredients carefully"]},
                {"q": "3. You must not go near this when it is moving.",
                 "options": ["A) ROTATING MACHINERY - Maintain safe distance. No loose clothing.",
                             "B) MERRY-GO-ROUND - Children under 12 must be accompanied",
                             "C) REVOLVING DOOR - Push gently"]},
                {"q": "4. The company needs someone who can fix equipment before it breaks.",
                 "options": ["A) PREVENTIVE MAINTENANCE TECHNICIAN WANTED - Industrial experience required",
                             "B) DOCTOR - Available for consultations Mon-Fri",
                             "C) CAR MECHANIC - Oil change special this week"]},
                {"q": "5. These new machines can work without people all day.",
                 "options": ["A) FULLY AUTOMATED PRODUCTION LINE - 24/7 unmanned operation capability",
                             "B) SELF-SERVICE LAUNDRY - Open 7 days a week",
                             "C) AUTOMATIC DOOR - Please wait for it to open"]},
                {"q": "6. Everything produced here must meet exact standards.",
                 "options": ["A) TOLERANCE: +/-0.005mm - Parts outside specification must be rejected",
                             "B) EXAM PASSING MARK: 60% - Results posted Friday",
                             "C) SPEED LIMIT: 50 km/h - Fines for exceeding"]},
            ],
            "part2_text": "Three industrial mechanics discuss their career paths and the importance of English.\n\nHernan has worked in CNC machining for twelve years. He started as a machine operator and is now a programming supervisor. He creates CNC programs for complex parts used in the aerospace industry. All technical specifications and client documents arrive in English. He says that without English, he would not have advanced to his current position.\n\nLorena works in maintenance for an automotive parts factory. She is responsible for keeping all production machines running. Her team performs preventive maintenance, repairs breakdowns, and upgrades equipment. When the factory installed new German robots last year, all the programming manuals were in English. Lorena's English skills made her the key person for the project.\n\nRicardo specializes in quality control at a precision machining company. He inspects parts using coordinate measuring machines (CMMs) and ensures they meet international standards (ISO 9001). He writes inspection reports in both Spanish and English because many of their clients are international. He also attends online quality management courses in English.",
            "part2_questions": [
                {"q": "7. Who works in aerospace manufacturing?", "options": ["A) Hernan", "B) Lorena", "C) Ricardo"]},
                {"q": "8. Who is responsible for factory maintenance?", "options": ["A) Hernan", "B) Lorena", "C) Ricardo"]},
                {"q": "9. Who writes reports in two languages?", "options": ["A) Hernan", "B) Lorena", "C) Ricardo"]},
                {"q": "10. Who was key for installing new robots?", "options": ["A) Hernan", "B) Lorena", "C) Ricardo"]},
                {"q": "11. Who uses coordinate measuring machines?", "options": ["A) Hernan", "B) Lorena", "C) Ricardo"]},
                {"q": "12. Who creates CNC programs?", "options": ["A) Hernan", "B) Lorena", "C) Ricardo"]},
                {"q": "13. Who takes quality management courses online?", "options": ["A) Hernan", "B) Lorena", "C) Ricardo"]},
            ],
            "part3_text": "Predictive Maintenance: The Future of Industrial Reliability\n\nPredictive maintenance is a strategy that uses data from sensors and artificial intelligence to predict when a machine is likely to fail. Instead of waiting for a breakdown (reactive maintenance) or replacing parts on a fixed schedule (preventive maintenance), predictive maintenance tells technicians exactly when intervention is needed.\n\nThe technology works by installing sensors on critical machines. These sensors measure vibration, temperature, noise, oil quality, and electrical consumption. The data is sent to a computer system that uses machine learning algorithms to detect patterns that indicate developing problems.\n\nFor example, a vibration sensor on a motor might detect increasing irregularities weeks before a bearing failure. The system alerts the maintenance team, who can then schedule a repair during planned downtime rather than experiencing an unexpected shutdown that stops production.\n\nThe benefits are significant. Studies show that predictive maintenance can reduce maintenance costs by 25-30%, reduce breakdowns by 70%, and increase machine life by 20-25%. These improvements translate into millions of dollars in savings for large factories.\n\nHowever, implementing predictive maintenance requires investment in sensors, software, and training. Technicians need new skills: data analysis, sensor technology, and understanding of AI systems. Most training programmes and software documentation are in English, making language skills essential for maintenance professionals.",
            "part3_questions": [
                {"q": "14. What does predictive maintenance use to predict failures?",
                 "options": ["A) Crystal balls and intuition", "B) Data from sensors and artificial intelligence", "C) Only visual inspections"]},
                {"q": "15. What do sensors measure on machines?",
                 "options": ["A) Only temperature", "B) Vibration, temperature, noise, oil quality and electrical consumption", "C) The colour of the machine"]},
                {"q": "16. What advantage does predictive maintenance have over reactive maintenance?",
                 "options": ["A) It is cheaper to install.", "B) It predicts problems before breakdowns happen.", "C) It does not require any technology."]},
                {"q": "17. How much can predictive maintenance reduce breakdowns?",
                 "options": ["A) By 10%", "B) By 30%", "C) By 70%"]},
                {"q": "18. What new skills do technicians need for predictive maintenance?",
                 "options": ["A) Cooking and cleaning", "B) Data analysis, sensor technology and understanding of AI", "C) Only traditional repair skills"]},
            ],
            "part4_sentences": [
                {"pre": "The CNC program must be carefully (19) _____ before running it on real material.",
                 "options": ["A) deleted", "B) simulated", "C) forgotten"]},
                {"pre": "A calliper is a precision instrument used to (20) _____ the dimensions of a part.",
                 "options": ["A) paint", "B) measure", "C) break"]},
                {"pre": "The factory (21) _____ new robots to increase production speed.",
                 "options": ["A) painted", "B) installed", "C) destroyed"]},
                {"pre": "Hydraulic oil must be (22) _____ regularly to maintain system performance.",
                 "options": ["A) drunk", "B) replaced", "C) frozen"]},
                {"pre": "The maintenance team works in (23) _____ to ensure the factory runs 24 hours a day.",
                 "options": ["A) silence", "B) shifts", "C) darkness"]},
                {"pre": "All machined parts must meet the required (24) _____ before being shipped to the client.",
                 "options": ["A) colours", "B) temperatures", "C) tolerances"]},
            ],
            "part5_sentences": [
                {"text": "25. The machine operator must check the tool _____ before each operation.", "hint": "(offset / settings)"},
                {"text": "26. A CNC machine is controlled _____ a computer program.", "hint": "(by)"},
                {"text": "27. The part was rejected because it was outside the _____ tolerance.", "hint": "(required / specified)"},
                {"text": "28. Predictive maintenance can reduce costs _____ up to 30%.", "hint": "(by)"},
                {"text": "29. The technician _____ wearing safety glasses when operating the lathe.", "hint": "(was / is)"},
                {"text": "30. Steel is an alloy made _____ iron and carbon.", "hint": "(of / from)"},
            ],
        },
    }
    
    d = sp_data[specialty]
    return {
        "level": "4to Medio",
        "specialty": d["name"],
        "filename": f"diagnostico_4to_{specialty}.pdf",
        "part1": {
            "instructions": "Questions 1-6\nWhich notice (A, B or C) says this?\nFor each question, choose the correct letter.",
            "questions": d["part1_questions"],
        },
        "part2": {
            "instructions": "Questions 7-13\nRead the text below about three professionals.\nFor each question, choose the correct answer (A, B or C).",
            "text": d["part2_text"],
            "questions": d["part2_questions"],
        },
        "part3": {
            "instructions": "Questions 14-18\nRead the text below and choose the correct answer (A, B or C) for each question.",
            "text": d["part3_text"],
            "questions": d["part3_questions"],
        },
        "part4": {
            "instructions": "Questions 19-24\nRead the text below and choose the correct word (A, B or C) for each space.",
            "text_before": "",
            "sentences": d["part4_sentences"],
        },
        "part5": {
            "instructions": "Questions 25-30\nRead the text below and write the missing word for each space.\nUse only ONE word for each space.",
            "sentences": d["part5_sentences"],
        }
    }


# ========== PDF GENERATION ==========

class DiagnosticPDF(FPDF):
    def __init__(self, logo_path, cuadro_path):
        super().__init__()
        self.logo_path = logo_path
        self.cuadro_path = cuadro_path
        # Add Unicode font (Windows Arial)
        self.add_font("ArialU", "", r"C:\Windows\Fonts\arial.ttf")
        self.add_font("ArialU", "B", r"C:\Windows\Fonts\arialbd.ttf")
        self.add_font("ArialU", "I", r"C:\Windows\Fonts\ariali.ttf")
        self.add_font("ArialU", "BI", r"C:\Windows\Fonts\arialbi.ttf")
    
    def header_block(self, level, specialty, year="2026"):
        """Custom header with logo and cuadro images."""
        # Logo - centered, proportional
        page_w = self.w - 20  # margins
        # Logo: 3780x1890 -> ratio 2:1
        logo_w = 60
        logo_h = 30
        logo_x = (self.w - logo_w) / 2
        self.image(self.logo_path, x=logo_x, y=8, w=logo_w, h=logo_h)
        self.ln(logo_h + 2)
        
        # Cuadro - full width below logo
        cuadro_w = page_w
        cuadro_h = cuadro_w / 2  # same 2:1 ratio
        cuadro_x = 10
        self.image(self.cuadro_path, x=cuadro_x, y=self.get_y(), w=cuadro_w, h=cuadro_h)
        self.ln(cuadro_h + 5)
        
        # Test title
        self.set_font("ArialU", "B", 14)
        title = "EVALUACION DIAGNOSTICA - INGLES"
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT", align="C")
        
        # Level and specialty
        self.set_font("ArialU", "B", 12)
        sub = level
        if specialty:
            sub += f" - {specialty}"
        self.cell(0, 7, sub, new_x="LMARGIN", new_y="NEXT", align="C")
        
        self.set_font("ArialU", "", 10)
        self.cell(0, 6, f"Ano Escolar {year}", new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(3)
        
        # Student info box
        self.set_font("ArialU", "", 10)
        self.set_draw_color(0)
        self.set_line_width(0.3)
        y0 = self.get_y()
        self.rect(10, y0, page_w, 24)
        self.set_xy(12, y0 + 2)
        self.cell(0, 6, "Nombre: ________________________________________     Curso: __________     Fecha: ___/___/2026")
        self.set_xy(12, y0 + 10)
        self.cell(0, 6, "Puntaje Total: ___ / 30 pts          Nota: ___          Exigencia: 60%")
        self.set_xy(12, y0 + 17)
        self.set_font("ArialU", "I", 9)
        self.cell(0, 5, "Instrucciones: Lee cada seccion cuidadosamente. Usa lapiz pasta azul o negro. Tienes 70 minutos.")
        self.set_y(y0 + 28)
        self.ln(2)

    def section_title(self, part_num, title):
        self.set_font("ArialU", "B", 11)
        self.set_fill_color(41, 98, 255)
        self.set_text_color(255, 255, 255)
        self.cell(0, 7, f"  PART {part_num} - {title}", new_x="LMARGIN", new_y="NEXT", fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def instructions_text(self, text):
        self.set_font("ArialU", "I", 9)
        self.multi_cell(0, 4.5, text)
        self.ln(2)

    def reading_text(self, text, title=""):
        if title:
            self.set_font("ArialU", "B", 10)
            self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("ArialU", "", 9)
        self.set_fill_color(245, 245, 245)
        x0 = self.get_x()
        y0 = self.get_y()
        # Draw background
        self.set_x(10)
        self.multi_cell(self.w - 20, 4.5, text.strip(), fill=True)
        self.ln(3)

    def question_mc(self, q_text, options):
        """Multiple choice question."""
        self.set_font("ArialU", "B", 9.5)
        # Check page break
        if self.get_y() > 260:
            self.add_page()
        self.multi_cell(0, 5, q_text)
        self.set_font("ArialU", "", 9)
        for opt in options:
            self.cell(8, 5, "")
            self.cell(0, 5, opt, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def question_gap(self, sentence, options):
        """Gap fill with options."""
        self.set_font("ArialU", "", 9.5)
        if self.get_y() > 262:
            self.add_page()
        self.multi_cell(0, 5, sentence)
        self.set_font("ArialU", "", 9)
        opts_text = "     ".join(options)
        self.cell(8, 5, "")
        self.cell(0, 5, opts_text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def question_write(self, sentence, hint=""):
        """Write one word question."""
        self.set_font("ArialU", "", 9.5)
        if self.get_y() > 265:
            self.add_page()
        self.multi_cell(0, 5, sentence)
        self.ln(2)


def generate_pdf(content):
    pdf = DiagnosticPDF(LOGO, CUADRO)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Header
    pdf.header_block(content["level"], content["specialty"])
    
    # ===== PART 1 =====
    pdf.section_title(1, "READING - Signs and Notices (6 points)")
    pdf.instructions_text(content["part1"]["instructions"])
    for q in content["part1"]["questions"]:
        pdf.question_mc(q["q"], q["options"])
    
    # ===== PART 2 =====
    if pdf.get_y() > 200:
        pdf.add_page()
    pdf.section_title(2, "READING - Matching (7 points)")
    pdf.instructions_text(content["part2"]["instructions"])
    pdf.reading_text(content["part2"]["text"])
    for q in content["part2"]["questions"]:
        pdf.question_mc(q["q"], q["options"])
    
    # ===== PART 3 =====
    if pdf.get_y() > 180:
        pdf.add_page()
    pdf.section_title(3, "READING - Comprehension (5 points)")
    pdf.instructions_text(content["part3"]["instructions"])
    pdf.reading_text(content["part3"]["text"])
    for q in content["part3"]["questions"]:
        pdf.question_mc(q["q"], q["options"])
    
    # ===== PART 4 =====
    if pdf.get_y() > 200:
        pdf.add_page()
    pdf.section_title(4, "READING - Vocabulary (6 points)")
    pdf.instructions_text(content["part4"]["instructions"])
    if content["part4"].get("text_before"):
        pdf.set_font("ArialU", "B", 10)
        pdf.cell(0, 6, content["part4"]["text_before"], new_x="LMARGIN", new_y="NEXT")
    for s in content["part4"]["sentences"]:
        pdf.question_gap(s["pre"], s["options"])
    
    # ===== PART 5 =====
    if pdf.get_y() > 220:
        pdf.add_page()
    pdf.section_title(5, "READING - Gap Fill (6 points)")
    pdf.instructions_text(content["part5"]["instructions"])
    for s in content["part5"]["sentences"]:
        pdf.question_write(s["text"])
    
    # Footer
    pdf.ln(5)
    pdf.set_font("ArialU", "I", 8)
    pdf.cell(0, 5, "- Fin de la evaluacion - Revisa tus respuestas antes de entregar. -", new_x="LMARGIN", new_y="NEXT", align="C")
    
    # Save
    filepath = os.path.join(OUT_DIR, content["filename"])
    pdf.output(filepath)
    return filepath


# ========== MAIN ==========

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    
    tests = []
    
    # 1ro Medio
    tests.append(get_1ro_medio_content())
    
    # 3ro Medio (5 specialties)
    for sp in ["automotriz", "electricidad", "electronica", "grafica", "industrial"]:
        tests.append(get_3ro_content(sp))
    
    # 4to Medio (5 specialties) 
    for sp in ["automotriz", "electricidad", "electronica", "grafica", "industrial"]:
        tests.append(get_4to_content(sp))
    
    # Generate all
    count = 0
    for test in tests:
        try:
            path = generate_pdf(test)
            level = test["level"]
            sp = f" - {test['specialty']}" if test["specialty"] else ""
            print(f"  OK: {test['filename']}  ({level}{sp})")
            count += 1
        except Exception as e:
            print(f"  ERROR: {test['filename']} - {e}")
    
    print(f"\n  {count} pruebas diagnosticas generadas en: {OUT_DIR}")
