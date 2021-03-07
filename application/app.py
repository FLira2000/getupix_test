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
    id = 0
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))

        id = insert_one(dict_body).inserted_id
    except:
        return Response("Invalid JSON", status=400)

    return id

@app.route("/search", methods=['GET'])
def search():
    returnable = None
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))

        returnable = find_one(dict_body)
    except:
        return Response("Invalid JSON", status=400)
    
    if returnable != None:
        del(returnable['_id'])
    return returnable

app.run()