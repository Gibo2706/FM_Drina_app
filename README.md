# 🛠️ FM Drina Admin Panel

Flask aplikacija za generisanje ponuda i ugovora u građevinskoj delatnosti.  
Cilj je da Filip ili neko umesto njega brzo i precizno kreira dokumenta koja se često ponavljaju.

---

## 🚀 Funkcionalnosti

- ✅ Generisanje ponuda putem forme
- ✅ Automatski predlog broja ponude
- ✅ Generisanje ugovora putem forme
- ✅ Predlozi za svaki član ugovora (editable)
- ✅ Čuvanje .docx fajlova i .json metapodataka
- ✅ Promena podrazumevanog teksta svakog člana (klik na 💾)
- ✅ Prikaz svih dokumenata (ponude i ugovori)
- ✅ Pretraga u realnom vremenu (klijent, broj, datum)
- ✅ Export u PDF
- ✅ Filtriranje po tipu dokumenta

---

## 🧱 Tehnologije

- Python 3.9+
- Flask
- Bootstrap 5
- docxtpl
- python-dotenv

---

## 📁 Struktura projekta

```
filip_app/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── dashboard.py
│   │   ├── ponuda.py
│   │   ├── ugovor.py
│   │   └── dokumenta.py
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── ponuda_form.html
│   │   ├── ugovor_form.html
│   │   ├── dokumenti.html
│   │   └── docx_templates/
│   │       ├── ponuda_template.docx
│   │       └── ugovor_template_full.docx
│   ├── utils/
│   │   ├── doc_generator.py
│   │   └── doc_counter.py
│   └── defaults/
│       └── clanovi.json
├── generated_documents/
├── run.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Pokretanje lokalno

```bash
python -m venv venv
.env\Scriptsctivate
pip install -r requirements.txt

$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
python -m flask run
```

Aplikacija se pokreće na: [http://localhost:5000/filip](http://localhost:5000/filip)

---

## 🧠 Napomena

Obavezno ažurirati:
- `README.md` kada se doda nova funkcionalnost
- `requirements.txt` kada se doda novi paket
- `.gitignore` da ne šalješ `.env`, `__pycache__`, i `generated_documents/`

---

## 📃 Licenca

MIT – koristi slobodno uz zdrav razum 😄