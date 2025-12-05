from flask import Flask
app = Flask(__name__)

@app.get("/hello")
def hello():
    return {"msg": "Hello from DevOps Pipeline!"}
