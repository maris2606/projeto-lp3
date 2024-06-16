# importa a classe flask do modulo flask
from flask import Flask, render_template

from validate_docbr import CPF, CNPJ

# java
# Aluno aluno = new Aluno();

# python
# a1 = Aluno()

# instancia o objeto flask que representa a aplicação
app = Flask("minha aplicação")


# rota + função
# rota: definição de um padrao de url
# função: função python com um retorno

# página home - /
# "'app', toda vez que a rota for '/', execute home"
@app.route("/") # @ decorator -> uma notação pra função home
def home():
    return render_template('home.html')

# página contatos - /contatos
@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

# página de produtos - /produtos
@app.route("/produtos")
def produtos(): 

    # o contexto serviria para trazer dados de fora (tipo bdd)

    # lista onde cada produto é um dicionário
    lista_produtos = [
        {'nome': 'coca cola', 'descricao': 'bebida'},
        {'nome': 'chips', 'descricao': 'saguadinho'},
        {'nome': 'bubalu', 'descricao': 'chicletchy'}
    ]
    # dá um nome pra acessar no html
    return render_template('produtos.html', produtos=lista_produtos)




@app.route("/servicos")
def servicos(): 
    return render_template('servicos.html')


@app.route("/gerar-cpf")
def cpf(): 
    cpf = CPF()
    return render_template('gerar-cpf.html', cpf_gerado = cpf.generate(True))

@app.route("/gerar-cnpj")
def cnpj(): 
    cnpj = CNPJ()
    return render_template('gerar-cnpj.html', cnpj_gerado = cnpj.generate(True))