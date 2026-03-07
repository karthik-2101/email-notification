from app.db import db
from app.model import User
import uuid
from sqlalchemy.exc import IntegrityError

def create_user(data):
    from app.tasks import send_email
    try:
        user = User(
            id=uuid.uuid4(),
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone_number=data.get("phone_number"),
        )

        db.session.add(user)
        db.session.commit()

        send_email.delay(user.email, "Welcome!", "Your account has been created.")

        return user

    except IntegrityError:
        db.session.rollback()
        raise ValueError("Email already exists")
