from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    source_name = models.CharField(max_length=200, default="Unknown Source")
    author = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    url_to_image = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
