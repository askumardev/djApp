## Installation steps

```
- python3
- python3 --version
- sudo apt install -y python3-pip python3-venv
- python3 -m pip install Django
```

## App creation and server steps

```
- django-admin startproject djApp
- python manage.py startapp challenges
- source .venv/bin/activate
- python3 manage.py runserver
```

## Accessible challenge URLs

- http://127.0.0.1:8000/challenge/ or http://127.0.0.1:8000/challenges/
- http://127.0.0.1:8000/challenge/january/ or http://127.0.0.1:8000/challenges/january/
- http://127.0.0.1:8000/challenge/february/ or http://127.0.0.1:8000/challenges/february/
- http://127.0.0.1:8000/challenge/3/ or http://127.0.0.1:8000/challenges/3/

## Django request / response cycle

1. Browser sends HTTP request
   - Example: `GET http://127.0.0.1:8000/challenge/`
2. WSGI/ASGI server receives request
   - In development, `python manage.py runserver` uses Django’s built-in server
3. Django creates an `HttpRequest` object
   - Parses method, path, headers, query parameters, form data, cookies
4. Middleware `process_request` runs
   - Middleware can inspect or modify the request before it reaches the view
5. URL dispatcher matches the path
   - Django starts with the project `urls.py` and follows any included URLconfs
   - The matched pattern may capture path parameters like `<str:month>` or `<int:month>`
   - Those parameters are passed into the view as function arguments
   - If no route matches, Django returns a 404 response
6. View function executes
   - The view receives `request` plus any URL parameters
   - It can read query data, use models, render templates, redirect, or return errors
   - In this app, `monthly_challenge` looks up the month text and returns it
   - `monthly_challenge_by_number` converts a number to a month name and redirects
   - The view can also use `reverse()` to build URLs from named routes
     - Example: `reverse('monthly-challenge', args=['january'])`
     - This keeps links stable even if URL patterns change
7. View returns an `HttpResponse`
   - Includes status code, headers, and body content
8. Middleware `process_response` runs
   - Middleware can modify the response before it is sent back
9. The server sends the HTTP response back to the browser
10. Browser renders the response or follows redirects
