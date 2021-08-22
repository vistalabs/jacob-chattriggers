from flask import Flask, request, url_for
import json
from flask import json as jsn

def store(file, key=None):
    with open(file, 'r') as v:
        x = json.load(v)
    if x is None: return
    with open(file, 'w') as v:
        json.dump(key, v, indent=4)
    return

api = Flask(__name__)

@api.route('/upload', methods=['POST'])
def post_upload():
	e = request.data.decode("UTF-8")
	j = json.loads(e)
	store('events.json', j['events'])
	return jsn.dumps({"success": "true"}), 201

api.run()
