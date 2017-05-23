import falcon
import json
import jinja2
import os

from urllib import parse
from wsgiref.simple_server import make_server


class ThingsResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
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
        req_args = parse.parse_qs(req.stream.read().decode('utf-8'))  # get the message and parse it to dictionary
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/json'
        resp.body = json.dumps(req_args)


class JsonResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/json'
        content = {'message': 'Hello World!'}
        resp.body = json.dumps(content)


env = jinja2.Environment(
    loader=jinja2.PackageLoader('templates', '.')
)

class TemplateResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        template = env.get_template('test_template.j2')
        users = [
            User('ann', 'Ann'),
            User('bob', 'Bob'),
            User('charlie', 'Charlie')
        ]
        resp.body = template.render(title='TEST', users=users)


class User:
    def __init__(self, url, username):
        self.url = url
        self.username = username


app = falcon.API()

things = ThingsResource()
json_resource = JsonResource()
template_resource = TemplateResource()

app.add_route('/things', things)
app.add_route('/other', json_resource)
app.add_route('/template', template_resource)

httpd = make_server('', 8000, app)
print("Serving on port 8000...")

httpd.serve_forever()
