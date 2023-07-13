# faça um programa que leia tres numeros


contador = 1
maior = 0

while contador <= 5:
    contador += 1
    number = int(input("Digite um numero: "))
    if number > maior:
        maior = number
print(maior)
