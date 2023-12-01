from flask import Flask , url_for
from flask_pymongo import PyMongo

server = Flask(__name__)
server.config['SECRET_KEY'] = "ACE202334NOVA"
server.config['MONGO_URI'] =  "mongodb+srv://admin:E145AZY1xoXJm9g5@cluster64459.gwh8ffh.mongodb.net/ace_nova?retryWrites=true&w=majority"

# mongodb_client = PyMongo(server)
# db = mongodb_client.db

from .views import views
server.register_blueprint(views, url_prefix="/")