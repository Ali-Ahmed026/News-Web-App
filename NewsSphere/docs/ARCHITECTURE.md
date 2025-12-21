# Architecture & Technical Details

## Project Architecture

### MVC Pattern

NewsSphere follows Django's MTV (Model-Template-View) architecture:

```
Request
  ↓
URLs (news/urls.py) → Routes request to appropriate view
  ↓
Views (news/views.py) → Processes request logic
  ↓
Services (news/services.py) → Fetches data from News API
  ↓
Models (news/models.py) → Database queries if needed
  ↓
Templates (templates/) → Renders HTML response
  ↓
Response (HTML/JSON)
```

## Key Components

### 1. News App (`news/`)

**Purpose**: Handles all news-related functionality

**Key Files**:
- `models.py` - Database models (if any custom models)
- `views.py` - Request handlers
- `services.py` - News API integration
- `urls.py` - URL routing
- `templates/` - HTML templates

**Key Views**:
- `home()` - Display top headlines
- `category()` - Show news by category
- `search()` - Search functionality
- `article_detail()` - Show full article

### 2. Accounts App (`accounts/`)

**Purpose**: User authentication and profile management

**Key Files**:
- `models.py` - User model extensions
- `views.py` - Login, register, logout
- `forms.py` - User registration form
- `urls.py` - Auth URLs

**Key Views**:
- `register()` - User registration
- `login()` - User login
- `logout()` - User logout
- `profile()` - User profile page

### 3. Project Settings (`newssphere/`)

**Key Files**:
- `settings.py` - Django configuration
- `urls.py` - Main URL router
- `wsgi.py` - WSGI application
- `asgi.py` - ASGI application

## Data Flow

### Fetching News

```
User requests /news/
    ↓
views.home() called
    ↓
services.fetch_top_headlines() called
    ↓
requests.get() → News API endpoint
    ↓
Parse JSON response
    ↓
Pass to template
    ↓
Render HTML with news articles
```

### User Authentication

```
User submits login form
    ↓
views.login() handles POST request
    ↓
authenticate() checks credentials
    ↓
login() creates session
    ↓
Redirect to homepage
```

## Database Schema

### User Model (Django Built-in)

```
User
├── id (PK)
├── username
├── email
├── password (hashed)
├── first_name
├── last_name
├── is_active
├── date_joined
└── last_login
```

Custom models can be added as needed for:
- Saved articles
- User preferences
- Article ratings

## External API Integration

### News API Integration

**Base URL**: `https://newsapi.org/v2`

**Endpoints Used**:
- `/top-headlines` - Latest news
- `/everything` - Search news

**Authentication**: API Key in query parameters

**Rate Limits**: 100 requests/day (free tier)

**Response Structure**:
```json
{
  "status": "ok",
  "totalResults": 123,
  "articles": [
    {
      "source": {"id": null, "name": "BBC"},
      "author": "John Doe",
      "title": "Article Title",
      "description": "Article description",
      "url": "https://...",
      "urlToImage": "https://...",
      "publishedAt": "2024-12-21T10:00:00Z",
      "content": "Full article content..."
    }
  ]
}
```

## Frontend Architecture

### Templates

**Base Template** (`base.html`):
- Navigation bar
- Header/Footer
- CSS/JS includes
- Block definitions for child templates

**Child Templates**:
- `home.html` - Homepage
- `category.html` - Category view
- `search.html` - Search results
- `detail.html` - Article details

### Static Files

**CSS** (`static/css/style.css`):
- Responsive grid layout
- Mobile-first design
- No external CSS frameworks

**JavaScript** (`static/js/main.js`):
- Search form handling
- Dynamic filtering
- Navigation interactions

## Security Measures

- **CSRF Protection**: Django middleware enabled
- **SQL Injection**: ORM prevents SQL injection
- **XSS Protection**: Template escaping by default
- **Password Hashing**: Django's default argon2
- **HTTPS**: Enabled in production

## Performance Optimizations

- Static file caching with WhiteNoise
- Database query optimization
- API response caching (if implemented)
- Minified CSS/JavaScript
- Responsive images

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 4.2+ | Web framework |
| djangorestframework | 3.14+ | REST API support |
| requests | 2.31+ | HTTP requests to News API |
| python-dotenv | 1.0+ | Environment variables |
| gunicorn | 21.0+ | Production server |
| psycopg2-binary | 2.9+ | PostgreSQL driver |
| whitenoise | 5.0+ | Static file serving |

## Deployment Considerations

- Environment variables for secrets
- Static file collection
- Database migrations
- Error logging
- Rate limiting
- CORS headers if API is exposed
