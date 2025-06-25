
# 🏨 Hotel CRM V2 – Django Hotel Management System

Hotel CRM V2 is a Django-based platform designed to streamline hotel operations, including guest management, room booking, sales reporting, and admin control panels. This is an advanced version with cleaner UI, better structure, and integration capabilities.

---

## 🚀 Features

- 🛏️ Room & Guest Management
- 💸 Booking and Payment Handling
- 📦 Inventory System
- 📊 Sales & Revenue Reports
- 🔐 Secure Admin Login and Role Management
- 🔔 Notifications
- 📱 Telegram Bot Integration (Admin Alerts)
- 🌐 Mobile Friendly UI with Bootstrap 5

---

## 📸 Screenshots

> You can add images in `/docs` and link them here

```
📍 Dashboard
📍 Admin Panel
📍 Booking Overview
📍 Sales Report
```

---

## 🧪 Test Account

> Visit the test site and use demo credentials to explore the app

🔗 **Live demo:** https://market-admin-demo.onrender.com

| Role    | Username | Password  |
|---------|----------|-----------|
| Admin   | admin    | demo123   |
| Manager | manager  | demo123   |

---

## 🛠️ Tech Stack

- Django 5.2
- Bootstrap 5
- SQLite / PostgreSQL
- JavaScript / HTMX
- Gunicorn + Nginx (Production)

---

## 💻 Getting Started

```bash
git clone https://github.com/yourusername/hotel_crmV2.git
cd hotel_crmV2

python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env           # Set your environment variables

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://127.0.0.1:8000 in your browser.

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🐳 Docker Setup (Optional)

```bash
docker compose up --build
```

---

## 📁 Project Structure

```
hotel_crmV2/
├── apps/
│   ├── bookings/
│   ├── inventory/
│   └── users/
├── templates/
├── static/
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

**Made with ❤️ in Uzbekistan**
