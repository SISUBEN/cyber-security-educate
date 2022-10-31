from audioop import add
from flask import Flask, render_template, request
import logging
import re
import json


try:
    app = Flask(__name__)
    LOG_FORMAT = "[%(asctime)s] [%(levelname)s] > %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    file = open("scores.json", "w")
    scores = json.loads(file) # global read
    # {
    #     "addr":scores
    # }

    def initScores(addr: int, score: float|int) -> dict:
        scores[addr] = score
        file.write(scores)
        return scores
    
    def addScores(addr: int, score: float|int) -> dict:
        try:
            scores[addr] = scores[addr] + scores
            file.write(scores)
            return scores
        except KeyError:
            score[addr] = 0 + scores #init

    def removeScores(addr: int, score: float|int) -> dict:
        try:
            scores[addr] = scores[addr] - scores
            file.write(scores)
            return scores
        except KeyError:
            score[addr] = 0 - scores #init

    @app.route("/")
    def index():
        # init user scores
        initScores(addr=request.remote_addr, score=0)
        return render_template("index.html")


    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            addr = request.remote_addr
            username = request.form["username"]
            password = request.form["password"]
            if re.match(r'^e[0-9]{6}$', username):
                # bad action, get 0 scores
                logging.info(f"IP addr:{addr}")
                logging.info(f"username:{username}")
                logging.info(f"password:{password}")
                del username, password, addr # del userdata
                return render_template("rickroll.html")
                # return render_template("badAction.html", contant="(一)當朋友傳送訊息要求協助匯款或代購遊戲點數時，務必提高警覺，撥通電話再行確認。<br/>"\
                #                                                  "(二)多組帳號勿使用同組密碼，避免因帳號遭破解被盜用，並應定期更改密碼。<br/>"\
                #                                                  "(三)避免在公用電腦登入私人帳號密碼使用。<br/>"\
                #                                                  "(四)如果訊息中帶有不明連結，請先向發送訊息的朋友確認。<br/>"\
                #                                                  "(五)勿下載來源不明或非官方認證應用程式，以免個資外洩。<br/>"
                #                                                  "(六)如果陌生網站叫你填寫社交網站賬戶或密碼，確認是否是官方網站，避免賬號密碼泄露")
            else:
                render_template("login.html")
        else:
            return render_template("login.html")
        return render_template("login.html")
    
    @app.route()
    def leave():
        # good action, get 10 scores
        addrees = request.remote_addr
        addScores(addr=addrees, score=10)
        return render_template("goodAction.html", score=scores[addrees])


    if __name__ == "__main__":
        app.run(debug=True, port=8080)
except:
    file.close()
finally:
    file.close()