# faça um programa que leia 20 numeros inteiros
#  e armazene em uma lista. Armazene os numeros
# pares na lista par e os numeros Impares na
# lista impar. improma as tres listas

lista = []
lista_par = []
lista_impar = []
for i in range(20):
    n = int(input('Digite um numero: '))
    lista.append(n)
    lista_par.append(n) if n % 2 == 0 else lista_par.append(n)
    
print("Todos os numeros:", lista)

print("Numeros Pares: ", lista_par)

print("Numeros Impares", lista_impar)
