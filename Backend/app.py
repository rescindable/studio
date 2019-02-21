# main webserver
print("Server starting...")
from flask import Flask, request, Response
import json

app = Flask(__name__)

errors = ""
try:
	header = open("../Frontend/html/header.html").read()
except:
	errors = errors+"[!] Couldn't get all the files to serve"

@app.route('/')
def index():
	# Placeholder, will get the frontend later
	return "<h1>Git test!</h1>"+"<script>console.log(\""+errors+"\");</script>"

