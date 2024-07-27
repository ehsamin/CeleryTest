import os
from celery import Celery
from django.conf import settings
from kombu import Exchange, Queue
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryTest.settings')

app = Celery('CeleryTest')

app.config_from_object('CeleryTest.settings', namespace='CELERY')

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]
app.conf.task_acts_late = True #acknowladge
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1 #dune dune worker anjam mide chan ta chan ta bardare alan yeke 1 ki 1ki barmidare
app.conf.worker_concurrency = 1 #hamzaman 1 1ki  1ki anham mide


#     'notifications.tasks.send_discount_email': {'queue': 'queue1'},
#     'notifications.tasks.send_data_for_ml': {'queue': 'queue2'},
# }


# app.conf.task_default_rate_limit = '1/m'

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

