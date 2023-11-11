# Arquivo para criar rotas/links do site

from flask import render_template, url_for, redirect
from __init__ import app, bcrypt, database
from flask_login import login_user, logout_user, login_required, current_user
from forms import FormLogin, FormCadastrar, FormPost
from models import Usuario, Post
import os
from werkzeug.utils import secure_filename # Para evitar salvar arquivos em que o nome possa comprometer o código, com algum caracter especial ou coisa do tipo


# Colocando no servidor local, o site no ar (link de acessso ao site no terminal após rodar 'app.run()')
@app.route('/', methods=['GET', 'POST'])
# @app.route('/') -> diz o que vai aparecer após o link/route(rota) do site, seguido de uma function representando à que página do site que está associada route/link  (ex.: HomePage)
def homepage():

    formlogar = FormLogin()

    # Criando sistema de login de usuário
    if formlogar.validate_on_submit():
        # Buscando se usuário existe a partir do email inserido
        user = Usuario.query.filter_by(email=formlogar.email.data).first()

        # Caso usuário seja encontrado...
        if user:
            # Verificando se a senha inserida é a mesma da senha cadastrada e criptografada
            if bcrypt.check_password_hash(user.senha, formlogar.senha.data):
            # bcrypt.check_password_hash(senha crypt cadastrada, senha inserida no login) -> faz uma comparação

                # Criando login automático
                login_user(user)

                #Redirecionando para page de perfil
                return redirect(url_for('perfil', id_user=user.id))


    return render_template('home.html', formulario=formlogar)
    # render_template -> busca no local deste arquivo uma pasta demoninada 'templates' para usar arquivos(no caso o html) dentro dela
    # Criação de um arquivo HMTL para fazer a página

# Criando uma page para Cadastro, a tela de Login será na homepage
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():

    formcadastro = FormCadastrar()

    # Criando sistema de cadastro de usuário
    if formcadastro.validate_on_submit():
    # .validate_on_submit() -> diz que o botão submit foi clicado e que as validações estão ok

        # Criptografando a senha cadastrada
        crypt_senha = bcrypt.generate_password_hash(formcadastro.senha.data)
        # bcrypt.generate_password_hash(local onde a senha foi inserida) -> gera uma senha criptografada

        user = Usuario(username=formcadastro.username.data, email=formcadastro.email.data, senha=crypt_senha)

        # Armazenando usuários no banco de dados
        database.session.add(user) # adiconando user
        database.session.commit() # comitando alteração

        # Ao finalizar o cadastro, o usuário será redirecionado para a page de perfil. Porém é necessário estar logado para acessar essa rota.

        # Criando login automático
        login_user(user, remember=True)
        # remember=True -> armazena o login nos cookies do navegador, ou seja, caso o usuario feche a janela, quando ela for reaberta o sistema irá lembrar que o user já estava logado

        # Redirecionando o usuário para a tela de perfil após concluir o cadastro
        return redirect(url_for('perfil', id_user=user.id))

    return render_template('cadastrar.html', formulario=formcadastro)

# O nome dentro de '< >' se torna uma variável, definida ao escrever na url.
# Deve ser um informação única do usuário (por exemplo o id).
@app.route('/perfil/<id_user>', methods=['GET', 'POST'])
@login_required # restringe o acesso se o user estiver logado
def perfil(id_user):

    # Verificando se está acessando o próprio perfil
    # E já que estaremos logados no nosso próprio perfil é aqui que carregaremos as fotos
    if int(id_user) == int(current_user.id):
    # current_user -> remete ao usuário logado no momento

        formfoto = FormPost()

        # Checando validação dos campos do formulário ao clicar no botão Submit
        if formfoto.validate_on_submit(): 
            # Selecionando o arquivo do post
            arquivo_post = formfoto.post.data

            # Convertendo o nome do arquivo_post para não gerar nenhum problema
            secure_name = secure_filename(arquivo_post.filename)

            # Escolhendo onde o arquivo ficará armazenado
            armazem_posts = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                          app.config['UPLOAD_FOLDER'],
                                            secure_name)
            # os.path.join() -> caminho de arquivo separado por vírgula ao invés de barra
            # os.path.abspath() -> encontra o caminho a partir do nome de algum arquivo
            # os.path.dirname(__file__) -> encontra o nome deste arquivo
            # app.config['UPLOAD_FOLDER'] -> variável que representa um caminho, criada no arquivo '__init__.py'

            # Salvando arquivo
            arquivo_post.save(armazem_posts)

            # Registrando post no SQL
            post = Post(img=secure_name, id_user=current_user.id) # data_criaçao e id são criados automáticamente, não precisam ser passados nos parâmetros ao criar o objeto
            database.session.add(post)
            database.session.commit()

        return render_template('perfil.html', usuario=current_user, formulario=formfoto)
    
    # Caso esteja acessando um outro perfil
    else:
        # Buscando usuário pelo id
        usuario = Usuario.query.get(int(id_user))
        return render_template('perfil.html', usuario=usuario, formulario=None)

# Criando sistema de Logout do usuário
# Ao clicar no botão 'sair' na página 'perfil.html', o usuário será redirecionado para a rota de logout
# A rota logout apenas executará essa função e após isso irá redirecionar o usuário para a home.html
@app.route('/logout')
@login_required
def logout():
    logout_user() # reconhece qual usuário já está logado e desconecta ele
    return redirect(url_for('homepage'))

@app.route('/feed')
@login_required
def feed(): 
    # Buscado todas as informações na class Post ordenadas pelo atributo 'data_criação'
    imagens = Post.query.order_by(Post.data_criaçao.desc()).all()
    # .desc() -> vem de descending, ou seja, ordem decrescente
    return render_template('feed.html', fotos=imagens)