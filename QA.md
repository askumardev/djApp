# Django QA: Project Code Review

## 1. What is the difference between `djApp/urls.py` and `challenges/urls.py`?

`djApp/urls.py` is the project-level URL configuration. It defines top-level routes such as `challenge/` and `challenges/` and uses `include('challenges.urls')` to hand control to the app.

`challenges/urls.py` is the app-level URL configuration. After the prefix is stripped, it matches the remaining path segments and dispatches to views like `index`, `monthly_challenge_by_number`, and `monthly_challenge`.

## 2. How does Django resolve `/challenge/february/`?

Django starts in `djApp/urls.py`, finds the `path('challenge/', include('challenges.urls'))` rule, and forwards the request to `challenges/urls.py` with `february/` remaining. `challenges/urls.py` then matches `<str:month>/` and calls `views.monthly_challenge(request, 'february')`.

## 3. What is the difference between `HttpResponse` and `HttpResponseRedirect`?

`HttpResponse` returns a normal page response with HTML content, status code, and headers. `HttpResponseRedirect` returns a 302 redirect response, instructing the browser to request a different URL. This project uses `HttpResponseRedirect` in `monthly_challenge_by_number` to convert numeric URLs like `/challenge/3/` into named month URLs.

## 4. What are path converters and how are they used here?

Path converters are the `<int:...>` and `<str:...>` patterns inside `path()` definitions. In `challenges/urls.py`, `<int:month>/` matches numeric month indexes and `<str:month>/` matches named month strings. They automatically convert captured path segments to Python values before passing them to the view.

## 5. What does `reverse('monthly-challenge', args=[month])` do?

`reverse()` builds a URL from a named route instead of hard-coding the path string. Here it resolves the `monthly-challenge` route defined in `challenges/urls.py` and returns a URL like `/challenge/february/`. That makes links stable when URL patterns change.

## 6. What does the `monthly_challenge` view do, and what is missing in the current template?

The view looks up the requested month in the `monthly_challenges` dictionary, renders `challenges/challenge.html` using `render_to_string()`, and returns the rendered HTML.

However, the current template does not display the passed context values like `month_name` or `text`, so the generated page still shows only static content. To use the context, the template should include placeholders like `{{ month_name }}` and `{{ text }}`.

## 7. What happens when a month is not supported or a number is out of range?

If the named month key is missing from `monthly_challenges`, `monthly_challenge()` catches the error and returns `HttpResponseNotFound("This month is not supported...")`.

If the numeric month is less than 1 or greater than 12, `monthly_challenge_by_number()` returns `HttpResponseNotFound("Month number out of range...")`.

## 8. Why do we use a virtual environment and `.gitignore` in this project?

The virtual environment isolates project dependencies such as Django from the system Python environment. It keeps package versions local to the project.

`.gitignore` ensures generated files like `venv/`, `db.sqlite3`, and `__pycache__/` are not committed to git, which keeps the repository clean and portable.
