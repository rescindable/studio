import os
from flask import request, Flask

app = Flask(__name__)

@app.route('/pull')
def reload()
	try:
		os.system('bash PullNew.sh')
		return 'success'
	except:
		return 'fail'

