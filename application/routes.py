from flask import Flask, request
from remote import find_one, insert_one

app = Flask("owid_covid")

@app.route("/", methods=["GET"])
def index():
    return {"Flask": "Just Flask"}

@app.route("/insert", methods=['POST'])
def insert():
    body = request.get_json()
    insert_one(body)
    
app.run()