# Arquivo para criar rotas/links do site

from flask import render_template, url_for
from __init__ import app
from flask_login import login_required # permitir acesso as páginas/routes apenas com o login acessado
from forms import FormLogin, FormCadastrar

# Colocando no servidor local, o site no ar (link de acessso ao site no terminal após rodar 'app.run()')
@app.route('/', methods=['GET', 'POST'])
# @app.route('/') -> diz o que vai aparecer após o link/route(rota) do site, seguido de uma function representando à que página do site que está associada route/link  (ex.: HomePage)
def homepage():
    formlogar = FormLogin()
    return render_template('home.html', formulario=formlogar)
    # render_template -> busca no local deste arquivo uma pasta demoninada 'templates' para usar arquivos(no caso o html) dentro dela
    # Criação de um arquivo HMTL para fazer a página

# Criando uma page para Cadastro, a tela de Login será na homepage
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    formcadastro = FormCadastrar()
    return render_template('cadastrar.html', formulario=formcadastro)

# O nome dentro de '< >' se torna uma variável, definida ao escrever na url
@app.route('/perfil/<usuario>')
@login_required # restringe o acesso se o user estiver logado
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)