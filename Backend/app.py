# main webserver
print("Server starting...")
from flask import Flask, request, Response
import json

app = Flask(__name__)

errors = ""
try:
	header = open("../Frontend/html/header.html").read()
	footer = open("../Frontend/html/footer.html").read()
	mainScript = open("../Frontend/js/main.js").read()
	loader = open("../Frontend/html/loader.html").read()
	loaderstyle = open("../Frontend/css/loader.css").read()
	skeleton = open("../Frontend/html/skeleton.html").read()
except:
	errors = errors+"[!] Couldn't get all the files to serve"

@app.route('/')
def index():
	index = header+loader+footer
	return index+"<script>console.log(\""+errors+"\");</script>"

@app.route('/skeleton')
def getSkeleton():
	return Response(skeleton, mimetype="text/html")

@app.route('/main')
def jsmain():
	return Response(mainScript, mimetype="text/javascript")

@app.route('/loaderstyle')
def getloaderstyle():
	return Response(loaderstyle, mimetype="text/css")
