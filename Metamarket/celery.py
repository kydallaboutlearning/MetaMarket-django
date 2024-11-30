#importing requirements
import os
from celery import  Celery
import django as django


#setting the django environment

os.environ.setdefault("DJANGO_SETTINGS_MODULE","Metamarket.settings")

app = Celery('Metamarket')
app.config_from_object('django.conf:settings',namespace = 'CELERY')
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')