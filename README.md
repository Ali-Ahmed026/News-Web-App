# NewsSphere

A web-based news aggregation application built with Django that fetches live news from the News API.

## Features

- **User Authentication**: Register, login, and logout using Django's built-in auth system
- **Top Headlines**: Browse the latest news on the home dashboard
- **Category Browsing**: Filter news by Technology, Business, Sports, Entertainment, Health, and Science
- **Article Details**: View full article information with links to original sources
- **Search**: Search for news articles by keyword
- **Responsive Design**: Mobile-friendly interface without external CSS frameworks
- **User Profile**: View account information and membership details

## Tech Stack

- **Backend**: Django 4.2, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (no frameworks)
- **Database**: MySQL (SQLite for development)
- **API**: [News API](https://newsapi.org/)

## Project Structure

```
NewsSphere/
├── manage.py
├── requirements.txt
├── .env.example
├── newssphere/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── news/                # News app
│   ├── views.py
│   ├── urls.py
│   └── services.py      # News API integration
├── accounts/            # Authentication app
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── templates/           # HTML templates
│   ├── base.html
│   ├── news/
│   └── accounts/
└── static/              # CSS and JavaScript
    ├── css/style.css
    └── js/main.js
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/NewsSphere.git
cd NewsSphere
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example file
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac

# Edit .env and add your settings:
# - SECRET_KEY: Generate a new Django secret key
# - NEWS_API_KEY: Get from https://newsapi.org/
# - Database credentials (if using MySQL)
```

### 5. Database Setup

**Option A: SQLite (Development)**
Edit `settings.py` and uncomment the SQLite configuration.

**Option B: MySQL (Production)**
```sql
CREATE DATABASE newssphere;
```
Update `.env` with your MySQL credentials.

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Getting a News API Key

1. Go to [https://newsapi.org/](https://newsapi.org/)
2. Click "Get API Key"
3. Create a free account
4. Copy your API key to the `.env` file

## Usage

1. **Home Page**: View top headlines (accessible to all)
2. **Register/Login**: Create an account to access all features
3. **Browse Categories**: Click category links in the navbar
4. **Search**: Use the search bar to find specific news
5. **Read Articles**: Click "Read More" for details, then "Read Full Article" for the source

## Screenshots

*Add screenshots of your application here*

## API Integration

The application uses the News API with the following endpoints:
- `GET /v2/top-headlines` - Fetch top headlines by country/category
- `GET /v2/everything` - Search all articles

## License

This project is for educational purposes.

## Author

Developed as part of the Web Application Development course.
