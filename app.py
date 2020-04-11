from flask import Flask,request
import json


app = Flask(__name__)


@app.route('/users',methods=["GET"])
def users():
    if request.method == "GET":
        data = [{"username":"1","password":"1"},
                {"username":"2","password":"2"},
                {"username":"3","password":"3"}]
        return json.dumps(data),200
    else:
        data = {
            "code":"500",
            "message":"只支持GET请求"
        }
        return json.dumps(data),400


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
