from app.app import create_app
from app.tasks import make_celery

flask_app = create_app()
app = make_celery(flask_app)

if __name__ == "__main__":
    app.start()