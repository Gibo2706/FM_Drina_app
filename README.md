# 🛠️ FM Drina Admin Panel

Flask aplikacija za generisanje ponuda i ugovora u građevinskoj delatnosti.  
Cilj je da Filip samostalno, brzo i tačno kreira dokumente koje inače pravi ručno.

---

## 🚀 Funkcionalnosti

- ✅ Generisanje ponuda putem jednostavne web forme
- ✅ Bootstrap UI/UX – čist, responzivan interfejs
- ✅ Pregled prethodnih dokumenata (uskoro)
- ✅ Modularna struktura (ponude, ugovori, dashboard)
- 🔐 Sigurno čuvanje podataka (tajni u `.env`)

---

## 🧱 Tehnologije

- [Python 3.9+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📁 Struktura projekta

```
filip_app/
│
├── app/                # Glavna Flask aplikacija
│   ├── __init__.py
│   ├── routes/         # Modularne rute
│   └── templates/      # HTML prikazi
│
├── run.py              # Ulazna tačka (za `flask run`)
├── .env                # Lokalne tajne (nije u GIT-u)
├── requirements.txt    # Python zavisnosti
├── .gitignore          # Ignorisani fajlovi i folderi
└── README.md           # Ovaj fajl 🙂
```

---

## ⚙️ Pokretanje lokalno

```bash
# Kreiraj i aktiviraj virtualno okruženje
python -m venv venv
.env\Scripts\Activate   # Windows

# Instaliraj zavisnosti
pip install -r requirements.txt

# Pokreni aplikaciju
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
python -m flask run
```

Aplikacija će biti dostupna na:
```
http://localhost:5000/filip
```

---

## 📌 TODO / razvoj

- [ ] Generisanje `.docx` ponuda
- [ ] Ugovori sa različitim ulogama (izvođač, naručilac, podizvođač)
- [ ] Prikaz i filtracija prethodnih dokumenata
- [ ] Export PDF
- [ ] Login (opciono)

---

## 🧠 Napomena za developera (tebe)

> Kada god dodaješ nove fajlove/foldere:
- Ažuriraj `.gitignore` ako treba da ih ignorišeš (npr. `generated_documents/`)
- Ažuriraj ovaj `README.md` – strukturu, zavisnosti, pokretanje itd.

---

## 📃 Licenca

MIT – koristi slobodno, ali na sopstvenu odgovornost 😄