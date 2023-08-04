class teste:
    test = 1

class teste2(teste):
    def imprimir(self):
        print(self.test)

aaa = teste2()
aaa.imprimir()