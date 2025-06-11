# 🛠️ FM Drina Admin Panel

Flask aplikacija za generisanje ponuda i ugovora u građevinskoj delatnosti.  
Cilj je da Filip samostalno, brzo i tačno kreira dokumente koje inače pravi ručno.

---

## 🚀 Funkcionalnosti

- ✅ Generisanje ponuda putem jednostavne web forme
- ✅ Bootstrap UI/UX – čist, responzivan interfejs
- ✅ Direktno preuzimanje generisanog .docx fajla
- ✅ Modularna struktura (ponude, ugovori, dashboard)
- 🔐 Sigurno čuvanje podataka (tajni u `.env`)

---

## 🧱 Tehnologije

- [Python 3.9+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [docxtpl](https://pypi.org/project/docxtpl/)

---

## 📁 Struktura projekta

```
filip_app/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── dashboard.py
│   │   └── ponuda.py
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── ponuda_form.html
│   │   └── docx_templates/
│   │       └── ponuda_template.docx
│   └── utils/
│       └── doc_generator.py
│
├── generated_documents/         # Izlazni .docx fajlovi (NE ide u git)
├── run.py
├── .env                         # Tajne promenljive
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Pokretanje lokalno

```bash
python -m venv venv
.env\Scriptsctivate          # Windows

pip install -r requirements.txt

$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
python -m flask run
```

Aplikacija se pokreće na:
```
http://localhost:5000/filip
```

---

## ✅ Novo: Preuzimanje generisanog fajla

- Kada se generiše ponuda, korisniku se prikazuje link:
  ```
  ✅ Ponuda generisana: Preuzmi fajl
  ```
- Klikom se direktno preuzima `.docx` fajl iz foldera `generated_documents`

---

## 📌 TODO / razvoj

- [x] Generisanje `.docx` ponuda
- [x] Direktno preuzimanje fajla
- [ ] Prikaz svih dokumenata u interfejsu (moji dokumenti)
- [ ] Automatski broj ponude (`13/25`, `14/25`...)
- [ ] Ugovori sa fleksibilnim ulogama
- [ ] Export PDF
- [ ] Login (opciono)

---

## 🧠 Napomena za developera

> Kada god dodaš nove fajlove/foldere:
- Ažuriraj `.gitignore` ako treba
- Ažuriraj ovaj `README.md` sa funkcijama i strukturalnim promenama

---

## 📃 Licenca

MIT – koristi slobodno, ali na sopstvenu odgovornost 😄