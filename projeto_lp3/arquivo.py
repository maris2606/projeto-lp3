# tem arquivo e quer trazer os dados para a memória e
# transformar pro python

# ler arquivo - read
# com o caminho do arquivo
# arquivo = open("projeto_lp3/dados.txt") # retorna objeto TextIOWrapper

# carrega os dados do arquivo em memória

# só lê uma vez, se rodar mais uma vez não vai ter mais conteúdo para ler
# print(arquivo.read()) 

# le todo o conteudo do arquivo em memoria

# conteudo = arquivo.read()
# print(conteudo)
# print(conteudo.upper())

# lembrando que, quando carrega muito arquivo pesado, não pode deixar
# aberto direto
# arquivo.close()

# essa não é muito a forma usual

# usa-se bloco with, que fecha automaticamente ao sair do escopo
# só tem acesso dentro do bloco

with open('projeto_lp3/dados.txt', 'r') as arquivo:
    # conteudo = arquivo.read()
    # print(conteudo)

    linhas = arquivo.readlines()
    # retorna lista com linhas
    print(linhas)
    # ['joao\n', 'jossana\n', 'millena\n', 'marisa']
    # as vezes é mais fácil só usar for

with open('projeto_lp3/dados.txt', 'r') as arquivo:
    linhas = []
    
    # 'in' utilizavel nos iteráveis, considera as linhas
    for linha in arquivo: 
        linhas.append(linha.strip()) # remove o \n e espaços

    print(linhas)

# tipo de leitura
# r - read - modo de leitura - não omitir
# w - write - substitui todo o conteudo
# a - append - escreve ao final

with open('projeto_lp3/dados.txt', 'a') as arquivo:
    arquivo.write('\njaca')
    # quando tem pass, ele não fecha

    # em arquivo geralmente não apaga
    # só marca como inativo, por ex.
    # apagar é meio trabalhoso


with open('projeto_lp3/dados.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(linhas)

# ----------------------------------------------------

with open('projeto_lp3/produtos.csv', 'r') as arquivo:
    # comma separated values
    # cada coluna representa um atributo do produto
    # cada linha é um elemento

    # um arquivo pra cada tabela
    