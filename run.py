# run.py
import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG", "False").lower() == "true")
