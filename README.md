# NewsSphere 📰

A modern, responsive news aggregation web application that brings you the latest headlines from around the world. Built with Django and powered by the News API.

## ✨ Features

- **🌍 Live News Feed** - Browse real-time headlines from global sources
- **🏷️ Category Browsing** - Filter news by Technology, Business, Sports, Entertainment, Health, and Science
- **🔍 Search Functionality** - Search for articles by keywords
- **👤 User Authentication** - Secure registration and login system
- **📱 Fully Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **⚡ Fast & Lightweight** - No heavy frameworks, pure HTML/CSS/JavaScript
- **🔗 Source Links** - Read full articles on original sources

## 🚀 Quick Start

### Try It Online
Visit the live application at: **[https://newssphere-fg8a.onrender.com/](https://newssphere-fg8a.onrender.com/)**

### Local Development Setup

**Requirements:**
- Python 3.8+
- pip
- Git

**Installation:**

```bash
# Clone the repository
git clone https://github.com/Ali-Ahmed026/News-Web-App.git
cd News-Web-App/NewsSphere

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get a News API key from newsapi.org and create .env file
# Add: NEWS_API_KEY=your_key_here

# Run migrations
python manage.py migrate

# Create a superuser account (for admin panel)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## 📖 How to Use

### As a Regular User
1. **Browse** - Explore top headlines on the home page
2. **Filter** - Click on categories to view news by topic
3. **Search** - Use the search bar to find articles
4. **Read** - Click any article to view full details and source link
5. **Account** - Create an account to personalize your experience

### As an Administrator
1. Visit `/admin` after logging in with superuser credentials
2. Manage users, news categories, and site settings
3. Monitor application usage and performance

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django 4.2, Django REST Framework |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Database** | SQLite (dev), PostgreSQL (production) |
| **API** | News API (newsapi.org) |
| **Hosting** | Render |

## 📂 Project Structure

```
NewsSphere/
├── manage.py
├── requirements.txt
├── newssphere/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── news/                    # News app
│   ├── views.py
│   ├── urls.py
│   ├── services.py          # News API integration
│   └── models.py
├── accounts/                # Authentication app
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── models.py
├── templates/               # HTML templates
│   ├── base.html
│   ├── news/
│   │   ├── home.html
│   │   ├── category.html
│   │   └── detail.html
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       └── profile.html
└── static/                  # CSS and JavaScript
    ├── css/style.css
    └── js/main.js
```

## 🔑 API Key Setup

1. Go to [newsapi.org](https://newsapi.org)
2. Sign up for a free account
3. Copy your API key
4. Create a `.env` file in the project root:
   ```
   NEWS_API_KEY=your_api_key_here
   ```

## 🐛 Troubleshooting

### "News API not working"
- Verify your News API key is valid
- Check that your API plan includes the endpoints being used
- Review rate limits (free tier: 100 requests/day)

### "Database errors"
- Run `python manage.py migrate` to create/update tables
- Ensure database file has proper permissions

### "Static files not loading"
- Run `python manage.py collectstatic`
- Check that `DEBUG=True` in development

### "Login issues"
- Ensure you've created a superuser: `python manage.py createsuperuser`
- Check browser cookies are enabled

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact & Support

- **Issues**: Use the [GitHub Issues](https://github.com/Ali-Ahmed026/News-Web-App/issues) page
- **Email**: [Your contact email]
- **Website**: [Your website if applicable]

## 🙏 Acknowledgments

- [News API](https://newsapi.org) for providing real-time news data
- [Django](https://www.djangoproject.com) for the excellent web framework
- The open-source community for inspiration and tools

---

**Happy news reading! 📰✨**
