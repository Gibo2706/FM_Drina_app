from flask import Blueprint, render_template, request, redirect, url_for, flash

ponuda_bp = Blueprint("ponuda", __name__)

@ponuda_bp.route("/", methods=["GET", "POST"])
def nova_ponuda():
    if request.method == "POST":
        # Ovde se uzimaju podaci iz forme
        klijent = request.form.get("klijent")
        lokacija = request.form.get("lokacija")
        opis = request.form.get("opis")
        cena = request.form.get("cena")
        datum = request.form.get("datum")

        # Validacija (osnovna)
        if not all([klijent, lokacija, opis, cena, datum]):
            flash("Sva polja su obavezna!", "danger")
            return redirect(url_for("ponuda.nova_ponuda"))

        # TODO: generisanje dokumenta

        flash("Ponuda uspešno generisana!", "success")
        return redirect(url_for("dashboard.home"))

    return render_template("ponuda_form.html")
