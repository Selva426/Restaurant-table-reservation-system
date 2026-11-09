import os

os.environ.setdefault("DJANGO_SECRET_KEY", "test-only-key-not-for-deployment")
os.environ.setdefault("DB_NAME", "test_database")
os.environ.setdefault("DB_USER", "test_user")
os.environ.setdefault("DB_PASSWORD", "test_password")

from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}