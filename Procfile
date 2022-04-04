release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input


web: gunicorn authTemplate.wsgi --preload --log-file –