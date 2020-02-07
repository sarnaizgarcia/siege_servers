import json

from sanic import Sanic
from sanic.response import json as sanic_json


app = Sanic('siege_test')

@app.route("/")
async def test(request):
    with open('../happy_path.json', 'r') as f:
        response = json.load(f)
        return sanic_json(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)