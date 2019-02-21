print("Server starting...")
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def index():
	# Placeholder, will get the frontend later
	return "<h1>I'm running</h1>"
