from flask import Flask, request

app = Flask(__name__)

dict = {'name': "", "pwd": ""}
@app.route("/user_reg", methods=["GET"])

def user_reg():
    username = request.args.get("username")
    password = request.args.get("password")
    dict['name'] = username
    dict['pwd'] = password

    return {"login created successfully " : dict}

@app.route("/user_auth", methods=["GET"])

def user_auth():
    username = request.args.get("username")
    password = request.args.get("password")

    check_dict = {"username": username, "password": password}
    if (dict['name'] != check_dict['username']):
        return "access denied, invalid username"
    elif(dict['pwd'] != check_dict['password']):
        return "access denied, invalid password"
    else:
        return "login succfully"
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)