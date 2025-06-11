from docxtpl import DocxTemplate
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_PATH = BASE_DIR / "app" / "templates" / "docx_templates" / "ponuda_template.docx"
OUTPUT_DIR = BASE_DIR / "generated_documents"
OUTPUT_DIR.mkdir(exist_ok=True)

def generisi_ponudu(data: dict) -> str:
    doc = DocxTemplate(TEMPLATE_PATH)
    doc.render(data)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    safe_name = data['klijent_naziv'].replace(" ", "_").replace(".", "").replace(",", "")
    naziv_fajla = f"Ponuda_{safe_name}_{timestamp}.docx"
    putanja = OUTPUT_DIR / naziv_fajla

    doc.save(putanja)
    return naziv_fajla  # samo ime fajla, ne puna putanja
