from flask import Flask,jsonify, jsonify,request,send_from_directory
import auth

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("../client", "index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    result=auth.register_user(username,password)
    return jsonify(result)
            
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    result=auth.login_user(username,password)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000,debug=True)