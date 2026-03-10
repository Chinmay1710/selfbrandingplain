# Chinmay Chaudhari – Portfolio Website

A modern personal portfolio and self-branding website built with **Django** for a Computer Engineering student at MPSTME, NMIMS University.

---

## 🚀 Quick Start

### 1. Create and activate a virtual environment
```bash
cd "/Users/chinmay/Documents/self Branding Plan"
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Load initial data (profile, skills, projects, etc.)
```bash
python manage.py loaddata portfolio_app/fixtures/initial_data.json
```

### 5. Create an admin superuser
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** to see your portfolio live! 🎉  
Admin panel: **http://127.0.0.1:8000/admin/**

---

## 📁 Project Structure

```
self Branding Plan/
├── manage.py
├── requirements.txt
├── Procfile
├── .env.example
├── portfolio_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio_app/
│   ├── models.py         ← 7 database models
│   ├── views.py          ← 7 page views
│   ├── urls.py           ← URL routing
│   ├── admin.py          ← Admin panel config
│   ├── forms.py          ← Contact form
│   └── fixtures/
│       └── initial_data.json
├── templates/
│   ├── base.html         ← Navbar, footer, Bootstrap 5
│   └── portfolio_app/
│       ├── home.html
│       ├── about.html
│       ├── skills.html
│       ├── projects.html
│       ├── experience.html
│       ├── certifications.html
│       └── contact.html
└── static/
    ├── css/main.css      ← Full design system
    └── js/main.js        ← Animations & interactivity
```

---

## 🌐 Pages

| Page | URL | Description |
|---|---|---|
| Home | `/` | Hero, stats, featured projects |
| About | `/about/` | Bio, profile card, education timeline |
| Skills | `/skills/` | Animated progress bars by category |
| Projects | `/projects/` | Project cards with tech tags |
| Experience | `/experience/` | Internship timeline |
| Certifications | `/certifications/` | Certification cards |
| Contact | `/contact/` | Contact form (saves to DB) |
| Admin | `/admin/` | Manage all content |

---

## 🗄️ Database Models

| Model | Purpose |
|---|---|
| `Profile` | Personal info, bio, social links, resume |
| `Education` | Education timeline entries |
| `Skill` | Skills with category and proficiency % |
| `Project` | Portfolio projects with GitHub links |
| `Internship` | Work experience entries |
| `Certification` | Certificates with credential links |
| `ContactMessage` | Messages from contact form |

---

## 🎨 Design System

- **Primary**: `#2563EB` (Blue)
- **Secondary**: `#0F172A` (Dark Navy)
- **Accent**: `#38BDF8` (Sky Blue)
- Dark theme with glassmorphism navbar
- AOS (Animate On Scroll) animations
- Typed.js animated hero subtitle
- Floating code card on home page
- Animated skill progress bars

---

## ☁️ Deployment

### PythonAnywhere
1. Upload project files
2. Create a virtual environment and install `requirements.txt`
3. Set `DEBUG=False` and add your domain to `ALLOWED_HOSTS` in `settings.py`
4. Run `python manage.py collectstatic`
5. Configure WSGI file to point to `portfolio_project.wsgi`

### Render / Railway
1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
3. Set start command: `gunicorn portfolio_project.wsgi`
4. Add env var: `SECRET_KEY=your-secret-key`, `DEBUG=False`

---

## 🔑 Admin Panel Usage

After `createsuperuser`, go to `/admin/` and:
- **Add projects** with descriptions, tech stack, GitHub links, images
- **Update skills** with proficiency percentages
- **Add certifications** with credential URLs
- **Read contact messages** and mark them as read
- **Update profile** info, bio, resume PDF upload
