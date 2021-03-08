from flask import Flask, request, Response
import flask_caching 
from remote import find_one, insert_one, delete, find_population, find_custom
from data_preparation import document_handler
import json
from functools import reduce
cache = flask_caching.Cache()

app = Flask("owid_covid")
app.config['CACHE_TYPE'] = 'simple' # nunca usei algo diferente, sendo sincero
cache.init_app(app)

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
@cache.cached(timeout=10)
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

# deleta um documento, baseado numa pesquisa
# precisei colocar um _ no nome, fiquei 5 minutos olhando e me pergutando o pq o flask se recusava a executar o /delete
@app.route("/delete", methods=['DELETE'])
def del_ete():
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))
        deleted = delete(dict_body)
    except Exception as e:
        print(e)
        return Response("Invalid JSON, please check the structure or if all indexes as strings", status=400)

    return {"Deleted count": deleted.deleted_count}

# procura e retorna o primeiro documento que contém a população específicada
# utilizei codigo python no lugar de aggregate, não sou mt bom com aggregation
@app.route("/find_population", methods=['GET'])
@cache.cached(timeout=120)##2 minutos de cache talvez seja mais do que suficiente até, mas deixa ai
def find_by_population():
    returnable = None
    try:
        body = request.get_json()
        dict_body = json.loads(json.dumps(body))
        
        if 'population' not in dict_body.keys() or len(dict_body.keys()) > 1:
            raise AttributeError

        returnable = find_population(dict_body['population'])
    except:
        return Response("Invalid JSON. Check if the JSON contains only the population key/value.", status=400)
    
    if returnable != None:
        del(returnable['_id'])
    else:
        return Response("Could not find any document with those population quantity", status=404)
    return returnable

# procura por um document que contenha os parametros especificados no teste
# location, iso code e data
# novamente preferi codigo python a aggregation, perdoe-me voce que está lendo
# mas nao uso mongo ha mt tempo e nao tenho tempo para ler todas as funcoes do aggreg novamente
@app.route("/search_custom", methods=['GET'])
@cache.cached(timeout=120)
def search_custom():
    returnable = 0
    
    body = request.get_json()
    dict_body = json.loads(json.dumps(body))
    expected_camps = ['iso_code', 'location', 'date']

    #perdao por isso, é pra contar a quantidade de atributos existentes que dão match com o document.
    # se der 3, tem o que é necessário.
    cnt = reduce(lambda a, b: a+b, [(lambda p: int(p in list(dict_body.keys())))(x) for x in expected_camps])
    if cnt != 3:
        raise AttributeError

    returnable = find_custom(dict_body)

    if returnable == 0:
        return Response("Could not find any document with those information", status=404)

    returnable = {"Ammount": returnable }

    return returnable


#aplicação rodando
app.run()