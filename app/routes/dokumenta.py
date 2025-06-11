from flask import Blueprint, render_template
from flask import send_from_directory, flash, redirect, url_for
import subprocess
from pathlib import Path
import json


dokumenti_bp = Blueprint("dokumenti", __name__)

@dokumenti_bp.route("/", methods=["GET"])
def prikaz_dokumenata():
    folder = Path(__file__).resolve().parent.parent.parent / "generated_documents"
    podaci = []

    for json_file in folder.glob("*.json"):
        try:
            with open(json_file, encoding="utf-8") as f:
                entry = json.load(f)
                podaci.append(entry)
        except Exception:
            continue

    podaci.sort(key=lambda x: x.get("datum", ""), reverse=True)

    # ✅ Dodaj proveru postojećih PDF-ova
    existing_pdfs = {f.name for f in folder.glob("*.pdf")}

    return render_template("dokumenti.html", ponude=podaci, existing_pdfs=existing_pdfs)



@dokumenti_bp.route("/regenerisi-pdf/<filename>")
def regenerisi_pdf(filename):
    folder = Path(__file__).resolve().parent.parent.parent / "generated_documents"
    docx_path = folder / filename

    if not docx_path.exists() or not docx_path.suffix == ".docx":
        flash("❌ Neispravan dokument!", "danger")
        return redirect(url_for("dokumenti.prikaz_dokumenata"))

    try:
        subprocess.run([
            "soffice", "--headless", "--convert-to", "pdf", "--outdir", str(folder), str(docx_path)
        ], check=True)
        flash("✅ PDF uspešno regenerisan.", "success")
    except Exception as e:
        flash(f"❌ Greška: PDF nije regenerisan. {e}", "danger")

    return redirect(url_for("dokumenti.prikaz_dokumenata"))
