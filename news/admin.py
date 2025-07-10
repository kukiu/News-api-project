from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_name', 'author', 'published_at')
    list_filter = ('source_name', 'published_at')
    search_fields = ('title', 'content', 'description')
