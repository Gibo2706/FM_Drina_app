# 🛠️ FM Drina Admin Panel

Flask aplikacija za generisanje ponuda i ugovora u građevinskoj delatnosti.  
Cilj je da Filip samostalno, brzo i tačno kreira dokumente koje inače pravi ručno.

---

## 🚀 Funkcionalnosti

- ✅ Generisanje ponuda putem web forme
- ✅ Preuzimanje ponuda u .docx formatu
- ✅ Prikaz svih generisanih dokumenata
- ✅ Bootstrap UI za jednostavno korišćenje
- 🔐 .env fajl za konfiguraciju

---

## 🧱 Tehnologije

- Python 3.9+
- Flask
- Bootstrap 5
- python-dotenv
- docxtpl

---

## 📁 Struktura projekta

```
filip_app/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── dashboard.py
│   │   ├── ponuda.py
│   │   └── dokumenta.py
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── ponuda_form.html
│   │   ├── dokumenti.html
│   │   └── docx_templates/
│   │       └── ponuda_template.docx
│   └── utils/
│       └── doc_generator.py
│
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

Aplikacija: [http://localhost:5000/filip](http://localhost:5000/filip)

---

## ✅ Dodato

- `/filip/dokumenti` – prikaz svih fajlova iz `generated_documents`
- Link za direktno preuzimanje svakog fajla
- Serviranje fajlova sa `/ponude/<filename>`

---

## 📌 TODO

- [x] Generisanje ponuda
- [x] Preuzimanje fajla
- [x] Prikaz svih dokumenata
- [ ] Automatski broj ponude
- [ ] Generisanje ugovora
- [ ] PDF export (kasnije)
- [ ] Autentifikacija (opciono)

---

## 🧠 Napomena

Ažuriraj:
- `.gitignore` ako dodaješ nešto što ne treba da ide u Git
- `README.md` svaki put kada menjaš strukturu, funkcije ili zavisnosti

---

## 📃 Licenca

MIT