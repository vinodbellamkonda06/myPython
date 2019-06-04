import json

from tornado.httpclient import HTTPClient

#response = HTTPClient().fetch("https://www.github.com").body
response=HTTPClient().fetch("google")

print(dir(response))
data = json.loads(response)
print(data)
tls_version = data["tls_version"]

print(tls_version)