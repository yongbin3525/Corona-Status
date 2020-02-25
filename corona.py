import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS

URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
app = Flask(__name__)
CORS(app)

@app.route('/corona')
def corona_status():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    status = str(soup.find("ul", {"class": "s_listin_dot"}).find_all('li')).replace(",", "")
    status = re.findall("\d+", status)
    print(status)

    return jsonify({"infected": status[0], "restore": status[1], "die": status[2], "sus": status[3]})


if __name__ == "__main__":
    app.run()
