from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def hello():
    n = random.random() * 3
    time.sleep(n)
    return "You waited for {} seconds!".format(n), 400

def create_app():
    return app

if __name__ == "__main__":
    app.run(host='0.0.0.0')