import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channel_tutorial.settings')

application = get_asgi_application()
