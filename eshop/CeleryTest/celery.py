import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryTest.settings')

app = Celery('CeleryTest')

app.config_from_object('CeleryTest.settings', namespace='CELERY')

# app.conf.task_routes = {
#     'notifications.tasks.send_discount_email': {'queue': 'queue1'},
#     'notifications.tasks.send_data_for_ml': {'queue': 'queue2'},
# }

app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

