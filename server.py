from flask import Flask, request

app = Flask(__name__)

@app.route("/sum_int", methods=["POST"])
def sum_int():
    reqJson = request.get_json()
    x = reqJson['x']
    y = reqJson['y']
    if y==0:
        return {"error": "y should not be 0"}, 400
    sum = x+y
    return {"result ": sum}

@app.route("/sum_text", methods=["POST"])
def sum():
    reqJson = request.get_json()
    x = reqJson['x']
    y = reqJson['y']
    if y==0:
        return {"error": "y should not be 0"}, 400
    sum = x+y
    return {"result ": sum}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)
    

