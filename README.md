# News API Django Project

A Django web application that fetches and displays the latest news from NewsAPI.org.

## Features

- Displays latest news headlines from various sources
- Search functionality for finding specific news
- Category filtering (business, entertainment, health, etc.)
- Pagination for browsing through multiple pages of results
- Clean, responsive UI using Bootstrap 4
- RESTful API endpoints for news articles

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd news_api_project
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on the `.env.example` template:
```bash
cp .env.example .env
```

5. Edit the `.env` file with your actual values:
```
DEBUG=True
DJANGO_SECRET_KEY=your_secret_key_here
NEWS_API_KEY=your_news_api_key_here
ALLOWED_HOSTS=127.0.0.1,localhost
```

6. Apply migrations:
```bash
python manage.py migrate
```

7. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

### Running the Application Locally

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to view the application.

## Deployment

### Preparing for Deployment

1. Set `DEBUG=False` in your production environment
2. Configure proper `ALLOWED_HOSTS` for your domain
3. Make sure your API keys and secret keys are securely stored as environment variables

### Deploying to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the following settings:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn news_api.wsgi`
4. Add the following environment variables:
   - `DEBUG`: False
   - `DJANGO_SECRET_KEY`: [Generate a secure key]
   - `NEWS_API_KEY`: [Your NewsAPI key]
   - `ALLOWED_HOSTS`: your-app.onrender.com,your-custom-domain.com

### Deploying to PythonAnywhere

1. Create a PythonAnywhere account
2. Upload your code using Git
3. Create a virtual environment and install dependencies
4. Set up a web app with the following configuration:
   - **Source code**: /path/to/your/repo
   - **Working directory**: /path/to/your/repo
   - **WSGI configuration file**: Use the PythonAnywhere WSGI file template for Django
5. Configure environment variables in the PythonAnywhere dashboard

## API Endpoints

- `/api/articles/` - List all articles in the database
- `/news/` - View latest news from NewsAPI.org

## Security Notes

- Never commit `.env` files or any files containing sensitive information
- Always use environment variables for API keys, secret keys, and other sensitive data
- Keep `DEBUG=False` in production to avoid exposing sensitive information
- Regularly update dependencies to address security vulnerabilities

## License

This project is licensed under the MIT License - see the LICENSE file for details. 