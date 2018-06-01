# -*- coding: utf-8 -*-

"""
Diversas formas de abrir um arquivo:

i) arq = open("dados.txt", "r"), r indica read modo de leitura, arquivo tem que existir
ii) arq = open("dados.txt", "w"), w indica writ, modo de escrita, se arquivo não existir criar
iii) arq = open("dados.txt", "r+"), r+ modo de leitura e escrita, arquivo tem que existir, ponteiro e colocado no começo do arquivo
    você tem que movimentar o ponteiro com seek(), senão nao sai do lugar
iv) arq = open("dados.txt", "rb+"), rb+, modo de leitura, arquivo tipo binário, pnteiro é colocado no inicio do arquivo
    voce tem que movimentar o ponteiro com seek(), senão não sai do lugar

v) arq = open("dados.txt", "rb") rb, modo de leitura, arquivo tipo binário, é possivel ler tudo]
vi) arq = open("dados.txt", "wb")wb, modo de escrita, arquivo binário
vii) arq = open("dados.txt", "a") a, modo de escrita, adiciona dados ao final, não apaga os dados já existentes
ix) arq = open("dados.txt", "ab") ab, modo de escrita, tipo binário,adiciona dados ao final, não apaga os dados já existentes

Siglas de todos os modos de abertura de arquivos

r - read
w - write
a - append

rb, r+, rb+, wb, w+, wb+, a, ab, a+, ab+

"""

# dicas sobre arquivos: http://www.bosontreinamentos.com.br/programacao-em-python/leitura-e-gravacao-em-arquivos-com-python/

#não é possivel abrir um arquivo para leitura read(r) se este não tiver sido criado, não é possivel fazer:
#arq = ope("arquivo.txt", "r")

# abrindo arquivo no modo escrita. Se não existir cria o arquivo, se já existir Apaga tudo que tiver e escreve por cima
arq = open("dados.txt", "w")

arq.write("ola")
arq.write("\n tudo bem")
arq.close()

arq = open("dados.txt", "r")
dados = arq.readline()
print(dados)
#print(type(dados))
arq.close()

# abrindo arquivo no modo escrita com preservação. Se não exisitir cria o arquivo, se já existir adiciona os dados no final do arquivo
arq = open("dados2.txt", "a")
arq.write("\n ola mundo")
arq.close()

# abrindo arquivo dataset.txt
with open("dataset.txt", "r") as arq:
    lista = arq.read().splitlines()

print(lista)
print(len(lista))

print(lista[:2])