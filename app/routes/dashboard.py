# app/routes/dashboard.py
import json
from pathlib import Path
from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/", methods=["GET"])
def home():
    folder = Path(__file__).resolve().parent.parent.parent / "generated_documents"
    podaci = []

    for f in folder.glob("*.json"):
        try:
            with open(f, encoding="utf-8") as json_file:
                entry = json.load(json_file)
                podaci.append(entry)
        except Exception:
            continue

    # sortiraj po datumu i uzmi najnovijih 5
    poslednji = sorted(podaci, key=lambda x: x.get("datum", ""), reverse=True)[:5]

    return render_template("dashboard.html", poslednji=poslednji)