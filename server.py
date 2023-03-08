from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = 'https://fra.bornatejaratdeba.com/' + path
    response = requests.get(url, params=request.args)
    return response.content, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
