from flask import Flask

app = Flask(__name__)


# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    return "login page"


if __name__ == '__main__':
    app.run(port=8000, debug=True)