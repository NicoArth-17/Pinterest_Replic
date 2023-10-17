# Arquvio para executar a aplicação/site

from __init__ import app

if __name__ == '__main__':
# # if __name__ == '__nome do arquivo__': -> significa que o código inserido a baixo deverá ser executado neste arquivo, e quando este arquivo for importado em outro, o código a seguir não será executado

    # Rodar aplicação/site
    app.run(debug=True)
    # app.run() -> sobe o site para o ar
    # debug=True -> todas as alterações feitas na aplicação, já serão implementadas no site
