import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "default_key")

    from .routes.dashboard import dashboard_bp
    from .routes.ponuda import ponuda_bp

    app.register_blueprint(dashboard_bp, url_prefix="/filip")
    app.register_blueprint(ponuda_bp, url_prefix="/filip/ponuda")

    return app
