
# 🌍 Webtravel — Django Travel Management App  

![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)  
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap&logoColor=white)  

---

## 📖 Overview  
**Webtravel** is a Django web application built for the **R5A05 – Programmation avancée** course.  

It is designed to demonstrate advanced Django features through an educational project:  
- Manage **cities** (`Villes`) and **trips** (`Voyages`)  
- Associate **steps (étapes)** between trips and cities  
- Use **Django forms** to add new entities  
- Render data with **templates & Bootstrap 5**  
- Store and serve **static files** (CSS, images)  

This project serves as a complete **mini travel agency system**, ideal for learning and experimenting with Django.

---

## 🚀 Features
✅ Homepage with navigation  
✅ List of voyages and villes  
✅ Detailed view of a voyage and its steps  
✅ Forms to add new cities and voyages  
✅ User-friendly interface styled with **Bootstrap 5**  
✅ Modular templates (`base.html`, `includes/menu.html`, `includes/footer.html`)  

---

## 📂 Project Structure
```

webtravel/
├── applitravel/             # Main application
│   ├── models.py            # Ville, Voyage, Composition models
│   ├── views.py             # Views for list, detail, forms
│   ├── forms.py             # ModelForms for Ville & Voyage
│   ├── templates/applitravel/
│   │   ├── base.html        # Global layout
│   │   ├── voyages.html     # List of voyages
│   │   ├── villes.html      # List of cities
│   │   ├── voyage.html      # Voyage detail
│   │   ├── formulaireCreationVille.html
│   │   ├── formulaireCreationVoyage.html
│   │   ├── traitementFormulaireCreationVille.html
│   │   └── traitementFormulaireCreationVoyage.html
│   └── static/applitravel/  # CSS, images
├── webtravel/               # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── manage.py
├── README.md
└── .gitignore

````

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/webtravel.git
cd webtravel
````

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the server

```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎮 Usage

* **Home**: `/` → Welcome page
* **Voyages list**: `/voyages/`
* **Voyage detail**: `/voyages/<id>/`
* **Villes list**: `/villes/`
* **Add a city**: `/villes/add`
* **Add a voyage**: `/voyages/add`

---

## 🛠️ Built With

* [Django](https://www.djangoproject.com/) — Web framework
* [Python](https://www.python.org/) — Programming language
* [Bootstrap 5](https://getbootstrap.com/) — Styling & layout

---

## 📸 Screenshots

*(Add your own screenshots here for better visuals!)*

Example:
![Voyages Page](docs/screenshots/voyages.png)
![Formulaire Ville](docs/screenshots/form-ville.png)

---

## 👨‍💻 Author

* **Youssef Abichou**
  BUT Informatique – IUT d’Orsay
  Passionate about web development & IT technologies

---

## 🔮 Future Improvements

* [ ] Authentication & user roles (admin vs. user)
* [ ] Advanced search & filtering of voyages
* [ ] Dynamic trip composition (add/remove cities interactively)
* [ ] REST API for voyages & villes (Django REST Framework)

---

## 📜 License

This project is for **educational purposes** only (IUT d’Orsay).
You are free to use it for learning Django.

