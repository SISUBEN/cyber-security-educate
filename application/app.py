#coding=utf-8
from flask import Flask, render_template, request, abort
import logging
import re
import json

app = Flask(__name__)
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] > %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
scores = {}
black_list = []

def readScore():
    with open("scores.json", "r") as file:
        s = file.read()
        scores = json.loads(s)
    return scores

scores = readScore()
def saveScore():
    with open("scores.json", "w") as file_w:
        file_w.write(json.dumps(scores))
        

def initScores(addr: str, score: float|int) -> dict:
    scores[str(addr)] = score
    return scores
    
def addScores(addr: str, score: float|int) -> dict:
    scores[str(addr)] = scores[str(addr)] + score
    return scores

def removeScores(addr: str, score: float|int) -> dict:
    scores[str(addr)] = scores[str(addr)] - score
    return scores
    
@app.route("/")
def index():
    # init user scores
    addr = request.remote_addr
    readScore()

    if addr not in black_list:
        initScores(addr, 0)
        logging.info(f"Student {addr} requsted / ")
        saveScore()
        return render_template("index.html")
    else:
        abort(404)


@app.route("/login", methods=["POST", "GET"])
def login():
    addr = request.remote_addr
    if request.method == "POST":
        if addr not in black_list:
            username = request.form["username"]
            password = request.form["password"]
            if re.match(r'^e[0-9]{6}$', username):
                # bad action, get 0 scores
                logging.info(f"IP addr:{addr}")
                logging.info(f"username:{username}")
                logging.info(f"password:{password}")
                del username, password # del userdata
                # return render_template("rickroll.html")
                removeScores(addr, 10)
                saveScore()
                black_list.append(addr)
                return render_template("badAction.html", contant="(一)當朋友傳送訊息要求協助匯款或代購遊戲點數時，務必提高警覺，撥通電話再行確認。\n"\
                                                                "(二)多組帳號勿使用同組密碼，避免因帳號遭破解被盜用，並應定期更改密碼。\n"\
                                                                "(三)避免在公用電腦登入私人帳號密碼使用。\n"\
                                                                "(四)如果訊息中帶有不明連結，請先向發送訊息的朋友確認。\n"\
                                                                "(五)勿下載來源不明或非官方認證應用程式，以免個資外洩。\n"
                                                                "(六)如果陌生網站叫你填寫社交網站賬戶或密碼，確認是否是官方網站，避免賬號密碼泄露")
            else:
                render_template("login.html")
        else:
            abort(403)
    else:
        return render_template("login.html")
    return render_template("login.html")

@app.route("/leave")
def leave():
    # good action, get 10 scores
    addr = request.remote_addr
    if addr not in black_list:
        addScores(addr, 10)
        saveScore()
        black_list.append(addr)
        return render_template("goodAction.html", scores=scores[addr])
    else:
        abort(403)
if __name__ == "__main__":
    app.run(debug=True, port=8080)
    # file have other solution