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
    api_key = settings.NEWS_API_KEY  # You can keep the same variable name
    
    # Get parameters from request
    category = request.GET.get('category', '')
    search_query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    page_size = 10  # GNews free tier allows 10 articles per request
    
    # GNews API base URL
    base_url = "https://gnews.io/api/v4"
    
    # Determine which endpoint to use based on parameters
    if search_query:
        url = f"{base_url}/search"
        params = {
            'q': search_query,
            'token': api_key,
            'max': page_size,
            'page': page,
            'lang': 'en'
        }
    else:
        # For category browsing
        url = f"{base_url}/top-headlines"
        params = {
            'token': api_key,
            'max': page_size,
            'page': page,
            'lang': 'en'
        }
        
        # Map NewsAPI categories to GNews categories
        category_mapping = {
            'business': 'business',
            'entertainment': 'entertainment',
            'general': 'general',
            'health': 'health',
            'science': 'science',
            'sports': 'sports',
            'technology': 'technology'
        }
        
        if category and category != 'all' and category in category_mapping:
            params['topic'] = category_mapping[category]
    
    try:
        response = requests.get(url, params=params)
        
        # Check if the API request was successful
        if response.status_code == 200:
            data = response.json()
            
            # GNews returns articles in a different format
            articles = data.get('articles', [])
            total_results = len(articles)  # GNews doesn't provide total count
            
            # Transform GNews response to match our template's expected format
            transformed_articles = []
            for article in articles:
                transformed_article = {
                    'title': article.get('title'),
                    'description': article.get('description'),
                    'url': article.get('url'),
                    'urlToImage': article.get('image'),
                    'publishedAt': article.get('publishedAt'),
                    'source': {
                        'name': article.get('source', {}).get('name', 'Unknown')
                    },
                    'author': article.get('source', {}).get('name', 'Unknown'),
                    'content': article.get('content')
                }
                transformed_articles.append(transformed_article)
            
            # Calculate pagination info
            # Note: GNews free tier has limited pagination capabilities
            has_next = len(articles) == page_size
            has_prev = page > 1
            
            # Available categories for the filter
            categories = [
                'all', 'business', 'entertainment', 'general', 
                'health', 'science', 'sports', 'technology'
            ]
            
            context = {
                'articles': transformed_articles,
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
            error_message = f"Failed to fetch news. Status code: {response.status_code}"
            return render(request, 'news/error.html', {'error_message': error_message})
    
    except Exception as e:
        # Handle any exceptions that might occur
        error_message = str(e)
        return render(request, 'news/error.html', {'error_message': error_message})
