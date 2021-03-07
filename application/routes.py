from typing import Type
from flask import Flask, request, Response
from remote import find_one, insert_one
import json

app = Flask("owid_covid")

@app.route("/", methods=["GET"])
def index():
    return {"Home": "Sweet Home"}

@app.route("/insert", methods=['POST'])
def insert():
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))

        insert_one(dict_body)
    except:
        return Response("Invalid JSON", status=400)

    return "OK"

app.run()