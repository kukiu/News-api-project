#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pathlib
from dotenv import load_dotenv

def main():
    """Run administrative tasks."""
    # Load environment variables from .env file if it exists
    env_path = pathlib.Path(__file__).parent / '.env'
    if env_path.exists():
        load_dotenv(str(env_path))
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
