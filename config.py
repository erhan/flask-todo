import os

class DefaultConfig(object):
    def __init__(self):
        self.DEBUG = True
        self.SQLALCHEMY_DATABASE_URI = 'postgresql://@localhost/flask_todo'
        self.DATABASE_CONNECT_OPTIONS = {}
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SECRET_KEY = "flask-todo"
        self.SERVER_NAME = "0.0.0.0:5001"


class ProductionConfig(DefaultConfig):
    def __init__(self):
        super(ProductionConfig, self).__init__()
        self.DEBUG = False
        self.SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        self.SERVER_NAME = "flask-todo-ornek.herokuapp.com"


ENV = os.getenv('ENVIRONMENT', 'Local')
configuration = DefaultConfig()
if ENV == "Production":
    configuration = ProductionConfig()