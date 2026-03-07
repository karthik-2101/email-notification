from flask import Blueprint, request, jsonify
import logging
from app.service import create_user

logger = logging.getLogger(__name__)

user_bp = Blueprint("users", __name__, url_prefix="/users")


@user_bp.route("", methods=["POST"])
def create_user_endpoint():
    data = request.get_json()
    logger.info("Received request to create user: %s", data)
    try:
        user = create_user(data)

        return jsonify({
            "id": str(user.id),
            "email": user.email,
            "message": "User created successfully"
        }), 201

    except ValueError as e:
        logger.warning("User creation failed: %s", e)
        return jsonify({"error": str(e)}), 400