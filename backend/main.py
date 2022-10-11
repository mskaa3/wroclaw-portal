import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv(dotenv_path="./.env.local")

DEBUG=bool(os.environ.get("DEBUG",True))

app=Flask(__name__)
CORS(app)

app.config["DEBUG"]=DEBUG

@app.route("/")
def hello():
  return "Hello from Wroclaw Portal"

if __name__=="__main__":
  app.run(host="0.0.0.0",port=5000)