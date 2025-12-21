# Installation & Setup Guide

## System Requirements

- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **Internet**: Required for News API access

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ali-Ahmed026/News-Web-App.git
cd News-Web-App/NewsSphere
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get News API Key

1. Visit [newsapi.org](https://newsapi.org/register)
2. Create a free account
3. Copy your API key from the dashboard

### 5. Configure Environment Variables

Create `.env` file in the project root:

```bash
# .env file
DEBUG=True
SECRET_KEY=your-secret-key-here
NEWS_API_KEY=your-newsapi-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

### 6. Run Migrations

```bash
python manage.py migrate
```

This creates the database and necessary tables.

### 7. Create Admin Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create username, email, and password.

### 8. Start Development Server

```bash
python manage.py runserver
```

### 9. Access the Application

- **Main App**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **News Categories**: http://localhost:8000/news/category/technology

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution**: Ensure virtual environment is activated and dependencies installed:
```bash
pip install -r requirements.txt
```

### Issue: "News API returned 401 Unauthorized"

**Solution**: 
- Verify API key is correct in `.env`
- Check API key is active on newsapi.org
- Ensure you're not exceeding rate limits (100/day free tier)

### Issue: "Port 8000 already in use"

**Solution**: Use a different port:
```bash
python manage.py runserver 8001
```

### Issue: "Database locked" or "migrations failed"

**Solution**: Delete and recreate the database:
```bash
# Delete db.sqlite3 if it exists
rm db.sqlite3  # or del db.sqlite3 on Windows
python manage.py migrate
python manage.py createsuperuser
```

## Development Workflow

### Running Tests
```bash
python manage.py test
```

### Creating New Django App
```bash
python manage.py startapp appname
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

### Creating Database Backup
```bash
python manage.py dumpdata > backup.json
```

## Next Steps

- Read the [main README](../README.md) for features overview
- Check [Architecture Guide](ARCHITECTURE.md) for technical details
- Visit [API Documentation](API.md) for endpoint information
