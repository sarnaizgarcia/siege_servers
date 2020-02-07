import json

from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    with open('../happy_path.json', 'r') as f:
        response = json.load(f)
        return jsonify(response)

if __name__ == "__main__":
    app.run()