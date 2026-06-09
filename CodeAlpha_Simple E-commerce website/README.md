# 🛒 E-Commerce Website 

## 📌 Project Description

This is a **basic E-commerce website** built using **Django (Python)** for backend and **HTML, CSS, JavaScript** for frontend.

The project allows users to:

* View products
* See product details
* Add items to cart
* Register & login
* Place basic orders

---

## 🚀 Features

✔ Product Listing
✔ Product Detail Page
✔ Shopping Cart
✔ User Registration & Login
✔ Order Processing (Basic)
✔ Admin Panel for Product Management

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Django (Python)
* **Database:** SQLite

---

## 📁 Project Structure

```
ecommerce_project/
│── manage.py
│
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
│   ├── templates/
│   │   ├── home.html
│   │   ├── product.html
│   │   ├── cart.html
│   │   ├── login.html
│   │   ├── register.html
│
│   ├── static/
│       ├── style.css
│
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download Project

```bash
git clone <your-repo-link>
cd ecommerce_project
```

---

### 2️⃣ Install Dependencies

```bash
pip install django
```

---

### 3️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

---

### 5️⃣ Run Development Server

```bash
python manage.py runserver

```

## 🧠 How It Works

* Products are stored in the database
* Users can register and login
* Logged-in users can add products to cart
* Orders are created when items are added

---

## ⚠️ Limitations (Basic Version)

* No payment gateway
* No advanced UI design
* No order history page
* Basic cart functionality

---

## 🚀 Future Improvements

* Payment integration (Razorpay/Stripe)
* Responsive UI design
* Product search & filters
* Order tracking system
* REST API integration

---

## 👨‍💻 Author

**Venkata Naga Sai**

Computer Science Engineering

---

## 📌 Project Type

CodeAlpha Internship Task – Basic E-commerce Website

---
