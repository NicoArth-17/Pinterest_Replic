from flask import Flask, render_template, url_for

# A biblioteca do flask recomenda iniciar com está variável 'app'
app = Flask(__name__)

# Colocando no servidor local, o site no ar (link de acessso ao site no terminal após rodar 'app.run()')
@app.route('/')
# @app.route('/') -> diz o que vai aparecer após o link/route(rota) do site, seguido de uma function representando à que página do site que está associada route/link  (ex.: HomePage)
def homepage():
    return render_template('home.html')
    # render_template -> busca no local deste arquivo uma pasta demoninada 'templates' para usar arquivos(no caso o html) dentro dela
    # Criação de um arquivo HMTL para fazer a página

# O nome dentro de '< >' se torna uma variável, definida ao escrever na url
@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

if __name__ == '__main__':
# # if __name__ == '__nome do arquivo__': -> significa que o código inserido a baixo deverá ser executado neste arquivo, e quando este arquivo for importado em outro, o código a seguir não será executado

    # Rodar aplicação/site
    app.run(debug=True)
    # app.run() -> sobe o site para o ar
    # debug=True -> todas as alterações feitas na aplicação, já serão implementadas no site
