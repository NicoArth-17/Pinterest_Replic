# Arquivo para estrutura do Banco de Dados

from __init__ import database
from datetime import datetime

# Criando classes/objetos que serão as tabelas no arquivo SQL
# OS atributos serão colunas

class Usuario(database.Model):
    # Dentro dos parênteses estão as regras para definir o tipo de info que a coluna vai receber
    id = database.Column(database.Integer, primary_key=True)
    # database.Integer -> tem que ser um numero inteiro
    # primary_key=True -> chave primária (reconhece a informação como única)
    username = database.Column(database.String, nullable=False)
    # database.String -> tem q ser uma string
    # nullable=False -> não pode ser nulo
    email = database.Column(database.String, nullable=False, unique=True)
    # unique=True -> email não poder ser igual outro
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship('Foto', backref='usuario', lazy=True)
    # .relationship('nome da classe que vai se relacionar', backref='usuario', lazy=True) -> diz que este atributo vai ser uma relação entre a tabela de Usuario e a tabela de Foto (não é ma coluna)
    # backref= -> faz uma relação inversa
    # lazy=True -> otimizar a busca no banco de dados


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    img = database.Column(database.String, default='default.png')
    # default= -> diz oque vai aparecer por padrão caso a info não seja inserida
    data_criaçao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_user = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    # database.ForeignKey('classe.atributo') -> Chave Estrangeira: pega o valor de um atributo de outra classe
    # obs: em 'classe.atributo' se escreve tudo minúsculo, mesmo que o nome da class esteja iniciando com letra maiúscula
