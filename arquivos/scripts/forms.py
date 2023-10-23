# Arrquivo para formulários

from flask_wtf import FlaskForm # estrutura que permitirá a criação dos forms
from wtforms import StringField, PasswordField, SubmitField # importar os campos que serão usados
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError # Validação de campos: campo obrigatótio, email, se um campo está igual a outro, quantidade de caracteres, mensagem de erro
from models import Usuario

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) # tipo_do_campo('label do campo')
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao = SubmitField('Entrar', validators=[ValidationError()])


class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8,16)])
    confirmaçao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao = SubmitField('Cadastrar', validators=[ValidationError()])

    # Function para validação de campo no form, deve ter nome digitado da seguinte forma: validate_NomeDoCampo()
    # Esse formato se dá pois usaremos uma função no arquivo de rotas que chamará todos os métodos de validação de campo ao clicar no botão submit
    def validate_email(self, email):
        user_email = Usuario.query.filter_by(email=email.data).first()
        # .query -> faz uma requisição de informção
        # .filter_by(NomeDaColunaNaClassUsuario = CampoQueSeráVerificado.data) -> filtra os valores encontrados e retorna em uma lista
        # campo -> retorna o campo | campo.data -> retorna a informação presente no campo
        # .first() -> pega o primeiro valor encontrado

        if user_email: # se já existir cadastrado, aparecer mensagem de erro
            return ValidationError('Email já cadastrado')