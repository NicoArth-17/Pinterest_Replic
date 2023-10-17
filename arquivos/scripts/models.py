# Arquivo para estrutura do Banco de Dados

from __init__ import database

# Criando classes/objetos que serão as tabelas no arquivo SQL
# OS atributos serão colunas

class Usuario(database.Model):
    id = database.Column()
    username = database.Column()
    email = database.Column()
    senha = database.Column()
    fotos = database.relationship()
    # .relationship() -> diz que este atributo vai ser uma relação entre a tabela de Usuario e a tabela de Foto


class Foto(database.Model):
    id = database.Column()
    img = database.Column()
    data_criaçao = database.Column()
    id_user = database.Column()
