"""
Serverless handler for Django on Vercel.
"""

import os
import sys
from pathlib import Path

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japhestech.settings")

django_app = get_wsgi_application()

# Serve checked-in source assets directly so deployment does not depend on collectstatic packaging.
app = WhiteNoise(django_app)
app.add_files(str(BASE_DIR / "techie" / "static"), prefix="static/")

# Also serve collectstatic output if it exists.
collectstatic_dir = Path(settings.STATIC_ROOT)
if collectstatic_dir.exists():
    app.add_files(str(collectstatic_dir), prefix="static/")
