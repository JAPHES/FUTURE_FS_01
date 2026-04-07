# Japhestech Portfolio (Django 5)

Personal portfolio site built with Django and deployed on Vercel using Python serverless functions plus WhiteNoise for static files.

## Stack
- Python / Django 5
- WhiteNoise for static assets
- Vercel serverless runtime (`@vercel/python`)

## Local Development
1) Create and activate a virtualenv.  
2) Install deps: `pip install -r requirements.txt`  
3) Run migrations (none needed for the static site, but Django expects a DB): `python manage.py migrate`  
4) Start dev server: `python manage.py runserver`  
   - Static files are served by Django in debug.

## Deployment (Vercel)
- Build: `bash build_files.sh` (installs deps and runs `collectstatic`)  
- Static files: collected into `/public/static` and served by Vercel's filesystem handler  
- Serverless entrypoint: `api/index.py` (WSGI wrapped with WhiteNoise as a fallback)  
- Routes: filesystem first, then all remaining requests go to `api/index.py`  
- Required env vars:
  - `DJANGO_SETTINGS_MODULE=japhestech.settings`
  - `SECRET_KEY=your-secret-key`
  - `DEBUG=False`
  - `VERCEL_URL=japhestech.vercel.app`

## Live Site
https://japhestech.vercel.app/
