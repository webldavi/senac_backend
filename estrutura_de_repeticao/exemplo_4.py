#crie um programa que leia um numero e gere a tabuada desse numero de 1 a 10
number = int(input("Qual numero vc deseja ver a tabuada: "))
if number >=1 and number<=10:
    for n in range(10):
        print(f"{number} x {n+1} ==> {number * (n+1)}")