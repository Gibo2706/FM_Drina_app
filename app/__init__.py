import os
from flask import Flask, send_from_directory
from dotenv import load_dotenv
from pathlib import Path

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "default_key")

    from .routes.dashboard import dashboard_bp
    from .routes.ponuda import ponuda_bp
    from .routes.dokumenta import dokumenti_bp

    app.register_blueprint(dashboard_bp, url_prefix="/filip")
    app.register_blueprint(ponuda_bp, url_prefix="/filip/ponuda")
    app.register_blueprint(dokumenti_bp, url_prefix="/filip/dokumenti")


    # ✅ Dodaj rutu ovde – UNUTAR funkcije
    @app.route('/ponude/<path:filename>')
    def preuzmi_ponudu(filename):
        folder = Path(__file__).resolve().parent.parent / "generated_documents"
        return send_from_directory(folder, filename, as_attachment=True)

    return app
