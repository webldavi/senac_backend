# construa um código que receba tres numeros
# e calcule a média aritiética entre eles
numero_1 = float(input("Digite o numero 1: "))
numero_2 = float(input("Digite o numero 2: "))
numero_3 = float(input("Digite o numero 3: "))


def media():
    return (numero_1 + numero_2 + numero_3) / 3

print(f"A média dos numeros é {media()}")

