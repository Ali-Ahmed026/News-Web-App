from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import news_service

CATEGORIES = [
    ('technology', 'Technology'),
    ('business', 'Business'),
    ('sports', 'Sports'),
    ('entertainment', 'Entertainment'),
    ('health', 'Health'),
    ('science', 'Science'),
]

def home(request):
    """Home page with top headlines."""
    data = news_service.get_top_headlines()
    articles = data.get('articles', [])
    
    # Debug: Log if there's an error
    if data.get('status') == 'error':
        print(f"News API Error: {data.get('message', 'Unknown error')}")
    
    return render(request, 'news/home.html', {
        'articles': articles,
        'categories': CATEGORIES,
        'current_category': None,
    })

@login_required
def category_news(request, category):
    """News filtered by category."""
    data = news_service.get_category_news(category)
    category_name = dict(CATEGORIES).get(category, category.title())
    return render(request, 'news/category.html', {
        'articles': data.get('articles', []),
        'categories': CATEGORIES,
        'current_category': category,
        'category_name': category_name,
    })

@login_required
def article_detail(request):
    """Display article details from URL parameters."""
    article = {
        'title': request.GET.get('title', ''),
        'description': request.GET.get('description', ''),
        'content': request.GET.get('content', ''),
        'url': request.GET.get('url', ''),
        'urlToImage': request.GET.get('image', ''),
        'source': {'name': request.GET.get('source', '')},
        'publishedAt': request.GET.get('published', ''),
        'author': request.GET.get('author', ''),
    }
    return render(request, 'news/article_detail.html', {
        'article': article,
        'categories': CATEGORIES,
    })

@login_required
def search(request):
    """Search news articles."""
    query = request.GET.get('q', '')
    articles = []
    if query:
        data = news_service.search_news(query)
        articles = data.get('articles', [])
    return render(request, 'news/search.html', {
        'articles': articles,
        'query': query,
        'categories': CATEGORIES,
    })
