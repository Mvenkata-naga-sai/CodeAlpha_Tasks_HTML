# 📱 Mini Social Media Platform (Django)

## 📌 Project Description

This project is a **basic social media web application** built using **Django (Python)**.
It allows users to create accounts, share posts, like posts, comment, and interact with other users.

---

## 🚀 Features

✔ User Registration & Login
✔ Create Posts
✔ Like Posts
✔ Comment on Posts
✔ Follow Users (basic model)
✔ Simple Feed System

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Django (Python)
* **Database:** SQLite

---

## 📁 Project Structure

```
social_media_project/
│── manage.py
│
├── social_media/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
│   ├── templates/
│   │   ├── home.html
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

### 1️⃣ Download or Clone Project

```bash
git clone <your-repo-link>
cd social_media_project
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

### 4️⃣ Run Server

```bash
python manage.py runserver
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🔐 How to Use

1. Register a new account
2. Login to your account
3. Create posts
4. Like posts
5. Comment on posts

---

## 🧠 How It Works

* Users are stored in Django authentication system
* Posts are linked to users
* Likes and comments are stored in separate tables
* Feed displays all posts

---

## ⚠️ Limitations

* No profile pictures
* No real-time updates
* No notifications
* Basic UI design

---

## 🚀 Future Improvements

* Profile images
* Followers list UI
* Notifications system
* Real-time chat
* Modern UI (React integration)

---

## 👨‍💻 Author

**Venkata Naga Sai**
Final Year - Computer Science Engineering

---

## 📌 Project Type

CodeAlpha Internship Task – Social Media Platform

---
