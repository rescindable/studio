# main webserver
print("Server starting...")
from flask import Flask, request, Response
import json

app = Flask(__name__)

errors = ""
try:
	header = open("../Frontend/html/header.html").read()
	footer = open("../Frontend/html/footer.html").read()
except:
	errors = errors+"[!] Couldn't get all the files to serve"

@app.route('/')
def index():
	index = header+"Content :)"+footer
	return index+"<script>console.log(\""+errors+"\");</script>"

