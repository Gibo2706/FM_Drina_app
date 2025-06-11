from flask import Blueprint, render_template
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
    return render_template("dokumenti.html", ponude=podaci)

