from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    retv = str()
    for k, v in os.environ.iteritems():
        try:
            retv += "%s: %s\n" % (k, v)
        except:
            pass
    return retv

if __name__ == "__main__":
    application.run()
