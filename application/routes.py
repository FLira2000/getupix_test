from flask import Flask, request

app = Flask("owid_covid")

@app.route("/", methods=["GET"])
def index():
    return {"Flask": "Just Flask"}

app.run()