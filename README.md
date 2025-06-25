
# 🛒 Supermarket POS – Django-based Point of Sale System

A modern, responsive Point of Sale (POS) system built with Django 5.2 and Bootstrap 5, designed specifically for supermarkets and grocery stores. The system supports inventory tracking, transaction processing, sales reports, and user access control.

---

## 🚀 Features

- 📦 Product Management with Barcode Support
- 🧾 Real-time Sales & Transaction History
- 🧍 Role-based Access: Owner / Cashier
- 🗃️ Stock Level and Restock Threshold Management
- 🧠 Autocomplete for Fast Checkout (HTMX-ready)
- 📊 Admin Dashboard with Sales Overview
- 🔐 Secure Login System
- 📤 Exportable Sales Reports
- 🔔 Notifications and Low-stock Alerts
- 📱 Mobile-Responsive Design

---

## 📸 Screenshots

> You can upload images to `/docs` and reference here

```
📍 Owner Dashboard
📍 Product Listing
📍 Restock Inventory
📍 Sales Summary
```

---

## 🧪 Test Account

> Explore the system using the live demo below:

🔗 **Live demo:** https://market-admin-demo.onrender.com

| Role    | Username | Password  |
|---------|----------|-----------|
| Owner   | owner    | demo123   |
| Cashier | cashier  | demo123   |

---

## 🛠️ Built With

- Django 5.2
- Bootstrap 5
- SQLite / PostgreSQL
- JavaScript (HTMX Optional)
- Gunicorn + Nginx (Production-ready)

---

## 💻 Getting Started

```bash
git clone https://github.com/yourusername/supermarket-pos.git
cd supermarket-pos

python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env           # Set your environment variables

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000`.

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🐳 Docker Support

```bash
docker compose up --build
```

Runs Django + PostgreSQL in containers.

---

## 📁 Project Structure

```
supermarket-pos/
├── market/
│   ├── templates/market/
│   ├── static/market/
│   └── models.py, views.py, etc.
├── docs/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✉️ Contact

> Maintainer: [@yourhandle](https://t.me/yourhandle)  
> Email: your@email.com

---

## 📄 License

MIT License © 2025 Your Name

---

**Made with ❤️ in Uzbekistan – “Har bir savdo nazorat ostida”**
