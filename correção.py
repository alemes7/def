import os

s = 0
competidores = {}

def menu(x):
    if x == 1:
        registrar()
        s = 0
    elif x == 2:
        alterar()
        s = 0
    elif x == 3:
        listar()
        s = 0
    elif x == 4:
        s = 1
    else:
        print("Opção invalida")
        s = 0

    return s
#/////////////////////////////////////////////////////////////////////////////////////////
def registrar():
    os.system("cls")
    nome = input("Digite o nome do competidor:")
    val = []
    for num in range(5):
        num = float(input("Digite a distancia do salto: "))
        val.append(num)
    competidores[nome] = val #para colocar na lista
    os.system("cls")
#/////////////////////////////////////////////////////////////////////////////////////////
def alterar():
    os.system("cls")
    nome = input("Digite o nome do competidor: ")
    if nome in competidores:
        t = len(competidores[nome])#len é utilizado para obter o numero de itens *de uma lista
        print(f"Digite qual dos {t} valores da lista deseja alterar")
        print(f"Saltos registrados: {competidores}")
        p = int(input(""))
        competidores[nome][p-1] = float(input("Digite qual o novo valor da entrada: "))
    else:
        print("Competidor não encontrado")
        os.system("cls")
#/////////////////////////////////////////////////////////////////////////////////////////
def listar():
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
    os.system("pause")
#/////////////////////////////////////////////////////////////////////////////////////////

while s == 0:
    op = int(input("Boas-vindas!\n[1] Registrar \n[2] Alterar \n[3] Listar \n[4] Sair \nInforme o que você deseja:"))
    s = menu(op)
    print(s)