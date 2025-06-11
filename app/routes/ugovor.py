from flask import Blueprint, render_template, request, redirect, url_for, flash
from pathlib import Path
from datetime import datetime
import json
from app.utils.doc_generator import generisi_ugovor  # još ćemo je definisati

ugovor_bp = Blueprint("ugovor", __name__)

@ugovor_bp.route("/", methods=["GET", "POST"])
def novi_ugovor():
    defaults_path = Path(__file__).resolve().parent.parent / "defaults" / "clanovi.json"
    with open(defaults_path, encoding="utf-8") as f:
        default_clauses = json.load(f)

    if request.method == "POST":
        try:
            data = {
                "datum": request.form.get("datum"),
                "narucilac_naziv": request.form.get("narucilac_naziv"),
                "narucilac_adresa": request.form.get("narucilac_adresa"),
                "narucilac_pib": request.form.get("narucilac_pib"),
                "narucilac_mb": request.form.get("narucilac_mb"),
                "izvodjac_naziv": request.form.get("izvodjac_naziv"),
                "izvodjac_adresa": request.form.get("izvodjac_adresa"),
                "izvodjac_pib": request.form.get("izvodjac_pib"),
                "izvodjac_mb": request.form.get("izvodjac_mb"),
                "povezana_ponuda": request.form.get("povezana_ponuda") or "",
                "tip": "ugovor"
            }

            # Učitavanje sadržaja svih klauzula
            # Sva polja iz forme koja idu u docx
            for key in [
                "opis_radova", "cena_radova", "nacin_placanja", "obaveze_narucioca",
                "obaveze_izvodjaca", "dodatne_klauzule", "nadzor",
                "kvalitet_materijala", "primopredaja", "garancija", "zavrsne_odredbe"
            ]:
                data[key] = request.form.get(key)


            # Generiši ugovor
            fajl = generisi_ugovor(data)
            flash(f"✅ Ugovor generisan: <a href='/ponude/{fajl}' class='alert-link' download>Preuzmi fajl</a>", "success")
            return redirect(url_for("ugovor.novi_ugovor"))
        except Exception as e:
            flash(f"Greška prilikom generisanja ugovora: {e}", "danger")

    return render_template("ugovor_form.html", default_clauses=default_clauses)

@ugovor_bp.route("/update-default", methods=["POST"])
def update_default_clan():
    key = request.form.get("key")
    text = request.form.get("text")

    path = Path(__file__).resolve().parent.parent / "defaults" / "clanovi.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data[key] = text

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return "OK", 200
    except Exception as e:
        return f"Greška: {str(e)}", 500
