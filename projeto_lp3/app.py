# importa a classe flask do modulo flask
import json
from flask import Flask, render_template, request
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
    
    with open('projeto_lp3/lojas.json', 'r', encoding='utf8') as arquivo:
        lista_lojas = json.load(arquivo)

        lojas_ZN = [loja for loja in lista_lojas if loja['zona'].lower() == 'zona norte']
        lojas_ZL = [loja for loja in lista_lojas if loja['zona'].lower() == 'zona leste']
        lojas_ZS = [loja for loja in lista_lojas if loja['zona'].lower() == 'zona sul']
        lojas_ZO = [loja for loja in lista_lojas if loja['zona'].lower() == 'zona oeste']
        lojas_C = [loja for loja in lista_lojas if loja['zona'].lower() == 'centro']

        return render_template('contatos.html', lojas_ZL = lojas_ZL, lojas_ZN = lojas_ZN, lojas_ZO = lojas_ZO, lojas_ZS = lojas_ZS, lojas_C= lojas_C)

# página de produtos - /produtos
# lista_produtos = [
#         {'nome': 'coca cola', 'descricao': 'bebida'},
#         {'nome': 'chips', 'descricao': 'saguadinho'},
#         {'nome': 'bubalu', 'descricao': 'chicletchy'}
#     ]

@app.route("/produtos")
def produtos(): 

    # o contexto serviria para trazer dados de fora (tipo bdd)
    # lista onde cada produto é um dicionário
    # lista_produtos = [
    #     {'nome': 'coca cola', 'descricao': 'bebida'},
    #     {'nome': 'chips', 'descricao': 'saguadinho'},
    #     {'nome': 'bubalu', 'descricao': 'chicletchy'}
    # ]
    # return render_template('produtos.html', produtos=lista_produtos)

    with open('projeto_lp3/produtos.json', 'r', encoding='utf8') as arquivo:
        lista_produtos = json.load(arquivo)
        produtos = [{**produto, 'preco': format(produto['preco'], '.2f')} for produto in lista_produtos]

        # dá um nome pra acessar no html
        return render_template('produtos.html', produtos=produtos)

@app.route("/entre-em-contato")
def entre_em_contato():
    return render_template('entre-em-contato.html')


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

@app.route("/politica_privacidade")
def politica_privacidade():

    return render_template('politica-privacidade.html')

@app.route("/termos_uso")
def termos_uso():

    return render_template('termos-uso.html')

@app.route("/como_utilizar")
def como_utilizar():

    return render_template('como-utilizar.html')

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template('cadastro-produto.html')

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    # descricao = request.form['descricao']
    marca = request.form['marca']
    categoria = request.form['categoria']
    preco = float(request.form['preco'])
    estoque =  int(request.form['estoque'])
    # produto = {'nome': nome, 'descricao':descricao}
    
    with open('projeto_lp3/produtos.json', 'r', encoding='utf8') as arquivo:
        
        lista_produtos = json.loads(arquivo.read())
        novo_produto = {'id': lista_produtos[-1]['id']+1,'nome': nome, 'marca':marca, 'categoria': categoria, 'preco':preco, 'estoque': estoque}

        lista_produtos.append(novo_produto)
    
    with open('projeto_lp3/produtos.json', 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(lista_produtos, indent=2))

    with open('projeto_lp3/produtos.json', 'r', encoding='utf8') as arquivo:
        produtos = [{**produto, 'preco': format(produto['preco'], '.2f')} for produto in lista_produtos]
        return render_template('produtos.html', produtos=produtos)


# rodar direto por aqui
app.run()