# 🚗 AutoHub – Django Vehicle Management System

AutoHub is a full-featured web-based automobile management system built using the Django framework.  
It allows users to explore automobile companies, view vehicle details, browse interior & exterior galleries, and calculate EMI instantly.

---

## 🌟 Features

- 🏢 Company Management (CRUD)
- 🚘 Product (Vehicle) Details Page
- 🖼 Interior & Exterior Image Gallery
- 💰 EMI Calculator
- 📊 Admin Panel Management
- 🎨 Clean & Responsive UI (Bootstrap 5)

---

## 🛠 Tech Stack

- Python 3.13
- Django 6.0
- SQLite3 (Default Database)
- Bootstrap 5
- HTML5 / CSS3

---

## 📁 Project Structure

```
AutoHub/
│
├── cbv/                  # Main Django Project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── cbvapp/               # Main Application
│   ├── migrations/
│   ├── templates/
│   │   └── cbvapp/
│   │       ├── company_list.html
│   │       ├── company_detail.html
│   │       ├── products_details.html
│   │       ├── add_company.html
│   │       ├── delete_confirm.html
│   │       └── emi_calculator.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
|   └── admin.py
│
├── templates/
|      └── index.html
|      └── base.html
|
├── media/                # Uploaded Images
├── static/               # Static Files (CSS/JS)
├── db.sqlite3
└── manage.py
```

---

## 🧱 Database Models

### Company
- name
- ceo
- est_year
- origin
- image

### Product
- company (ForeignKey)
- product_name
- price
- color
- fuel_type
- cc
- mileage
- pro_img

### Interior
- product (ForeignKey)
- image

### Exterior
- product (ForeignKey)
- image

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/autohub.git
cd autohub
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

Activate:

Windows:
```bash
env\Scripts\activate
```

Mac/Linux:
```bash
source env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

Open in browser:
```
http://127.0.0.1:8000/
```

Admin panel:
```
http://127.0.0.1:8000/admin/
```

---

## 💰 EMI Calculation Logic

EMI Formula Used:

```
EMI = (P × R × (1 + R)^N) / ((1 + R)^N - 1)
```

Where:
- P = Loan Amount
- R = Monthly Interest Rate
- N = Number of Months

---

## 🎯 How It Works

1. Admin adds companies and vehicles.
2. Interior & exterior images are uploaded via admin panel.
3. Users browse companies.
4. Click a product to view full details.
5. Use EMI calculator to estimate monthly payment.

---

## 📸 UI Highlights

- Clean card-based layout
- Responsive grid design
- Modern Bootstrap styling
- Organized gallery sections

---

## 🔐 Admin Panel Usage

All vehicle images (Interior & Exterior) are managed through:

```
/admin/
```

No frontend upload functionality is enabled.

---

## 📌 Future Improvements

- Search & filter vehicles
- Authentication system
- Wishlist feature
- Compare vehicles
- REST API integration
- Deployment to production (Render / AWS / Railway)

---

## 👨‍💻 Author

Developed by **Gowtham Reddy**

---

## 📄 License

This project is for educational purposes.
