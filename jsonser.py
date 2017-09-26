import json
from flask import Response
from flask import Flask
app = Flask(__name__)
@app.route("/", methods=["GET"])
def get_json2():
    data = {
        "abandon":{"123456":[
                                    [1,2,3,4],
                                    [5,6,7,8]
                                ],
                    "654321":[
                                    [1, 2, 3, 4],
                                    [5, 6, 7, 8]
                                ]
                    }
    }
    format = json.dumps(data)
    return Response(
        response=format,
        mimetype="application/json",
        status=200
    )
app.run()
