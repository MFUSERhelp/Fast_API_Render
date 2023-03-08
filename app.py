from flask import Flask, request
import requests
import json
from datetime import date, timedelta

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/', methods = ['GET', 'POST'])
def get_mf():
    scheme_code = str(request.args.get('input'))
    # print("#########",scheme_code)
    API_ENDPOINT1 = r"https://pulsedb.pulselabs.co.in/rest/api/v1/screener/search"
    API_ENDPOINT2 = r"https://pulsedb-qa.pulselabs.co.in/rest/api/v1/mf/nav-history"
    auth = "zR3w_WoBHZubHyRVAF0l"
    to_date = str(date.today())
    from_date = str(date.today()-timedelta(days=365))
    data = {
            "auth": auth,
            "plan_name": "broker",
            "scheme_code": scheme_code,
            "holding_period": "1Y"
            }
    r = requests.post(url = API_ENDPOINT1, data = data)
    pastebin_url = r.text
    json_object = json.loads(pastebin_url)["data"][0]
    data = {
            "auth": auth,
            "scheme_code": scheme_code,
            "from": from_date,
            "to": to_date,
            "frequency": "month"
            }
    r = requests.post(url = API_ENDPOINT2, data = data)
    pastebin_url = r.text
    json_object1 = json.loads(pastebin_url)["data"]
    # print(json_object[0])
    json_object.update(json_object1)
    # json_object = json.loads(
    # json_object[0]
    return json_object


# x = get_mf()
# print(x)
if __name__ == '__main__':
    app.run()
