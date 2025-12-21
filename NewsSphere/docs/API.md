# API Documentation

## REST API Endpoints

NewsSphere provides a REST API for accessing news data programmatically.

### Base URL
```
http://localhost:8000/api
https://your-domain.com/api (production)
```

## Endpoints

### Get Top Headlines

**Endpoint**: `GET /api/news/top-headlines/`

**Description**: Retrieve the latest news headlines

**Query Parameters**:
| Parameter | Type | Description |
|-----------|------|-------------|
| `country` | string | ISO country code (e.g., 'us', 'gb') |
| `category` | string | News category (tech, business, sports, etc.) |
| `limit` | integer | Number of articles (default: 20, max: 100) |

**Example Request**:
```bash
curl "http://localhost:8000/api/news/top-headlines/?country=us&category=technology&limit=10"
```

**Example Response**:
```json
{
  "status": "success",
  "count": 10,
  "results": [
    {
      "id": 1,
      "title": "Latest Tech Innovation",
      "description": "A groundbreaking new technology...",
      "source": "TechCrunch",
      "url": "https://example.com/article",
      "image_url": "https://example.com/image.jpg",
      "published_at": "2024-12-21T10:00:00Z",
      "content": "Full article content..."
    }
  ]
}
```

**Status Codes**:
- `200 OK` - Request successful
- `400 Bad Request` - Invalid parameters
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error

### Search News

**Endpoint**: `GET /api/news/search/`

**Description**: Search for news articles by keyword

**Query Parameters**:
| Parameter | Type | Description |
|-----------|------|-------------|
| `q` | string | Search query (required) |
| `category` | string | Filter by category |
| `sort_by` | string | relevancy, popularity, publishedAt |
| `from_date` | date | Start date (YYYY-MM-DD) |
| `to_date` | date | End date (YYYY-MM-DD) |
| `limit` | integer | Number of results |

**Example Request**:
```bash
curl "http://localhost:8000/api/news/search/?q=artificial+intelligence&category=technology"
```

**Example Response**:
```json
{
  "status": "success",
  "count": 25,
  "total_results": 523,
  "results": [
    {
      "id": 1,
      "title": "AI Breakthrough 2024",
      "description": "New developments in artificial intelligence...",
      "source": "MIT Technology Review",
      "url": "https://example.com/article",
      "image_url": "https://example.com/image.jpg",
      "published_at": "2024-12-20T15:30:00Z",
      "relevance_score": 0.95
    }
  ]
}
```

### Get Article by ID

**Endpoint**: `GET /api/news/articles/{id}/`

**Description**: Retrieve a specific article

**Path Parameters**:
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | Article ID (required) |

**Example Request**:
```bash
curl "http://localhost:8000/api/news/articles/1/"
```

**Example Response**:
```json
{
  "id": 1,
  "title": "Article Title",
  "description": "Short description",
  "content": "Full article content...",
  "source": "News Source",
  "url": "https://example.com/article",
  "image_url": "https://example.com/image.jpg",
  "published_at": "2024-12-21T10:00:00Z",
  "author": "John Doe",
  "category": "technology"
}
```

### Get Categories

**Endpoint**: `GET /api/news/categories/`

**Description**: List all available news categories

**Example Request**:
```bash
curl "http://localhost:8000/api/news/categories/"
```

**Example Response**:
```json
{
  "categories": [
    {
      "id": "technology",
      "name": "Technology",
      "description": "Tech news and innovations",
      "icon": "🔧"
    },
    {
      "id": "business",
      "name": "Business",
      "description": "Business and finance news",
      "icon": "💼"
    },
    {
      "id": "sports",
      "name": "Sports",
      "description": "Sports news and updates",
      "icon": "⚽"
    },
    {
      "id": "entertainment",
      "name": "Entertainment",
      "description": "Entertainment and celebrity news",
      "icon": "🎬"
    },
    {
      "id": "health",
      "name": "Health",
      "description": "Health and medical news",
      "icon": "⚕️"
    },
    {
      "id": "science",
      "name": "Science",
      "description": "Science and research news",
      "icon": "🔬"
    }
  ]
}
```

## Authentication

Currently, the API is public and does not require authentication. In future versions, consider adding:
- Token-based authentication
- Rate limiting per user
- API key management

## Rate Limiting

The API respects the News API rate limits:
- **Free Tier**: 100 requests per day
- **Paid Plans**: Higher limits available

Rate limit headers in response:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 75
X-RateLimit-Reset: 1703174400
```

## Error Handling

### Error Response Format

```json
{
  "status": "error",
  "error_code": "INVALID_QUERY",
  "message": "Search query cannot be empty",
  "details": {
    "field": "q",
    "reason": "required"
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_QUERY` | 400 | Invalid search query |
| `INVALID_CATEGORY` | 400 | Unknown category |
| `INVALID_DATE` | 400 | Invalid date format |
| `NOT_FOUND` | 404 | Article not found |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |
| `API_ERROR` | 503 | External API error |
| `SERVER_ERROR` | 500 | Internal server error |

## Example Implementations

### JavaScript

```javascript
async function getTopHeadlines() {
  try {
    const response = await fetch('/api/news/top-headlines/?limit=10');
    const data = await response.json();
    
    if (data.status === 'success') {
      data.results.forEach(article => {
        console.log(article.title);
      });
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

getTopHeadlines();
```

### Python

```python
import requests

def get_search_results(query):
    url = "http://localhost:8000/api/news/search/"
    params = {"q": query, "limit": 20}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['status'] == 'success':
        for article in data['results']:
            print(article['title'])

get_search_results("artificial intelligence")
```

### cURL

```bash
# Get top headlines
curl -X GET "http://localhost:8000/api/news/top-headlines/?limit=10" \
  -H "Accept: application/json"

# Search for articles
curl -X GET "http://localhost:8000/api/news/search/?q=python" \
  -H "Accept: application/json"
```

## Pagination

For large result sets, pagination may be available:

```
GET /api/news/search/?q=technology&page=1&page_size=20
```

Response includes:
```json
{
  "count": 500,
  "next": "/api/news/search/?page=2",
  "previous": null,
  "results": [...]
}
```

## CORS

CORS is disabled by default for security. To enable cross-origin requests in production, add:

```python
# settings.py
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware']
CORS_ALLOWED_ORIGINS = ['https://yourdomain.com']
```
