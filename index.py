from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>資管二B陳喬莘的求職相關資訊網頁</h1>"
	homepage += "<a href=/myself>我的個人簡介</a><br>"
	homepage += "<a href=/MIS>MIS相關工作介紹</a><br>"
	homepage += "<a href=/Ucan>職涯測驗結果</a><br>"
	homepage += "<a href=/work>求職自傳履歷</a><br>"
	return homepage

@app.route("/myself")
def myself():
	return render_template("myself.html")

@app.route("/MIS")
def MIS():
	return render_template("MIS.html")

@app.route("/Ucan")
def Ucan():
	return render_template("Ucan.html")

@app.route("/work")
def work():
	return render_template("work.html")
	

#if __name__ == "__main__":
#	app.run()