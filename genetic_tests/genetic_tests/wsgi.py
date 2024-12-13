# genetic_tests/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'genetic_tests.settings')

application = get_wsgi_application()
