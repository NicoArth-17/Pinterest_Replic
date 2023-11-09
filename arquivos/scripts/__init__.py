# Arquivo para criar a aplicação/site

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Criar banco de dados
from flask_login import LoginManager # Gerenciar senhas
from flask_bcrypt import Bcrypt # Criptografar senha

app = Flask(__name__)

# Configurando banco de dados sqlite junto ao 'app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
# app.config['variável do banco de dados'] 
# 'sqlite:///comunidade.db' -> cria uma pasta 'instance' com um arquivo sqlite 'comunidade.db' em branco 
# executado no arquivo "criar-banco-dados.py"

# Chave de segurança
app.config['SECRET_KEY'] = 'c85b5271079061f807ece62a3631e6be'

# Criando um armazenamento das fotos no perfil
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts'

# Criando df para o banco de dados
database = SQLAlchemy(app)

# Criando um login
bcrypt = Bcrypt(app) # Criptográfia
login_manager = LoginManager(app) # Gerenciador
login_manager.login_view = 'homepage' # Para onde o usuario vai ser redirecionado quando não estiver logado

import routes