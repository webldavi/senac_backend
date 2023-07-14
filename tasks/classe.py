# class Ball:
#     def __init__(self, color, radius, material):
#         self.color = color
#         self.radius = radius
#         self.material = material

#     def switch_color(self, color):
#         self.color = color

#     def get_color(self):
#         return self.color


# bola = Ball("red", 15, "borracha")
# print(bola.get_color())
# bola.switch_color("Blue")
# print(bola.get_color())


# class Square:
#     def __init__(self, width):
#         self.width = width

#     def switch_width(self, width):
#         self.width = width

#     def get_width(self):
#         return self.width

#     def area(self):
#         return self.width ** 2


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def switch_side_a(self, side_a):
        self.side_a = side_a

    def switch_side_b(self, side_b):
        self.side_b = side_b

    def get_side_a(self):
        return self.side_a

    def get_side_b(self):
        return self.side_b

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return self.side_a * 2 + self.side_b * 2


# Programa principal
side_a = int(input("Tamanho do lado A: "))
side_b = int(input("Tamanho do lado B: "))

rectangle = Rectangle(side_a, side_b)

area = rectangle.area()

perimeter = rectangle.perimeter()


print("\n")
print(f"Área: {area}")

print(f"Perímetro: {perimeter}")

print(f"Quantidade de pisos que medem 1 metro: {area}")

print(f"Quantidade de rodapés que medem 2 metro: {perimeter}")
