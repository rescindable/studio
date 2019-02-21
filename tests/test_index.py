from urllib.parse import urlencode
import json

def call (client, path, params):
	url = path+'?'+urlencode(params)
	response = client.get(url)
	return response

def test_index(client)
	result = call(client, '/', '')
	# Fetch the index here
	assert result == "<h1>I'm running</h1>"
