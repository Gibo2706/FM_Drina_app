from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils.doc_generator import generisi_ponudu, generisi_broj_ponude
from datetime import datetime

ponuda_bp = Blueprint("ponuda", __name__)

@ponuda_bp.route("/", methods=["GET", "POST"])
def nova_ponuda():
    predlog_broj_ponude = generisi_broj_ponude()

    if request.method == "POST":
        broj_ponude = request.form.get("broj_ponude") or predlog_broj_ponude
        klijent_naziv = request.form.get("klijent_naziv")
        klijent_adresa = request.form.get("klijent_adresa")
        klijent_grad = request.form.get("klijent_grad")
        klijent_pib = request.form.get("klijent_pib")
        klijent_mb = request.form.get("klijent_mb")
        opis_ponude = request.form.get("opis_ponude")
        stavke_ponude = request.form.get("stavke_ponude")
        datum = request.form.get("datum")

        if not all([
            klijent_naziv, klijent_adresa, klijent_grad,
            klijent_pib, klijent_mb, broj_ponude,
            opis_ponude, stavke_ponude, datum
        ]):
            flash("Sva polja su obavezna!", "danger")
            return redirect(url_for("ponuda.nova_ponuda"))

        data = {
            "klijent_naziv": klijent_naziv,
            "klijent_adresa": klijent_adresa,
            "klijent_grad": klijent_grad,
            "klijent_pib": klijent_pib,
            "klijent_mb": klijent_mb,
            "klijent_potpis": klijent_naziv,
            "broj_ponude": broj_ponude,
            "opis_ponude": opis_ponude,
            "stavke_ponude": stavke_ponude,
            "datum": datum
        }

        fajl = generisi_ponudu(data)
        flash(f"✅ Ponuda generisana: <a href='/ponude/{fajl}' class='alert-link' download>Preuzmi fajl</a>", "success")
        return redirect(url_for("ponuda.nova_ponuda"))

    return render_template("ponuda_form.html", predlog_broj_ponude=predlog_broj_ponude)
