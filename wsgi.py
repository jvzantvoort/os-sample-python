from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    retv = dict()
    for k, v in os.environ.iteritems():
        retv += "%s: %s\n" % (k, v)
    return retv

if __name__ == "__main__":
    application.run()
