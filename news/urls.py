from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import fetch_news, home

# router = DefaultRouter()
# router.register('articles', ArticleViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('', home, name='home'),
    path('news/', fetch_news, name='fetch_news'),
] 