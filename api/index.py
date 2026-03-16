"""
Serverless handler for Django on Vercel.

- Vercel automatically provides environment variables; no manual .env loading needed.
- Sets DJANGO_SETTINGS_MODULE to `japhestech.settings`.
- Initializes Django’s WSGI application via get_wsgi_application().
- Wraps the WSGI app with WhiteNoise so collected static files in STATIC_ROOT are served at /static/.
- Exposes `app`, which Vercel’s Python runtime looks for.
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Add project root (one level above api/) to Python path so imports resolve
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Ensure Django knows which settings to use (overridden by Vercel env if set)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japhestech.settings")

# Initialize the standard Django WSGI application
django_app = get_wsgi_application()

# Serve static files collected into STATIC_ROOT at the /static/ URL prefix
static_root = os.getenv("STATIC_ROOT", str(BASE_DIR / "staticfiles"))
app = WhiteNoise(django_app, root=static_root, prefix="static/")
