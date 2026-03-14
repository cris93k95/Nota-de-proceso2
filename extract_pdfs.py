import fitz  # PyMuPDF
import os

pdf_folder = r"c:\Users\crist\OneDrive\Escritorio\2026\Planes y programas"
output_folder = r"c:\Users\crist\OneDrive\Escritorio\2026\textos_extraidos"

os.makedirs(output_folder, exist_ok=True)

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    txt_name = pdf_file.replace('.pdf', '.txt')
    txt_path = os.path.join(output_folder, txt_name)
    
    print(f"Extrayendo: {pdf_file}...")
    doc = fitz.open(pdf_path)
    
    full_text = []
    for page_num, page in enumerate(doc, 1):
        text = page.get_text()
        if text.strip():
            full_text.append(f"--- PÁGINA {page_num} ---\n{text}")
    
    doc.close()
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(full_text))
    
    print(f"  -> {txt_name} ({len(full_text)} páginas con texto)")

print("\n¡Extracción completada!")
