# -*- coding: utf-8 -*-

def opcao(op):
    if op == 1:
        escrever()
    elif op == 2:
        ler()
    else:
        print("\n\n Nenhuma opção escolhida")

def escrever():
    dados = input("\n\n Digite a entrada >> ")
    with open("saida.txt", "a") as arq:
        arq.write(dados)
        arq.close()

def ler():
    with open("saida.txt", "r") as arq:
        dados = arq.read()
        arq.close()
    print(dados)


op = input("\n\n Digite 1 para escrever ou 2 para ler >> ")
op = int(op)

opcao(op)