from celery import Celery

app = Celery('tasks', )

app.config_from_object('celery_config')



