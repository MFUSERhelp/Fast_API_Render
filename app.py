from flask import Flask
import requests
import json

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/', methods = ['GET', 'POST'])
def get_mf():
    # scheme_code = str(request.args.get('input'))
    API_ENDPOINT = r"https://pulsedb.pulselabs.co.in/rest/api/v1/screener/search"
    data = {
            "auth": "zR3w_WoBHZubHyRVAF0l",
            "plan_name": "broker",
            "scheme_code": "144342",
            "holding_period": "1Y"
            }
    r = requests.post(url = API_ENDPOINT, data = data)
    pastebin_url = r.text
    json_object = json.loads(pastebin_url)
    return json_object


if __name__ == '__main__':
    app.run()
