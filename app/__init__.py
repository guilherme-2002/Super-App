import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth

# Configuração do log da aplicação
logging.basicConfig(format='%(asctime)s - %(message)s', filename="log/app.log", level=logging.INFO)
log = logging.getLogger()

# Inicialização da aplicação Flask
app = Flask(__name__, instance_relative_config=True)

# Carregando configurações a partir de 'cfg/app.cfg'
app.config.from_pyfile('../cfg/app.cfg', silent=True)
app.config['FLASK_SECRET'] = app.config.get('SECRET_KEY')
app.config['BASIC_AUTH_FORCE'] = True
app.secret_key = app.config.get('SECRET_KEY')

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando extensões
db = SQLAlchemy(app)
migrate = Migrate(app, db)
auth = HTTPBasicAuth()

# Importando outros módulos após a inicialização do app e db
from app import models, views, admin, auth 