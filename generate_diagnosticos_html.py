from __future__ import annotations

import re
import random
from pathlib import Path
from collections import Counter

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent
DIAG_DIR = ROOT / "Pruebas Diagnostico"

LABELS = ["A", "B", "C", "D", "E"]

FILLER_PATTERNS = [
    r"\bthis task\b",
    r"\bin a different workshop situation\b",
    r"\bfor another related classroom context\b",
    r"\bin the same technical context(?: for this)?\b",
    r"\bthe same technical context(?: for this)?\b",
    r"\bsame technical context(?: for this)?\b",
    r"\bfor this task in the same technical\b",
    r"\bin the same technical\b",
    r"\bfor this\b",
    r"\bfor at school\b",
    r"\bcontext for at school\b",
    r"\bat school\b",
    r"\bin class\b",
]

TRAILING_FILLER_TOKENS = {
    "for",
    "in",
    "the",
    "same",
    "task",
    "context",
    "technical",
}

NAME_DISTRACTORS = ["Camila", "Diego", "Valentina", "Matias", "Fernanda", "Javier"]

GENERIC_DISTRACTORS = [
    "Follow the workshop protocol before starting any task",
    "Check the safety rules before using the equipment",
    "Ask the teacher for instructions before continuing",
    "Review the technical guide before choosing the answer",
    "Complete the activity according to class procedure",
]

SPECIALTY_BANK = {
    "automotriz": [
        "Inspect the brake fluid before the road test",
        "Use the diagnostic scanner to check engine codes",
        "Replace the air filter during regular maintenance",
        "Adjust tyre pressure according to workshop standards",
        "Check battery terminals before starting the vehicle",
        "Review the service manual before repairing the engine",
    ],
    "electricidad": [
        "Turn off the main breaker before touching any wire",
        "Use a multimeter to measure voltage safely",
        "Label each cable before connecting the circuit",
        "Check insulation damage before installing the panel",
        "Test continuity before powering the electrical system",
        "Follow lockout procedures before maintenance work",
    ],
    "electronica": [
        "Check resistor values before soldering the board",
        "Use antistatic protection when handling components",
        "Measure current carefully with the digital meter",
        "Verify polarity before connecting the capacitor",
        "Test the circuit on a breadboard first",
        "Read the datasheet before replacing the microchip",
    ],
    "grafica": [
        "Check colour calibration before final printing",
        "Review image resolution before exporting the file",
        "Use crop marks to align the printed design",
        "Adjust contrast levels before sending to press",
        "Confirm page margins in the layout software",
        "Select the correct paper type for the project",
    ],
    "industrial": [
        "Check machine guards before starting production",
        "Read the safety checklist before operating equipment",
        "Measure each metal part with a vernier caliper",
        "Inspect weld quality before assembling the structure",
        "Use protective equipment during cutting operations",
        "Follow maintenance steps from the technical manual",
    ],
    "general": [
        "Read the instructions carefully before answering",
        "Check your notes before choosing an option",
        "Follow safety rules during practical activities",
        "Use technical vocabulary from the current unit",
        "Review examples before completing the exercise",
        "Confirm your answer before moving to the next item",
    ],
}

GAP_WORD_BANK = {
    "automotriz": [
        "inspect",
        "adjust",
        "replace",
        "repair",
        "test",
        "service",
        "engine",
        "brakes",
        "filter",
        "battery",
        "coolant",
        "torque",
    ],
    "electricidad": [
        "measure",
        "install",
        "connect",
        "protect",
        "switch",
        "verify",
        "cable",
        "voltage",
        "current",
        "breaker",
        "circuit",
        "panel",
    ],
    "electronica": [
        "solder",
        "assemble",
        "connect",
        "test",
        "program",
        "verify",
        "sensor",
        "resistor",
        "transistor",
        "voltage",
        "signal",
        "board",
    ],
    "grafica": [
        "print",
        "design",
        "adjust",
        "edit",
        "export",
        "prepare",
        "colour",
        "layout",
        "format",
        "margin",
        "contrast",
        "resolution",
    ],
    "industrial": [
        "measure",
        "operate",
        "install",
        "check",
        "inspect",
        "maintain",
        "tolerance",
        "pressure",
        "shift",
        "welding",
        "lathe",
        "caliper",
    ],
    "general": [
        "check",
        "review",
        "complete",
        "follow",
        "correct",
        "answer",
        "safely",
        "carefully",
        "quickly",
        "clearly",
        "notes",
        "guide",
    ],
}

GAP_FORM_BANK = {
    "automotriz": {
        "base": ["inspect", "adjust", "replace", "repair", "test", "service"],
        "past": ["inspected", "adjusted", "replaced", "repaired", "tested", "serviced"],
        "noun": ["scanner", "engine", "battery", "coolant", "torque", "workshop"],
        "plural": ["filters", "brakes", "gears", "tyres", "manuals", "codes"],
    },
    "electricidad": {
        "base": ["measure", "install", "connect", "protect", "verify", "test"],
        "past": ["measured", "installed", "connected", "protected", "verified", "tested"],
        "noun": ["voltage", "current", "circuit", "breaker", "panel", "cable"],
        "plural": ["circuits", "cables", "panels", "fuses", "wires", "meters"],
    },
    "electronica": {
        "base": ["solder", "assemble", "connect", "test", "program", "verify"],
        "past": ["soldered", "assembled", "connected", "tested", "programmed", "verified"],
        "noun": ["resistor", "sensor", "signal", "voltage", "board", "transistor"],
        "plural": ["resistors", "sensors", "signals", "boards", "chips", "circuits"],
    },
    "grafica": {
        "base": ["print", "design", "adjust", "edit", "export", "prepare"],
        "past": ["printed", "designed", "adjusted", "edited", "exported", "prepared"],
        "noun": ["layout", "margin", "contrast", "colour", "format", "resolution"],
        "plural": ["layouts", "margins", "colours", "formats", "images", "layers"],
    },
    "industrial": {
        "base": ["measure", "operate", "install", "check", "inspect", "maintain"],
        "past": ["measured", "operated", "installed", "checked", "inspected", "maintained"],
        "noun": ["tolerance", "pressure", "welding", "lathe", "caliper", "maintenance"],
        "plural": ["tolerances", "tools", "shifts", "parts", "machines", "bolts"],
    },
    "general": {
        "base": ["check", "review", "complete", "follow", "correct", "answer"],
        "past": ["checked", "reviewed", "completed", "followed", "corrected", "answered"],
        "noun": ["guide", "answer", "class", "topic", "exercise", "example"],
        "plural": ["notes", "answers", "classes", "topics", "examples", "rules"],
    },
}


def strip_label(option_text: str) -> str:
    return re.sub(r"^[A-E]\)\s*", "", option_text).strip()


def tokenize(text: str) -> list[str]:
    return [token for token in text.split() if token.strip()]


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_option_text(text: str) -> str:
    cleaned = normalize_spaces(strip_label(text))
    for pattern in FILLER_PATTERNS:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)

    cleaned = re.sub(r"\s+([,.!?;:])", r"\1", cleaned)
    cleaned = normalize_spaces(cleaned)
    cleaned = cleaned.strip(" -")

    tokens = tokenize(cleaned)
    while tokens and tokens[-1].lower() in TRAILING_FILLER_TOKENS:
        tokens.pop()
    cleaned = " ".join(tokens).strip(" -")

    if not cleaned:
        cleaned = "Review the technical information before answering"

    if cleaned.endswith("without"):
        cleaned = f"{cleaned} supervisor approval"

    return cleaned


def is_name_list(options: list[str]) -> bool:
    if not options:
        return False
    for option in options:
        words = tokenize(option)
        if len(words) != 1:
            return False
        if not words[0][0].isupper():
            return False
    return True


def unique_keep_order(values: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(value)
    return out


def detect_specialty(file_name: str) -> str:
    lower = file_name.lower()
    if "automotriz" in lower:
        return "automotriz"
    if "electricidad" in lower:
        return "electricidad"
    if "electronica" in lower:
        return "electronica"
    if "grafica" in lower:
        return "grafica"
    if "industrial" in lower:
        return "industrial"
    return "general"


def extract_question_number(question_div) -> int | None:
    q_text_tag = question_div.find("p", class_="q-text")
    if not q_text_tag:
        return None
    text = q_text_tag.get_text(" ", strip=True)
    match = re.search(r"\b(\d{1,2})\b", text)
    if not match:
        return None
    number = int(match.group(1))
    if 1 <= number <= 30:
        return number
    return None


def parse_option_divs(question_div) -> list[tuple[str, str]]:
    options = []
    for opt in question_div.find_all("div", class_="option", recursive=False):
        text = clean_option_text(opt.get_text(" ", strip=True))
        m = re.match(r"^([A-E])\)\s*(.*)$", opt.get_text(" ", strip=True))
        label = m.group(1) if m else ""
        if text:
            options.append((label, text))
    return options


def parse_inline_options(question_div) -> list[tuple[str, str]]:
    inline = question_div.find("p", class_="options-inline")
    if not inline:
        return []
    raw = inline.get_text(" ", strip=True).replace("\xa0", " ")
    parts = re.split(r"\b([A-E])\)\s*", raw)
    options: list[tuple[str, str]] = []
    for i in range(1, len(parts), 2):
        label = parts[i].strip()
        text = clean_option_text(parts[i + 1]) if i + 1 < len(parts) else ""
        if label in LABELS and text:
            options.append((label, text))
    return options


def is_gapfill_question(question_div) -> bool:
    classes = question_div.get("class", [])
    return "gap-fill" in classes or question_div.find("p", class_="options-inline") is not None


def get_answer_key_map(soup: BeautifulSoup) -> dict[int, str]:
    mapping: dict[int, str] = {}
    for item in soup.select(".answer-grid .answer-item"):
        raw = item.get_text(" ", strip=True)
        m = re.match(r"^(\d+)\.\s*(.+)$", raw)
        if not m:
            continue
        num = int(m.group(1))
        ans = m.group(2).strip()
        mapping[num] = ans
    return mapping


def set_answer_key_value(soup: BeautifulSoup, number: int, new_value: str) -> None:
    for item in soup.select(".answer-grid .answer-item"):
        raw = item.get_text(" ", strip=True)
        if not raw.startswith(f"{number}."):
            continue
        num_span = item.find("span", class_="ans-num")
        if num_span:
            item.clear()
            item.append(num_span)
            num_span.insert_after(f" {new_value}")
        break


def overlap_score(question_text: str, candidate: str) -> int:
    q_words = {w.lower() for w in tokenize(re.sub(r"[^A-Za-z0-9 ]", " ", question_text)) if len(w) > 2}
    c_words = {w.lower() for w in tokenize(re.sub(r"[^A-Za-z0-9 ]", " ", candidate)) if len(w) > 2}
    return len(q_words.intersection(c_words))


def build_balanced_label_map(file_stem: str, max_question: int = 24) -> dict[int, str]:
    rng = random.Random(file_stem)
    labels = LABELS.copy()
    rng.shuffle(labels)

    counts = {label: max_question // len(LABELS) for label in LABELS}
    remainder = max_question % len(LABELS)
    for label in labels[:remainder]:
        counts[label] += 1

    bag: list[str] = []
    for label in LABELS:
        bag.extend([label] * counts[label])

    rng.shuffle(bag)
    return {index + 1: bag[index] for index in range(max_question)}


def select_distractors(correct_text: str, current_options: list[str], pool: list[str], question_text: str) -> list[str]:
    used = {correct_text.lower()}
    base = [opt for opt in current_options if opt.lower() not in used]
    candidates = unique_keep_order(base + pool + GENERIC_DISTRACTORS)
    candidates = [c for c in candidates if c.lower() not in used]

    if is_name_list([correct_text] + current_options):
        names = [name for name in NAME_DISTRACTORS if name.lower() not in used]
        return names[:4]

    target_len = len(tokenize(correct_text))

    scored = sorted(
        candidates,
        key=lambda c: (
            -overlap_score(question_text, c),
            abs(len(tokenize(c)) - target_len),
        ),
    )

    picked: list[str] = []
    for cand in scored:
        key = cand.lower()
        if key in used:
            continue
        used.add(key)
        picked.append(cand)
        if len(picked) == 4:
            break

    while len(picked) < 4:
        fallback = GENERIC_DISTRACTORS[len(picked) % len(GENERIC_DISTRACTORS)]
        if fallback.lower() not in used:
            picked.append(fallback)
            used.add(fallback.lower())
        else:
            picked.append(f"Review the technical procedure before answering option {len(picked) + 1}")

    return picked


def select_gapfill_distractors(correct_text: str, current_options: list[str], specialty: str) -> list[str]:
    correct = clean_option_text(correct_text)
    correct_words = len(tokenize(correct))
    if correct_words == 0:
        correct_words = 1

    def infer_form() -> str:
        low = correct.lower()
        words = tokenize(low)
        if len(words) >= 2:
            return "noun"
        if low.endswith("ed"):
            return "past"
        if low.endswith("s") and len(low) > 3:
            return "plural"
        return "base"

    form = infer_form()
    form_bank = GAP_FORM_BANK.get(specialty, GAP_FORM_BANK["general"])
    preferred = form_bank.get(form, [])
    fallback_form = GAP_FORM_BANK["general"].get(form, [])

    candidates = unique_keep_order(
        [clean_option_text(opt) for opt in current_options]
        + preferred
        + fallback_form
        + GAP_WORD_BANK.get(specialty, [])
        + GAP_WORD_BANK["general"]
    )

    filtered: list[str] = []
    used = {correct.lower()}
    for cand in candidates:
        key = cand.lower()
        if key in used:
            continue
        token_count = len(tokenize(cand))
        if 1 <= token_count <= 2 and abs(token_count - correct_words) <= 1:
            filtered.append(cand)
            used.add(key)
        if len(filtered) == 4:
            break

    while len(filtered) < 4:
        fallback = GAP_WORD_BANK["general"][len(filtered) % len(GAP_WORD_BANK["general"])]
        if fallback.lower() not in used:
            filtered.append(fallback)
            used.add(fallback.lower())
        else:
            filtered.append(f"term{len(filtered)+1}")

    return filtered[:4]


def rebuild_option_set(
    question_number: int,
    question_text: str,
    options: list[tuple[str, str]],
    answer_map: dict[int, str],
    pool: list[str],
    label_map: dict[int, str],
    specialty: str,
    gapfill_mode: bool,
) -> tuple[list[tuple[str, str]], str | None]:
    if question_number not in answer_map:
        return options, None

    correct_key = answer_map[question_number].strip().upper()
    if correct_key not in LABELS:
        return options, None

    option_dict = {label: text for label, text in options if label in LABELS}
    correct_text = option_dict.get(correct_key)
    if not correct_text and options:
        correct_text = options[0][1]
    if not correct_text:
        return options, None

    current_texts = [text for _, text in options]
    if gapfill_mode:
        distractors = select_gapfill_distractors(correct_text, current_texts, specialty)
    else:
        distractors = select_distractors(correct_text, current_texts, pool, question_text)

    target_label = label_map.get(question_number, LABELS[(question_number - 1) % len(LABELS)])
    final_map: dict[str, str] = {target_label: correct_text}

    other_labels = [label for label in LABELS if label != target_label]
    for idx, label in enumerate(other_labels):
        final_map[label] = distractors[idx]

    rebuilt = [(label, final_map[label]) for label in LABELS]
    return rebuilt, target_label


def write_option_divs(soup: BeautifulSoup, question_div, options: list[tuple[str, str]]) -> None:
    for old_div in question_div.find_all("div", class_="option", recursive=False):
        old_div.decompose()
    for label, text in options:
        new_div = soup.new_tag("div")
        new_div["class"] = ["option"]
        new_div.string = f"{label}) {text}"
        question_div.append(new_div)


def write_inline_options(question_div, options: list[tuple[str, str]]) -> None:
    inline = question_div.find("p", class_="options-inline")
    if not inline:
        return
    sep = "  \u00a0\u00a0\u00a0  "
    inline.string = sep.join(f"{label}) {text}" for label, text in options)


def process_file(file_path: Path) -> tuple[int, int]:
    html = file_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    specialty = detect_specialty(file_path.name)
    specialty_pool = SPECIALTY_BANK.get(specialty, SPECIALTY_BANK["general"])
    answer_map = get_answer_key_map(soup)
    label_map = build_balanced_label_map(file_path.stem, 24)

    total_questions = 0
    updated_questions = 0

    part_divs = soup.select("div.page:not(.answer-key) div.part")
    for part in part_divs:
        questions = part.find_all("div", class_="question", recursive=False)
        if not questions:
            continue

        part_pool: list[str] = []
        for question in questions:
            opts = parse_option_divs(question) or parse_inline_options(question)
            if not opts:
                continue
            part_pool.extend([text for _, text in opts])

        combined_pool = unique_keep_order(part_pool + specialty_pool + SPECIALTY_BANK["general"])

        for question in questions:
            question_number = extract_question_number(question)
            if question_number is None:
                continue

            options = parse_option_divs(question)
            is_inline = False
            if not options:
                options = parse_inline_options(question)
                is_inline = bool(options)
            if not options:
                continue

            q_text = question.find("p", class_="q-text")
            q_text_value = q_text.get_text(" ", strip=True) if q_text else ""

            rebuilt, new_key = rebuild_option_set(
                question_number,
                q_text_value,
                options,
                answer_map,
                combined_pool,
                label_map,
                specialty,
                is_gapfill_question(question),
            )

            total_questions += 1
            if rebuilt:
                if is_inline:
                    write_inline_options(question, rebuilt)
                else:
                    write_option_divs(soup, question, rebuilt)
                if new_key:
                    set_answer_key_value(soup, question_number, new_key)
                updated_questions += 1

    html_out = str(soup)
    html_out = html_out.replace("(A, B or C)", "(A, B, C, D or E)")
    html_out = html_out.replace("(A or B)", "(A, B, C, D or E)")
    html_out = html_out.replace("correct letter.", "correct letter (A-E).")
    html_out = html_out.replace("correct answer (A, B or C)", "correct answer (A, B, C, D or E)")
    html_out = html_out.replace("correct word (A, B or C)", "correct word (A, B, C, D or E)")

    file_path.write_text(html_out, encoding="utf-8")
    return total_questions, updated_questions


def main() -> None:
    files = sorted(DIAG_DIR.glob("diagnostico_*.html"))
    if not files:
        print("No se encontraron pruebas HTML en Pruebas Diagnostico/")
        return

    print("Ajustando alternativas a 5 opciones (A-E) y longitud equilibrada...\n")
    global_counter = Counter()
    for file_path in files:
        total, updated = process_file(file_path)
        print(f"OK: {file_path.name}  | preguntas: {total} | ajustadas: {updated}")

        soup = BeautifulSoup(file_path.read_text(encoding="utf-8"), "html.parser")
        for item in soup.select(".answer-grid .answer-item"):
            raw = item.get_text(" ", strip=True)
            m = re.match(r"^(\d+)\.\s*([A-E])$", raw)
            if not m:
                continue
            num = int(m.group(1))
            if 1 <= num <= 24:
                global_counter[m.group(2)] += 1

    if global_counter:
        dist = ", ".join(f"{label}:{global_counter.get(label, 0)}" for label in LABELS)
        print(f"\nDistribución global de respuestas 1-24 -> {dist}")

    print("\nProceso completado.")


if __name__ == "__main__":
    main()
