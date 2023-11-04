# Arquivo apenas para criar o banco de dados.
# Este arquivo pode ser deletado após a criação do sql
# Estes comando poderiam ter sido executados no terminal para não precisar criar outro arquivo

from __init__ import database, app
from models import Usuario, Post # importando tabelas

# Criando um contexto para criar banco de dados (vai criar o SQL a partir do 'app')
with app.app_context():
    # Executando criação do SQL
    database.create_all()