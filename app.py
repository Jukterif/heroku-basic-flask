import logging
import hashlib
from requests import get

from flask import Flask
from flask import request
from flask import jsonify

app = Flask('__name__')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def main_page():
    return "NULL"

@app.route('/forsciencenevergiveup',  methods=['POST'])
def proxy():
    try:
        content = request.json
        url = content['url']
        password = content['password']
        uri = 'trytoscanthispage' + url
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15', 'Referer': 'https://google.com/'}
        try:
            headers = content['options']['headers']
        except:
            pass
        req_password = hashlib.sha1(uri.encode()).hexdigest()
        if password == req_password:
            try:
                html = get(url, headers=headers).text
                return jsonify({'html': html})
            except:
                pass
    except:
        pass

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

