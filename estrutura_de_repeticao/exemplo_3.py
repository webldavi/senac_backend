bigger_number = 0

for n in range(5):
    current_number = int(input(f"Digite o {n+1}º numero: "))
    if current_number > bigger_number: bigger_number = current_number
print(bigger_number)



