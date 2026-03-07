from celery import Celery
from flask_mail import Message
from app.db import mail

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

def make_celery(app):
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery

@celery.task
def send_email(to, subject, body):
    msg = Message(
    subject=subject,
    recipients=[to],
    body=body,
    sender="no_reply@example.com"
)

    mail.send(msg)
