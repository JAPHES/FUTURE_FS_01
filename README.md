# Japhestech Portfolio (Django 5)

Personal portfolio site for Japhes Murithi - an IT Technician and Fullstack Developer. Built with Django and deployed on Vercel using Python serverless functions plus WhiteNoise for static files.

## About
Passionate IT Technician with deep faith, honesty, and diligence. Expert in solving complex problems with precision and efficiency, showcasing a keen eye for detail and adherence to instructions. My passion lies in creating impactful digital experiences across various platforms, combining technical expertise and creativity.

## Stack
- Python / Django 5
- WhiteNoise for static assets
- Vercel serverless runtime (`@vercel/python`)
- Bootstrap 5 for responsive UI
- Swiper.js for carousels
- AOS (Animate On Scroll) for animations

## Features
- **About Section**: Professional profile showcasing expertise in problem-solving, digital innovation, and technical excellence
- **Services**: 5 services offered with icon-based visualization:
  - Web Application Development
  - UI/UX Design
  - Mentorship & Training
  - Backend API Development
  - IoT Projects (Smart device integration and embedded systems)
- **Projects**: Showcase of 6+ completed projects with GitHub links
- **FAQ**: Common questions about development process and collaboration
- **Contact**: Multiple ways to get in touch

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
  - `ALLOWED_HOSTS=japhes.secora.dev,japhestech.vercel.app,.vercel.app`
  - `CSRF_TRUSTED_ORIGINS=https://japhes.secora.dev,https://japhestech.vercel.app,https://*.vercel.app`

### Custom domain

The production portfolio uses `japhes.secora.dev`. Add this domain to the Vercel project, then create the CNAME record requested by Vercel in the `secora.dev` DNS zone:

- Type: `CNAME`
- Name/Host: `japhes`
- Value/Answer: the exact CNAME target shown by Vercel
- TTL: `300`

## Recent Updates
- ✨ Redesigned about section with new professional identity
- 🎨 Updated services with icon-based visualization (replaced images with Bootstrap icons)
- 🚀 Added IoT Projects as a new service offering
- 🔧 Improved project showcase with GitHub-first approach
- 📋 Removed testimonials section for cleaner focus

## Live Site
https://japhes.secora.dev/

## Contact
- Email: japhesmurithi@gmail.com
- Phone: 0769809329
- GitHub: [@JAPHES](https://github.com/JAPHES)
