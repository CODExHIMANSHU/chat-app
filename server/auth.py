import users

def register_user(username,password):
    existing_user=users.get_user(username)
    if existing_user:
        return{"success":False,"message":"Username already exists"}
    
    users.create_user(username,password)
    return{"success":True,"message":"Account created!"}

def login_user(username,password):
    existing=users.get_user(username)
    if not existing:
        return{sucess:False,"message":"User not found"}

    if existing["password"]!=password:
        return{"success":False,"message":"Wrong Password"}
    
    return{"success":True,"message":"Login successful"}