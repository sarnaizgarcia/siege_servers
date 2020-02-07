from aiohttp import web
import json


async def handle(request):
    with open('../happy_path.json', 'r') as f:
        response = json.load(f)
        return web.json_response(response)

app = web.Application()
app.add_routes([web.get('/', handle)])

if __name__ == '__main__':
    web.run_app(app)