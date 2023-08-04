class Forma:
    def __init__(self):
        self.area = float


    def get_area(self):
        return 0

class Retangulo(Forma):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height


    def calcArea(self):
        return self.base * self.height
    
    def __str__(self) -> str:
        return f"\033[1;36m Sua forma: \033[0;32m Retangulo \033[1;36m sua Area: \033[0;32m {self.calcArea()} \033[0;0m"



retangulo = Retangulo(5, 2)

print(retangulo)