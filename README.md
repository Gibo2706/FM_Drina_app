# 🛠️ FM Drina Admin Panel

Flask aplikacija za generisanje ponuda i ugovora u građevinskoj delatnosti.  
Cilj je da Filip samostalno, brzo i tačno kreira dokumente koje inače pravi ručno.

---

## 🚀 Funkcionalnosti

- ✅ Generisanje ponuda putem forme
- ✅ Automatski (ili ručni) unos broja ponude
- ✅ Generisanje .docx fajlova
- ✅ Čuvanje metapodataka u .json formatu
- ✅ Tabela sa pregledom svih dokumenata (klijent, broj, datum)
- ✅ Direktno preuzimanje .docx fajla
- 🖨️ PDF dugme (placeholder za kasnije)

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
│       ├── doc_generator.py
│       └── doc_counter.py
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

Aplikacija se pokreće na: [http://localhost:5000/filip](http://localhost:5000/filip)

---

## 🧾 Moji dokumenti

Tabela prikazuje:

- Broj ponude
- Klijenta
- Datum
- Dugme za DOCX
- PDF status (uskoro)

---

## 📌 TODO

- [x] Automatski broj ponude
- [x] Pregled svih dokumenata sa metapodacima
- [ ] PDF export
- [ ] Filter i pretraga u tabeli
- [ ] Ugovori
- [ ] Autentifikacija

---

## 🧠 Napomena

Ažuriraj `.gitignore` i `README.md` svaki put kad:
- Dodaješ funkcionalnost
- Meniš strukturu foldera
- Ubacuješ nove pakete u `requirements.txt`

---

## 📃 Licenca

MIT – koristi slobodno, uz poštovanje zdravog razuma 😄