from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

# GETメソッド、POSTメソッドの追記
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        message = request.form["message"]
        return render_template("index.html", message=message)

@app.route("/", methods = ["GET"])
def index_get():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def index_post():
    massage = request.form["message"]
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run(port=8000, debug=True)