import json
from flask import Response
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_json2():
    data = {
        "abandon": [{"time": [1, 2, 3, 4],
                     "time2": [1, 2, 3, 4]}],
        "abandon2": [{"time": [1, 2, 3, 4],
                      "time2": [1, 2, 3, 4]}]

    }
    format = json.dumps(data)
    return Response(
        response=format,
        mimetype="application/json",
        status=200
    )


app.run()
