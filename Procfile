release: python manage.py migrate
web: gunicorn runkeeper.wsgi --log-file -
worker: celery worker -A datauploader 