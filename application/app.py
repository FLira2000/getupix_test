from typing import Type
from flask import Flask, request, Response
from remote import find_one, insert_one
from data_preparation import document_handler
import json
app = Flask("owid_covid")

@app.route("/", methods=["GET"])
def index():
    return {"Home": "Sweet Home"}

# insere um novo documento, não levando em consideração EXATAMENTE O QUE
# parte do ponto de partida do document based database, que é extensível e permite modificações on the air
@app.route("/insert", methods=['POST']) 
def insert():
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))
        insert_one(dict_body)
    except:
        return Response("Invalid JSON", status=400)

    return "OK"

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

# insere um novo documento baseado num JSON enviado, mas que precisa ter a mesma cara de outros documentos
# implica em ser ou o primeiro a ser adicionado de uma serie temporal ou uma serie temporal completa
@app.route("/insert_complete", methods=['POST'])
def insert_complete():
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))
        if document_handler(dict_body) == False:
            return Response("Invalid JSON base for document, check if all camps are in the object", status=400)
    
        insert_one(dict_body)  
    except Exception as e:
        print(e)
        return Response("Invalid JSON base for document, check the structure or if the indexes are all strings", status=400)

    return "OK"



app.run()