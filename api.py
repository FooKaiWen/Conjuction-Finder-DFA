import flask
from flask import request, jsonify
from flask_cors import CORS
from dfa import dfa_api

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/api/', methods=['GET'])
def api_id():
    text = ""
    if 'text' in request.args:
        text = str(request.args['text'])
    
    status = False
    status = dfa_api(text)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(status)

app.run()