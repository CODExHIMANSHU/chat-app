def create_user(name, password):
    user = {
        "name": name,
        "password": password
    }
    print("User created:", user)
    return user

def get_user(users_list, name):
    for user in users_list:
        if user["name"] == name:
            return user
    return None

def update_user(users_list, name, new_password):
    for user in users_list:
        if user["name"] == name:
            user["password"] = new_password
            return user
    return None

def delete_user(users_list, name):
    for user in users_list:
        if user["name"] == name:
            users_list.remove(user)
            return True
    return False

users = []
users.append(create_user("Himanshu", "1234"))
users.append(create_user("Sarah", "5678"))
print("Find Sarah:", get_user(users, "Sarah"))
update_user(users, "Himanshu", "newpass")
print("Updated Himanshu:", get_user(users, "Himanshu"))
delete_user(users, "Sarah")
print("After delete:", users)