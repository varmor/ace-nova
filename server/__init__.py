from flask import Flask 

server = Flask(__name__)
server.config['SECRET_KEY'] = "THESAILORSOFMENTALPEACE"


from .views import views
server.register_blueprint(views, url_prefix="/")