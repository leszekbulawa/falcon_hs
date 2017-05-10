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
<h2>Body</h2>
<form method="post">
<input type="text" name="input">
<input type="submit" name="button" value="submit">
</form>
</body>
</html>
'''
    def on_post(self, req, resp):
        req_text = req.stream.read().decode('utf-8')
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/json'
        d = {'req_text': req_text}
        resp.body = json.dumps(d)


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
