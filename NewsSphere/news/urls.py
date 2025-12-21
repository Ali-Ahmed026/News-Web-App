from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>/', views.category_news, name='category_news'),
    path('article/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search'),
]
