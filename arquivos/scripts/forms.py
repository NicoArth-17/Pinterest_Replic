# Arquivo para formulários

from flask_wtf import FlaskForm # estrutura que permitirá a criação dos forms
from wtforms import StringField, PasswordField, SubmitField, FileField # importar os campos que serão usados
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError # Validação de campos respectivamente: campo obrigatótio, email, se um campo está igual a outro, quantidade de caracteres, mensagem de erro
from models import Usuario

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) # tipo_do_campo('label do campo', validators=ListaDeValidadores)
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao = SubmitField('Entrar')


class FormCadastrar(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8,16)])
    confirmaçao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    # EqualTo('NomeDoCampo/Atributo que deve ser igual')
    botao = SubmitField('Cadastrar')

    # Já que no arquivo models.py definimos o campo de email como uma imnformação unique, criaremos uma validação para esse info realmente ser única 
    # Function para validação de campo no form, deve ter nome digitado da seguinte forma: validate_NomeDoCampo/Atributo()
    # Esse formato se dá pois usaremos uma função no arquivo de rotas que chamará todos os métodos de validação de campo ao clicar no botão submit
    def validate_email(self, email):
        user_email = Usuario.query.filter_by(email=email.data).first()
        # .query -> faz uma requisição de informção
        # .filter_by(NomeDoCampo/Atributo que será verificado = Valor do NomeDoCampo/Atributo que será verificado) -> filtra os valores encontrados e retorna em uma lista
        # campo -> retorna o campo | campo.data -> retorna a informação presente no campo
        # .first() -> pega o primeiro valor encontrado

        if user_email: # se já existir este email cadastrado, aparecerá uma mensagem de erro
            return ValidationError('Email já cadastrado')
        
class FormPost(FlaskForm):
    post = FileField('Foto', validators=[DataRequired()])
    botao = SubmitField('Enviar')
