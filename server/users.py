import json
import os

USERS_FILE = "server/database/users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def create_user(name, password):
    users = load_users()
    user = {"name": name, "password": password}
    users.append(user)
    save_users(users)
    print("User created:", user)
    return user

def get_user(name):
    users = load_users()
    for user in users:
        if user["name"] == name:
            return user
    return None

def update_user(name, new_password):
    users = load_users()
    for user in users:
        if user["name"] == name:
            user["password"] = new_password
            save_users(users)
            return True
    return False

def delete_user(name):
    users = load_users()
    updated = [u for u in users if u["name"] != name]
    save_users(updated)
    return True                                                                