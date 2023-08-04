import time

class Tamagashi:
    __humor = 10
    def __init__(self, nome, idade, fome, saude):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_fome(self, fome):
        self.fome = fome

    def set_saude(self, saude):
        self.saude = saude

    def get_humor(self):
        if self.fome < 5:
            self.__humor = self.fome

        elif self.fome > 5:
            self.__humor = self.saude

        if self.saude < self.fome:
            self.__humor = self.saude

        elif self.saude > self.fome:
            self.__humor = self.fome

        if self.__humor < 5:
            return "▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▓▒▒▓▒▒▒▒\n▒▒▒▒▓▒▒▓▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▓▓▓▓▓▓▓▓▒▒\n▒▓▒▒▒▒▒▒▒▒▓▒"
        elif self.__humor > 5:
            return "▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▓▒▒▓▒▒▒▒\n▒▒▒▒▓▒▒▓▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒\n▒▓▒▒▒▒▒▒▒▒▓▒\n▒▒▓▓▓▓▓▓▓▓▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒"


bichinho = Tamagashi("Zeca", 4, 10, 10)

print(bichinho.get_humor())

print("\n")
print(bichinho.__humor)
bichinho.set_fome(4)

print(bichinho.get_humor())