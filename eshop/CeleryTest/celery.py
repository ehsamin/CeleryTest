import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryTest.settings')

app = Celery('CeleryTest')

app.config_from_object('CeleryTest.settings', namespace='CELERY')

app.conf.task_routes = {
    'notifications.tasks.send_discount_emails': {'queue': 'queue1'}
}


app.autodiscover_tasks()


