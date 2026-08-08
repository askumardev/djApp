# Django Settings Documentation

This document explains the settings in `djApp/djApp/settings.py` and what each one does.

## BASE_DIR

- `BASE_DIR = Path(__file__).resolve().parent.parent`
- Defines the project root directory.
- Used to build absolute paths for files like the database, static files, and templates.

## SECRET_KEY

- `SECRET_KEY = 'django-insecure-&!5gf91cm1-a(*pc!!=brnytfvg3k&u65pgpnu=9lnqslhlmxm'`
- A secret string used for cryptographic signing.
- Must be kept private in production to protect sessions, CSRF tokens, and password reset tokens.
- In a real app, use environment variables or a secrets manager instead of committing it.

## DEBUG

- `DEBUG = True`
- Enables debug mode, which shows detailed error pages and stack traces.
- Should only be `True` in development.
- In production, set to `False` to avoid leaking sensitive information.

## ALLOWED_HOSTS

- `ALLOWED_HOSTS = []`
- A list of hostnames/domains that the app may serve.
- When `DEBUG = False`, Django rejects requests to hosts not in this list.
- For local development, it can remain empty or contain `['localhost', '127.0.0.1']`.

## INSTALLED_APPS

- A list of enabled Django applications.
- Includes Django built-in apps and project-specific apps.
- In this project:
  - `django.contrib.admin`: Admin site
  - `django.contrib.auth`: Authentication system
  - `django.contrib.contenttypes`: Content types framework
  - `django.contrib.sessions`: Session support
  - `django.contrib.messages`: Messaging framework
  - `django.contrib.staticfiles`: Static file handling
  - `challenges`: Project app containing the monthly challenge logic

## MIDDLEWARE

- Middleware is a chain of hooks that process requests and responses.
- The configured middleware does things like security headers, sessions, CSRF protection, and authentication.
- In this project:
  - `SecurityMiddleware`: adds basic security headers
  - `SessionMiddleware`: enables session support
  - `CommonMiddleware`: basic URL and content handling
  - `CsrfViewMiddleware`: CSRF protection for POST forms
  - `AuthenticationMiddleware`: attaches `request.user`
  - `MessageMiddleware`: supports Django messages
  - `XFrameOptionsMiddleware`: prevents clickjacking

## ROOT_URLCONF

- `ROOT_URLCONF = 'djApp.urls'`
- Points to the project-level URL configuration module.
- Django loads this file first to route incoming requests.

## TEMPLATES

- Defines how Django loads and renders templates.
- `BACKEND`: Django’s built-in template engine.
- `DIRS`: custom template directories; empty here, so only app templates are used.
- `APP_DIRS = True`: enables automatic discovery of `templates/` inside installed apps.
- `context_processors`: functions that inject common context variables into templates.

## WSGI_APPLICATION

- `WSGI_APPLICATION = 'djApp.wsgi.application'`
- The callable entry point for WSGI servers.
- Used when running the app with `runserver` or any WSGI-compatible deployment.

## DATABASES

- Configures database access.
- This project uses SQLite:
  - `ENGINE = 'django.db.backends.sqlite3'`
  - `NAME = BASE_DIR / 'db.sqlite3'`
- SQLite is convenient for development and small prototypes.
- For production, use PostgreSQL, MySQL, or another supported database.

## AUTH_PASSWORD_VALIDATORS

- A list of password validation classes.
- Used by Django forms and auth when setting user passwords.
- Includes:
  - similarity validator
  - minimum length validator
  - common password validator
  - numeric password validator
- Helps enforce stronger passwords.

## LANGUAGE_CODE

- `LANGUAGE_CODE = 'en-us'`
- Default language for the project.
- Affects translations and locale formatting.

## TIME_ZONE

- `TIME_ZONE = 'UTC'`
- Default time zone for date/time handling.
- In production, set it to your server or application timezone if needed.

## USE_I18N

- `USE_I18N = True`
- Enables Django’s internationalization system.
- Allows translation of text and localized formatting.

## USE_TZ

- `USE_TZ = True`
- Enables timezone-aware datetimes.
- Recommended for correct handling of date/times across timezones.

## STATIC_URL

- `STATIC_URL = 'static/'`
- The base URL prefix for serving static files.
- In development, Django serves static files at `/static/`.
- In production, static files should be collected and served by the web server.

## MAILERS

- `MAILERS` is not a built-in Django setting.
- It appears to be a custom email configuration dictionary.
- In this project, it maps a default backend to `django.core.mail.backends.console.EmailBackend`.
- This backend prints emails to the console instead of sending them.
- Note: Django normally uses `EMAIL_BACKEND`, so this custom setting may need special handling if used.

## Notes

- This settings file is configured for development.
- Before deploying, change `DEBUG = False`, configure `ALLOWED_HOSTS`, and secure `SECRET_KEY`.
- Add `EMAIL_BACKEND` if real email sending is required.
- Add production static file settings (`STATIC_ROOT` and `MEDIA_ROOT`) if needed.
