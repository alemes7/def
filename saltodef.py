import os

não = "n"
sim = "y"
s = 0
sair = 0
atletas = []

#/////////////////////////////////////////////////////////////////////////////////////////////////////

def Registrar():
        nome = input("Nome do atleta: ")
        saltos = []
        for i in range(5):
            salto = float(input(f"Digite o valor do salto {i+1}: "))
            saltos.append(salto)
            atletas[nome] = saltos
            print("Registro concluído.")

#/////////////////////////////////////////////////////////////////////////////////////////////////////

def Alterar():
        nome = input("Nome do atleta: ")
        if nome in atletas:
            saltos = atletas[nome]
            print(f"Saltos registrados: {saltos}")
            num_salto = int(input("Digite o número do salto que deseja alterar (1 a 5): "))
            if 1 <= num_salto <= 5:
                novo_salto = float(input("Digite o novo valor do salto: "))
                saltos[num_salto-1] = novo_salto
                atletas[nome] = saltos
                print("Alteração concluída.")
            else:
                    print("Número de salto inválido.")
        else:
                print("Atleta não registrado.")

#/////////////////////////////////////////////////////////////////////////////////////////////////////

def Listar():
        if len(atletas) == 0:
            print("Nenhum atleta registrado.")
        else:
            print("Médias dos atletas:")
            for nome, saltos in atletas.items():
                media = sum(saltos) / 5
                print(f"{nome}: {media:.2f}")

#/////////////////////////////////////////////////////////////////////////////////////////////////////

def sair():
        print("Você realmente deseja sair?")
        print("Sim [y] \nNão [n]")
        ç = input("")

        if ç == "n":
                s = 0
        elif ç == "y":
                s = 1
        else:
            print("Opção invalida")
            sair

        
#/////////////////////////////////////////////////////////////////////////////////////////////////////

op = int(input("Informe o valor desejado \n 1 - Registrar \n 2 - Alterar \n 3 - Listar \n 4 - Sair"))



if op == 1:
    Registrar
elif op == 2:
    Alterar
elif op == 3:
    Listar
elif op == 4:
    sair
else:
    print("Opção invalida")

     
os.system("pause")
