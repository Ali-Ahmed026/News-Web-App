# FAQ - Frequently Asked Questions

## General Questions

### Q: Is NewsSphere free to use?
**A:** Yes! NewsSphere is completely free and open-source. The only cost is the free tier of the News API (100 requests/day).

### Q: Can I use this for commercial purposes?
**A:** Yes, under the MIT License. You're free to use, modify, and distribute it. Just include the original license file.

### Q: How often is the news data updated?
**A:** News is fetched in real-time from the News API, which updates continuously throughout the day.

### Q: What countries' news does it cover?
**A:** Over 50+ countries are supported through the News API, including all major countries worldwide.

### Q: Can I use this without the internet?
**A:** No, you need internet access because the app fetches live news from the News API.

---

## Technical Questions

### Q: What Python version is required?
**A:** Python 3.8 or higher. Python 3.10+ is recommended.

### Q: Can I use this with PostgreSQL?
**A:** Yes! By default it uses SQLite for development, but supports PostgreSQL for production. See [Installation Guide](INSTALLATION.md).

### Q: How do I add custom news sources?
**A:** Modify `services.py` to add additional API integrations. You can combine multiple news APIs.

### Q: Can I add user-saved articles feature?
**A:** Yes! You would need to:
1. Create a SavedArticle model in `models.py`
2. Add views for saving/retrieving articles
3. Create templates for saved articles page

### Q: How do I add comments/ratings to articles?
**A:** Create a Comment model:
```python
class Comment(models.Model):
    article_id = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## Deployment Questions

### Q: Is it free to deploy on Render?
**A:** Yes, Render has a free tier. However, the free tier has limitations like spinning down after inactivity.

### Q: Can I deploy on Heroku?
**A:** Heroku's free tier is no longer available. Consider Render, Railway, or PythonAnywhere instead.

### Q: How do I use a custom domain?
**A:** See the Deployment Guide for custom domain setup instructions.

### Q: How do I backup my database?
**A:** Run: `python manage.py dumpdata > backup.json`

### Q: Can I add email notifications?
**A:** Yes! Install django-celery and configure email backend in settings.

---

## News API Questions

### Q: Where do I get a News API key?
**A:** Visit [newsapi.org](https://newsapi.org), sign up, and get your free API key.

### Q: What are the free tier limitations?
**A:** 
- 100 requests per day
- 1 month search history
- No commercial use allowed without paid plan

### Q: Can I upgrade to a paid plan?
**A:** Yes! Visit your newsapi.org account and choose a premium plan for higher limits.

### Q: Why am I getting "401 Unauthorized" error?
**A:** Your API key is invalid, expired, or not set. Check your `.env` file.

### Q: Can I use News API from multiple sources?
**A:** Yes, but each source needs its own API key.

---

## User Account Questions

### Q: How do I reset a forgotten password?
**A:** Currently, there's no built-in password reset. Admin can reset it via admin panel or you need to implement email-based reset.

### Q: Can multiple users share one account?
**A:** Not recommended. Each user should have their own account.

### Q: How do I delete my account?
**A:** Contact the administrator or delete it from the admin panel.

### Q: Is my data private?
**A:** Yes, user data is stored securely. Passwords are hashed and never stored in plain text.

---

## Performance Questions

### Q: Why is the app slow on first load?
**A:** If on Render free tier, the service might have spun down. First request takes ~30 seconds to wake up.

### Q: How can I speed up the app?
**A:** 
- Upgrade to paid hosting tier
- Add caching (Redis)
- Optimize database queries
- Enable CDN for static files

### Q: How many concurrent users can it handle?
**A:** Depends on hosting. Free tier can handle ~10-20 concurrent users comfortably.

### Q: Can I cache news articles?
**A:** Yes! Implement caching:
```python
from django.core.cache import cache

def get_headlines():
    cache_key = 'top_headlines'
    headlines = cache.get(cache_key)
    if not headlines:
        headlines = fetch_from_api()
        cache.set(cache_key, headlines, 3600)  # Cache for 1 hour
    return headlines
```

---

## Troubleshooting Questions

### Q: "ModuleNotFoundError" - What should I do?
**A:** Activate your virtual environment and install dependencies:
```bash
pip install -r requirements.txt
```

### Q: "News API returned 0 articles" - How to fix?
**A:** 
- Check API key is valid
- Verify country code is correct (use 2-letter ISO code)
- Check you haven't exceeded rate limit

### Q: Static files aren't loading in production
**A:** Run: `python manage.py collectstatic --no-input`

### Q: Database migration fails
**A:** Try:
```bash
python manage.py migrate --fake-initial
```

### Q: Can't login after deployment
**A:** Create a new superuser in production:
```bash
python manage.py createsuperuser
```

---

## Contributing Questions

### Q: Can I contribute to NewsSphere?
**A:** Absolutely! Check our Contributing guidelines on GitHub.

### Q: How do I report a bug?
**A:** Open an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment (Python version, OS, browser)

### Q: Can I suggest new features?
**A:** Yes! Open a GitHub issue with your feature request.

---

## Still Have Questions?

- Check the [Installation Guide](INSTALLATION.md)
- Review the [Architecture Documentation](ARCHITECTURE.md)
- Read the [API Documentation](API.md)
- Visit [GitHub Issues](https://github.com/Ali-Ahmed026/News-Web-App/issues)
- Contact the developer
