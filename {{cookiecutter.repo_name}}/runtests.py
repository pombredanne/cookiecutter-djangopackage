import sys

try:
    from django.conf import settings
    from django_nose import NoseTestSuiteRunner
except ImportError:
    raise ImportError("To fix this error, run: pip install -r requirement-text.txt")

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="{{ cookiecutter.app_name }}.urls",
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "{{ cookiecutter.app_name }}",
    ],
    SITE_ID=1,
    # Custom project settings go here


)

test_runner = NoseTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(["."])

if failures:
    sys.exit(failures)
