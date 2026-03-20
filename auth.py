import json
from functools import wraps
from flask import session, redirect, url_for, flash

USERS_FILE = "users.json"


def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def authenticate(username, password):
    users = load_users()
    user = users.get(username)
    if user and user["password"] == password:
        return {
            "username": username,
            "role": user["role"],
            "name": user["name"],
            "company": user["company"],
            "country": user["country"]
        }
    return None


def login_required(role=None):
    """Decorator — protects routes. Optionally restricts to a specific role."""
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if "user" not in session:
                flash("Please log in to continue.", "error")
                return redirect(url_for("login"))
            if role and session["user"]["role"] != role:
                flash("You don't have permission to access that page.", "error")
                return redirect(url_for("dashboard"))
            return f(*args, **kwargs)
        return decorated
    return decorator


def current_user():
    return session.get("user")
