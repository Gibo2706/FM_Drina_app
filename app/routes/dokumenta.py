from flask import Blueprint, render_template
from pathlib import Path

dokumenti_bp = Blueprint("dokumenti", __name__)

@dokumenti_bp.route("/", methods=["GET"])
def prikaz_dokumenata():
    folder = Path(__file__).resolve().parent.parent.parent / "generated_documents"
    fajlovi = sorted([f.name for f in folder.glob("*.docx")], reverse=True)
    return render_template("dokumenti.html", fajlovi=fajlovi)
