# Arquivo para estrutura(tabelas) do Banco de Dados

from __init__ import database, login_manager
from datetime import datetime
from flask_login import UserMixin # Class q vai gerenciar o login

# Function necessária para toda criação de login com flask
@login_manager.user_loader # decorator indica que em seguida vem uma functio que carrega e retorna um usuário
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario)) # retorna um usuário específico (pega uma informção na class Usuario)

# Criando classes/objetos que serão as tabelas no arquivo SQL
# OS atributos serão colunas

class Usuario(database.Model, UserMixin):
# database.Model -> permite criar a class de modo à construir uma tabela, ou seja, de forma que o banco de dados vai entender
# User.Mixin -> determina a classe que vai gerenciar a estrutura de login

    # Dentro dos parênteses estão as regras para definir o tipo de info que a coluna vai receber
    id = database.Column(database.Integer, primary_key=True)
    # database.Column -> torna o atributo uma coluna da tabela
    # database.Integer -> tem que ser um numero inteiro
    # primary_key=True -> chave primária (reconhece a informação como única)
    username = database.Column(database.String, nullable=False)
    # database.String -> tem q ser uma string
    # nullable=False -> não pode ser nulo
    email = database.Column(database.String, nullable=False, unique=True)
    # unique=True -> email não poder ser igual outro
    senha = database.Column(database.String, nullable=False)
    posts = database.relationship('Post', backref='usuario', lazy=True)
    # .relationship('nome da classe que vai se relacionar', backref='usuario', lazy=True) -> diz que este atributo vai ser uma relação entre a tabela de Usuario e a tabela de Post (não é ma coluna)
    # backref= -> faz uma relação inversa
    # lazy=True -> otimizar a busca no banco de dados


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    img = database.Column(database.String, default='default.png')
    # default= -> diz oque vai aparecer por padrão caso a info não seja inserida
    # a tabela no banco de dados irá comportar apenas o nome da imagem, já o arquivo será armazenado em uma pasta (neste caso a pasta: arquivos/static/fotos_posts)
    data_criaçao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_user = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    # database.ForeignKey('classe.atributo') -> Chave Estrangeira: pega o valor de um atributo de outra classe
    # obs: em 'classe.atributo' se escreve tudo minúsculo, mesmo que o nome da class esteja iniciando com letra maiúscula
