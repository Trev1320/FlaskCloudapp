from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Its Trevor Otieno Here"

if __name__ == '__main__':
    app.run()