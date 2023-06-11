from urllib import parse

from aiohttp import web


async def test(request: web.Request):

    params = dict(parse.parse_qsl(parse.urlsplit(str(request.url)).query))
    data = await request.text()

    resp = web.Response(text=f"{params}\n{data}")

    return resp


app = web.Application()
app.add_routes([web.post('/test', test)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
