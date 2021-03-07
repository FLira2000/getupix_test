from typing import Type
from flask import Flask, request, Response
from remote import find_one, insert_one
import json
app = Flask("owid_covid")

@app.route("/", methods=["GET"])
def index():
    return {"Home": "Sweet Home"}

# insere um novo documento, não levando em consideração EXATAMENTE O QUE
# parte do ponto de partida do document based database, que é extensível e permite modificações on the air
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

# busca por um documento no bd, por json
# classico do bd
@app.route("/search", methods=['GET'])
def search():
    returnable = None
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))

        returnable = find_one(dict_body)
    except:
        return Response("Invalid JSON", status=400)
    
    if '_id' in list(returnable.keys()):
        del(returnable['_id'])
    else:
        return Response("Could not find any document with those informations", status=404)
    return returnable

#@app.route("/insert")

app.run()