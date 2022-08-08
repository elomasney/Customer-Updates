import os
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

mongo = PyMongo(app)
