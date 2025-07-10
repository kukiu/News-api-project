from django.shortcuts import render
from rest_framework import viewsets
# from .models import Article
# from .serializers import ArticleSerializer
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from django.conf import settings
import requests
import json

# Create your views here.

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

def fetch_news(request):
    # Get API key from settings
    api_key = settings.NEWS_API_KEY
    
    # Get parameters from request
    category = request.GET.get('category', '')
    search_query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    page_size = 21  # Show more articles per page
    
    # Using requests directly instead of newsapi-python for more flexibility
    params = {
        'apiKey': api_key,
        'pageSize': page_size,
        'page': page,
    }
    
    # Determine which endpoint to use based on parameters
    if search_query:
        url = "https://newsapi.org/v2/everything"
        params['q'] = search_query
        params['sortBy'] = 'relevancy'
    else:
        url = "https://newsapi.org/v2/top-headlines"
        params['country'] = 'us'  # Default to US news
        
        if category and category != 'all':
            params['category'] = category
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        # Check if the API request was successful
        if response.status_code == 200 and data.get('status') == 'ok':
            articles = data.get('articles', [])
            total_results = data.get('totalResults', 0)
            
            # Calculate pagination info
            total_pages = (total_results + page_size - 1) // page_size
            has_next = page < total_pages
            has_prev = page > 1
            
            # Available categories for the filter
            categories = [
                'all', 'business', 'entertainment', 'general', 
                'health', 'science', 'sports', 'technology'
            ]
            
            context = {
                'articles': articles,
                'current_category': category or 'all',
                'categories': categories,
                'search_query': search_query,
                'page': page,
                'has_next': has_next,
                'has_prev': has_prev,
                'next_page': page + 1,
                'prev_page': page - 1,
                'total_results': total_results,
                'showing_from': (page - 1) * page_size + 1,
                'showing_to': min(page * page_size, total_results),
            }
            
            return render(request, 'news/news_list.html', context)
        else:
            # If API request fails, show an error message
            error_message = data.get('message', 'Failed to fetch news. Please try again later.')
            return render(request, 'news/error.html', {'error_message': error_message})
    
    except Exception as e:
        # Handle any exceptions that might occur
        return render(request, 'news/error.html', {'error_message': str(e)})

def home(request):
    # Available categories for the filter
    categories = [
        'all', 'business', 'entertainment', 'general', 
        'health', 'science', 'sports', 'technology'
    ]
    return render(request, 'news/home.html', {'categories': categories})
