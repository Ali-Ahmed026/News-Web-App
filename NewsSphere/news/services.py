import requests
from django.conf import settings

class NewsAPIService:
    """Service class to interact with News API."""
    
    def __init__(self):
        self._api_key = None
        self._base_url = None
    
    @property
    def api_key(self):
        """Lazy load API key from settings."""
        if self._api_key is None:
            self._api_key = settings.NEWS_API_KEY
        return self._api_key
    
    @property
    def base_url(self):
        """Lazy load base URL from settings."""
        if self._base_url is None:
            self._base_url = settings.NEWS_API_BASE_URL
        return self._base_url
    
    def _make_request(self, endpoint, params=None):
        """Make a request to the News API."""
        if params is None:
            params = {}
        
        # Check if API key is set
        if not self.api_key:
            return {'status': 'error', 'message': 'News API key is not configured', 'articles': []}
        
        params['apiKey'] = self.api_key
        
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Check if API returned an error
            if data.get('status') == 'error':
                return {'status': 'error', 'message': data.get('message', 'Unknown API error'), 'articles': []}
            
            return data
        except requests.RequestException as e:
            return {'status': 'error', 'message': str(e), 'articles': []}
    
    def get_top_headlines(self, country='us', category=None, page_size=20):
        """Fetch top headlines."""
        params = {'country': country, 'pageSize': page_size}
        if category:
            params['category'] = category
        return self._make_request('top-headlines', params)
    
    def get_category_news(self, category, country='us', page_size=20):
        """Fetch news by category."""
        return self.get_top_headlines(country=country, category=category, page_size=page_size)
    
    def search_news(self, query, page_size=20):
        """Search for news articles."""
        params = {'q': query, 'pageSize': page_size, 'sortBy': 'publishedAt'}
        return self._make_request('everything', params)

news_service = NewsAPIService()
