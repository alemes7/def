import os

def registro(competidores):
    nome = input("Digite o nome do competidor: ")
    t = int(input("Digite quantos saltos o competidor deu: ")) #t vira a quantidade de saltos (qualquer valor)
    val = []
    for num in range(t):
        num = float(input("Digite a distancia do salto: "))
        val.append(num)
    competidores[nome] = val #para colocar na lista

    #//////////////////////////////////////////////////////////////////////////////////////////

def alterar(competidores):
    nome = input("Digite o nome do competidor: ")
    if nome in competidores:
        t = len(competidores[nome])#len é utilizado para obter o numero de itens *de uma lista
        print(f"Digite qual dos {t} valores da lista deseja alterar")
        print(f"Saltos registrados: {competidores}")
        p = int(input(""))
        competidores[nome][p-1] = float(input("Digite qual o novo valor da entrada: "))
    else:
        print("Competidor não encontrado")
    

#//////////////////////////////////////////////////////////////////////////////////////////////////////

def listar(competidores):
    if not competidores:
        print("Você ainda não cadastrou nenhum usuário")
    else:
        for nome, saltos in competidores.items():
            soma_saltos = 0
            qtd_saltos = 0
            for salto in saltos:
                soma_saltos += salto
                qtd_saltos += 1
            media = soma_saltos / qtd_saltos
            print(f"{nome}: {saltos}, Média: {media:.2f}")

def competicao():
    z = "N"
    competidores = {} 

    while z != "S":
        print("Selecione uma opção dentre as seguintes \n 1- Registro \n 2- Alterar \n 3- Listar \n 4- Sair")
        s = int(input("Digite a opção que deseja: "))

        if s == 1:
            os.system("cls")
            registro(competidores)
            os.system("cls")

        elif s == 2:
            os.system("cls")
            alterar(competidores)
            os.system("cls")

        elif s == 3:
            os.system("cls")
            listar(competidores)
            os.system("pause")

        elif s == 4:
            z = "S"
        else:
            print("Esta opção não está na lista")

competicao()