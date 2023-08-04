from classe import User

pessoa = User("davi", "1234", "luisdavi@gmail.com", "9991320392309")

print(pessoa.get_username())

pessoa.alter_username("Luis")

print(pessoa.get_username())
pessoa.set_teste("AAA")
print(pessoa.get_teste)