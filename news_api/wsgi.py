"""
WSGI config for news_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import pathlib
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
env_path = pathlib.Path(__file__).parent.parent / '.env'
if env_path.exists():
    load_dotenv(str(env_path))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_api.settings')

application = get_wsgi_application()
