"""
Serverless entrypoint for Django on Vercel.

- Vercel injects environment variables automatically (no .env load needed).
- Sets DJANGO_SETTINGS_MODULE to japhestech.settings.
- Initializes the Django WSGI application.
- Wraps the app with WhiteNoise to serve /static/ from STATIC_ROOT.
- Exposes `app`, which Vercel’s Python runtime expects.
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Add project root (one level above api/) to Python path so imports resolve
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Configure Django settings for this serverless process
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japhestech.settings")

# Initialize Django WSGI application
django_app = get_wsgi_application()

# Serve collected static files from STATIC_ROOT at /static/
static_root = os.getenv("STATIC_ROOT", str(BASE_DIR / "staticfiles"))
app = WhiteNoise(django_app, root=static_root, prefix="static/")
