# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a full-stack web application with a Django backend and Vue 3 frontend. The backend provides REST APIs with JWT authentication, while the frontend is a single-page application built with Vue 3, Vue Router, and Pinia state management.

## Architecture

### Backend (Django)
- **Location**: `backend/`
- **Django project**: `backend/backend/`
- **Django app**: `backend/web/` - main application
- **Database**: SQLite (`backend/db.sqlite3`)
- **Authentication**: JWT tokens via `django-rest-framework` and `django-rest-framework-simplejwt`
- **API routes**: Defined in `backend/web/urls.py`
- **Static files**: Frontend build outputs to `backend/static/frontend/`
- **CORS**: Configured to allow `http://localhost:5173` (Vite dev server)

### Frontend (Vue 3 + Vite)
- **Location**: `frontend/`
- **Build tool**: Vite
- **Framework**: Vue 3 with Composition API
- **State management**: Pinia
- **Routing**: Vue Router
- **Development server**: Vite dev server on port 5173
- **Build output**: Generated files are placed in `backend/static/frontend/`

### Static File Handling
- In development: Django serves static files from `backend/static/frontend/assets/` at `/assets/` URL
- In production: Static files should be served by a web server (nginx/Apache) or CDN
- Django templates use `{% static 'frontend/assets/...' %}` to reference built files
- The main template is at `backend/web/templates/index.html`

## Development Commands

### Frontend Development
```bash
cd frontend
npm install          # Install dependencies
npm run dev         # Start Vite dev server (port 5173)
npm run build       # Build for production (outputs to backend/static/frontend/)
npm run preview     # Preview production build locally
```

### Backend Development
```bash
cd backend
# Activate virtual environment first (if using .venv)
# On Windows: .venv\Scripts\activate
# On Unix/Mac: source .venv/bin/activate
python manage.py runserver  # Start Django dev server (port 8000)
python manage.py migrate    # Apply database migrations
python manage.py createsuperuser  # Create admin user
```

### Running Both Servers
1. Start Django backend: `cd backend && python manage.py runserver`
2. Start Vue frontend: `cd frontend && npm run dev`
3. Access the app at `http://localhost:5173` (frontend) or `http://localhost:8000` (Django-served version)

## Key Configuration Files

### Django Settings (`backend/backend/settings.py`)
- `DEBUG = True` - Development mode
- `STATIC_URL = "static/"`
- `STATICFILES_DIRS = [BASE_DIR / 'static']` - Development static files
- `CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]`
- JWT authentication configured with 2-hour access tokens

### Vite Configuration (`frontend/vite.config.js`)
- Vue 3 plugin with devtools
- Build output directory: `../backend/static/frontend`

### URL Routing
- Django admin: `/admin/`
- JWT token endpoints: `/api/token/`, `/api/token/refresh/`
- Frontend assets: `/assets/` (development only)
- Media files: `/media/` (development only)

## Development Notes

### Static File References in Templates
Always use Django's `{% static %}` tag in templates:
```html
<!-- Correct -->
<link rel="stylesheet" href="{% static 'frontend/assets/index.css' %}">

<!-- Incorrect (hardcoded path) -->
<link rel="stylesheet" href="/assets/index.css">
```

### Frontend-Backend Integration
1. Frontend makes API calls to `http://localhost:8000` (Django server)
2. Authentication: Include JWT token in `Authorization: Bearer <token>` header
3. CORS is configured to allow requests from `http://localhost:5173`

### Database
- Uses SQLite by default
- Migration files are in `backend/web/migrations/`
- Run `python manage.py makemigrations` after model changes

## Project Structure
```
AIFriend/
├── backend/                 # Django backend
│   ├── backend/            # Django project settings
│   │   ├── settings.py     # Main configuration
│   │   └── urls.py         # URL routing
│   ├── web/                # Django app
│   │   ├── templates/      # HTML templates
│   │   ├── urls.py         # App URLs (API endpoints)
│   │   └── viwes/          # View functions (note: typo "viwes")
│   ├── static/frontend/    # Built frontend assets
│   └── manage.py           # Django CLI
├── frontend/               # Vue 3 frontend
│   ├── src/                # Vue components
│   ├── package.json        # Dependencies and scripts
│   └── vite.config.js      # Vite configuration
└── CLAUDE.md               # This file
```