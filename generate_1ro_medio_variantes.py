#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pathlib import Path

BASE = Path(r"c:\Users\crist\OneDrive\Escritorio\2026\1ro Medio")

UNIT_FILES = {
    1: BASE / "Unidad 1" / "planificacion_unidad1.html",
    2: BASE / "Unidad 2" / "planificacion_unidad2.html",
    3: BASE / "Unidad 3" / "planificacion_unidad3.html",
    4: BASE / "Unidad 4" / "planificacion_unidad4.html",
}

VERSIONS = {
    "lu_vi": {
        "label": "Versión horario Lu+Vi (1°A, 1°C, 1°D)",
        "units": {
            1: {"date": "4 marzo – 3 mayo", "sessions": "15 sesiones de 90 min"},
            2: {"date": "4 mayo – 21 junio", "sessions": "14 sesiones de 90 min"},
            3: {"date": "6 julio – 20 septiembre", "sessions": "20 sesiones de 90 min (sin clases 14–20 sept.)"},
            4: {"date": "21 septiembre – 12 diciembre", "sessions": "20 sesiones de 90 min"},
        },
    },
    "lu_ju": {
        "label": "Versión horario Lu+Ju (1°B, 1°E)",
        "units": {
            1: {"date": "4 marzo – 3 mayo", "sessions": "17 sesiones de 90 min"},
            2: {"date": "4 mayo – 21 junio", "sessions": "13 sesiones de 90 min"},
            3: {"date": "6 julio – 20 septiembre", "sessions": "19 sesiones de 90 min (sin clases 14–20 sept.)"},
            4: {"date": "21 septiembre – 12 diciembre", "sessions": "20 sesiones de 90 min"},
        },
    },
}


def replace_first(pattern: str, replacement: str, text: str) -> str:
    return re.sub(pattern, replacement, text, count=1, flags=re.S)


def _get_class_number(block: str) -> int:
    m = re.search(r"CLASE\s+(\d+)", block)
    if m:
        return int(m.group(1))
    m = re.search(r">Clase\s+(\d+)<", block)
    return int(m.group(1)) if m else 0


def _renumber_block(block: str, new_number: int) -> str:
    block = re.sub(r"(CLASE\s+)\d+", rf"\g<1>{new_number}", block, count=1)
    block = re.sub(r'(<span class="clase-num">Clase\s+)\d+(</span>)', rf"\g<1>{new_number}\g<2>", block, count=1)
    return block


def _fit_class_blocks_to_total(content: str, target_total: int) -> str:
    class_start = re.search(r"<!--\s*=+\s*CLASE\s+\d+\s*=+\s*-->", content)
    if not class_start:
        return content

    notes_start_idx = content.find('<div class="notas-dist">', class_start.start())
    if notes_start_idx == -1:
        return content

    prefix = content[:class_start.start()]
    classes_section = content[class_start.start():notes_start_idx]
    suffix = content[notes_start_idx:]

    starts = [m.start() for m in re.finditer(r"<!--\s*=+\s*CLASE\s+\d+\s*=+\s*-->", classes_section)]
    starts.append(len(classes_section))
    blocks = [classes_section[starts[i]:starts[i + 1]] for i in range(len(starts) - 1)]

    parsed = []
    for block in blocks:
        parsed.append(
            {
                "old": _get_class_number(block),
                "is_eval": 'clase-card evaluacion' in block,
                "block": block,
            }
        )

    eval_blocks = [p for p in parsed if p["is_eval"]]
    normal_blocks = [p for p in parsed if not p["is_eval"]]

    if target_total >= len(parsed):
        kept = parsed
    else:
        normal_slots = max(0, target_total - len(eval_blocks))
        kept = normal_blocks[:normal_slots] + eval_blocks

    kept = sorted(kept, key=lambda x: x["old"])

    old_to_new = {}
    rebuilt_blocks = []
    for idx, item in enumerate(kept, start=1):
        old_to_new[item["old"]] = idx
        rebuilt_blocks.append(_renumber_block(item["block"], idx))

    merged = prefix + "".join(rebuilt_blocks) + suffix

    eval_old = [p["old"] for p in eval_blocks if p["old"] in old_to_new]
    eval_new = [old_to_new[n] for n in eval_old]
    if len(eval_old) >= 2:
        merged = merged.replace(f"Clases {eval_old[0]}–{eval_old[1]}", f"Clases {eval_new[0]}–{eval_new[1]}")
        merged = merged.replace(f"Clases {eval_old[0]}-{eval_old[1]}", f"Clases {eval_new[0]}-{eval_new[1]}")
    if len(eval_old) >= 1:
        merged = re.sub(rf"\bClase\s+{eval_old[-1]}\b", f"Clase {eval_new[-1]}", merged)

    return merged


def adapt_html(content: str, unit_number: int, version_key: str) -> str:
    version = VERSIONS[version_key]
    unit = version["units"][unit_number]

    subtitle_repl = (
        f'<p class="subtitle">Inglés — Liceo Técnico Profesional — Año Escolar 2026 — '
        f'{version["label"]}</p>'
    )
    content = replace_first(r'<p class="subtitle">.*?</p>', subtitle_repl, content)

    meta_block = (
        '<div class="meta-info">\n'
        f'        <span>📅 {unit["date"]}</span>\n'
        f'        <span>⏱ {unit["sessions"]}</span>\n'
        '        <span>📚 4 hrs/semana (2 sesiones)</span>\n'
        '        <span>🎯 Ajustada a calendario 2026 + feriados Chile</span>\n'
        '    </div>'
    )
    content = replace_first(r'<div class="meta-info">.*?</div>', meta_block, content)

    if unit_number == 1:
        content = content.replace(
            '<strong>Evaluaciones de la unidad:</strong>',
            '<strong>Evaluaciones de la unidad:</strong><br><small>Distribución Semestre 1: 2 notas en U1 y 3 notas en U2.</small>',
            1,
        )

    target_total = int(re.search(r"(\d+)\s+sesiones", unit["sessions"]).group(1))
    content = _fit_class_blocks_to_total(content, target_total)

    return content


def main():
    created = 0
    for unit_number, source_file in UNIT_FILES.items():
        source = source_file.read_text(encoding="utf-8")
        for version_key in VERSIONS:
            adapted = adapt_html(source, unit_number, version_key)
            output = source_file.with_name(f"planificacion_unidad{unit_number}_{version_key}.html")
            output.write_text(adapted, encoding="utf-8")
            created += 1
            print(f"✓ Created: {output}")

    print(f"\n✅ {created} variantes generadas para 1° Medio")


if __name__ == "__main__":
    main()
