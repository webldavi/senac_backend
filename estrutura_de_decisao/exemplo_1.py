numero_1 = float(input("Digite o numero 1: "))
numero_2 = float(input("Digite o numero 2: "))
numero_3 = float(input("Digite o numero 3: "))


def media():
    return (numero_1 + numero_2 + numero_3) / 3

aprovado = media() >= 60
reprovado = media() < 30

if aprovado:
    print("Você foi aprovado!")
elif reprovado:
    print("Você foi reprovado!")
else:
    print("você está na 4º prova")
