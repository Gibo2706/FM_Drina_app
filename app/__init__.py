import os
from flask import Flask, send_from_directory, request, Response
from dotenv import load_dotenv
from pathlib import Path

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "default_key")

    USERNAME = os.getenv("FILIP_USER")
    PASSWORD = os.getenv("FILIP_PASS")

    @app.before_request
    def basic_auth():
        if request.path.startswith("/filip"):
            auth = request.authorization
            if not auth or not (auth.username == USERNAME and auth.password == PASSWORD):
                return Response(
                    "⛔ Za pristup je potrebna autorizacija", 401,
                    {"WWW-Authenticate": 'Basic realm="FM Drina Admin"'}
                )

    from .routes.dashboard import dashboard_bp
    from .routes.ponuda import ponuda_bp
    from .routes.dokumenta import dokumenti_bp
    from .routes.ugovor import ugovor_bp


    app.register_blueprint(dashboard_bp, url_prefix="/filip")
    app.register_blueprint(ponuda_bp, url_prefix="/filip/ponuda")
    app.register_blueprint(dokumenti_bp, url_prefix="/filip/dokumenti")
    app.register_blueprint(ugovor_bp, url_prefix="/filip/ugovor")

    # ✅ Dodaj rutu ovde – UNUTAR funkcije
    @app.route('/ponude/<path:filename>')
    def preuzmi_ponudu(filename):
        folder = Path(__file__).resolve().parent.parent / "generated_documents"
        return send_from_directory(folder, filename, as_attachment=True)

    return app
