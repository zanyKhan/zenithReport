# ZenithReport 📰

A modern blog website built using **Django**, where users can read and manage blogs across multiple categories.

---

## 🚀 Features

- 📝 Create, edit, and publish blog posts  
- 🗂️ Multiple blog categories  
  - Technology  
  - Business  
  - Sports  
  - Science  
  - Politics  
  - Health  
- 👥 Role-based access system  
  - Admin  
  - Manager  
  - Editor  
- 🔐 Authentication (Login & Register)  
- 📊 Dashboard for blog & user management  
- 📱 Responsive design  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  
- **Authentication:** Django built-in auth system  

---

## 📂 Project Structure

```
zenithReport/
│── blog_main/ # Main project settings
│── blogs/ # Blog app (posts, categories)
│── dashboard/ # Dashboard & user management
│── social_links/ # Social media links
│── templates/ # HTML templates
│── static/ # CSS, JS, images
│── manage.py # Django project entry point
│── requirements.txt # Dependencies
```


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

    - git clone https://github.com/zanyKhan/zenithReport.git
    - cd zenithReport

  
### 2️⃣ Create Virtual Environment
    - python -m venv env
    - env\Scripts\activate

    
### 3️⃣ Install Dependencies
    - pip install -r requirements.txt

    
### 4️⃣ Run Migrations
    - python manage.py makemigrations
    - python manage.py migrate

    
### 5️⃣ Create Superuser
    - python manage.py createsuperuser

    
### 6️⃣ Run Server
    - python manage.py runserver

    
---

## 🔐 User Roles

- **Admin (Superuser):** Full access  
- **Manager:** Manage users & blogs  
- **Editor:** Create & edit blogs 

---


## 👩‍💻 Author

**Zainab Hussain**  
GitHub: https://github.com/zanyKhan  

---

## 📄 License

This project is created for learning and personal use.
