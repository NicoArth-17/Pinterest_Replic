# Arquivo para criar a aplicação/site

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Criar banco de dados

app = Flask(__name__)

# Configurando banco de dados sqlite junto ao 'app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
# app.config['variável do banco de dados'] 
# 'sqlite:///comunidade.db' -> cria uma pasta 'instance' com um arquivo sqlite 'comunidade.db' em branco 
# executado no arquivo "criar-banco-dados.py"

# Criando df para o banco de dados
database = SQLAlchemy(app)

import routes