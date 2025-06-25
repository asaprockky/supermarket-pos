````markdown
# 🛒 Market Admin – Inventory & Sales Management (Django 5.2 + Bootstrap 5)

A lightweight back-office web app for small shops and supermarkets.  
Manage products, stock levels, and transactions from a single, mobile-friendly dashboard.

<div align="center">
  <img src="docs/screenshot-dashboard.png" alt="Dashboard screenshot" width="90%">
</div>

---

## ✨ Key Features

| Module               | What you can do                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **Products**         | Create, edit, delete items; bar-code field, cost/price, category                |
| **Inventory**        | See current stock, set per-product **Restock Level**, one-click **Restock**     |
| **Sales**            | Transaction list with total price & payment method                              |
| **Dashboard**        | Cards for today’s revenue, low-stock alerts, quick links                        |
| **Auth**             | Django sessions, owner / cashier roles (customisable)                           |
| **API**              | `/api/products/` autocomplete endpoint (HTMX-friendly JSON)                     |

---

## 🚀 Live Demo / Test Link

> ### <https://fulstek.uz>

*Logged-out users are redirected to the login page.*  

---

## 🏗️ Quick Start (local)

```bash
git clone (https://github.com/asaprockky/supermarket-pos.git)
cd market-admin

# 1. Create venv + install deps
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Environment variables (see .env.example)
cp .env.example .env                # then edit if needed

# 3. DB migrations + superuser
python manage.py migrate
python manage.py createsuperuser

# 4. Run
python manage.py runserver
````

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) – log in → **Admin Panel**.

---

## 🧪 Running Tests

```bash
pytest
```

Generates a coverage report:

```bash
pytest --cov
```

---

## 🗂️ Project Structure

```
market_admin/
├── market/                # Django app with models, views, templates
│   ├── templates/market/
│   ├── static/market/
│   └── urls.py
├── media/                 # Uploaded files (ignored in git)
├── docs/                  # Screenshots, diagrams
├── requirements.txt
├── docker-compose.yml     # Optional container setup
└── README.md
```

---

## 🔧 Configuration

| Variable        | Default      | Purpose                      |
| --------------- | ------------ | ---------------------------- |
| `SECRET_KEY`    | `dev-secret` | Django secret                |
| `DEBUG`         | `True`       | Debug mode                   |
| `ALLOWED_HOSTS` | `*`          | Hosts list for production    |
| `DATABASE_URL`  | SQLite       | Any `dj-database-url` string |

*(Set them in `.env`, `docker-compose.yml`, or your hosting dashboard.)*

---

## 📈 API Endpoints (JSON)

| URL                                 | Description                   |
| ----------------------------------- | ----------------------------- |
| `GET /api/products/?q=milk`         | Autocomplete (name / barcode) |
| `POST /product/<id>/restock/`       | Add `quantity` to stock       |
| `POST /product/<id>/restock-level/` | Update `restock_level`        |

All endpoints require an authenticated session; use token or SessionAuth as needed.

---

## 🐳 Docker (optional)

```bash
docker compose up --build
```

* Django runs on **`8000`**
* PostgreSQL service included
* Static files collected to `/static/`

---

## 🛡️ Security Notes

* `LogoutView` uses `GET` by default – safe for this internal app.
* For stricter CSRF posture, switch to a POST-only logout form.

---

## 🤝 Contributing

1. Fork ➡️ Branch (`git checkout -b feature/fancy`)
2. Code & tests
3. `black . && isort .`
4. PR 🚀

All feedback is welcome – open an issue or ping me on Telegram **@s17aj_04**.

---



---

> *Made with ❤️ in Uzbekistan – «Bir qadam oldinga, har kun!»*
