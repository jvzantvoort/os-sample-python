from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World from %s\n\n" % os.uname()[1]

if __name__ == "__main__":
    application.run()
