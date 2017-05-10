import falcon
import json

from wsgiref.simple_server import make_server


class ThingsResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        resp.body = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Body</h1>
</body>
</html>
'''


class JsonResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/json'
        d = {'message': 'Hello World!'}
        resp.body = json.dumps(d)


app = falcon.API()

things = ThingsResource()
json_resource = JsonResource()

app.add_route('/things', things)
app.add_route('/other', json_resource)

httpd = make_server('', 8000, app)
print("Serving on port 8000...")

httpd.serve_forever()
