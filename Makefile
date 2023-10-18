run:
	python3 manage.py runserver
makemigrate:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
superuser:
	python3 manage.py createsuperuser
celery:
	celery -A config worker -l DEBUG

