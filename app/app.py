from flask import Flask

app = Flask(__name__)

#  workspace.logger や print を使用可能にする
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!!!!!!"


if __name__ == "__main__":
    app.run()
