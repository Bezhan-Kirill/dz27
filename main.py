# class Figure:
#     def __init__(self, side1, side2, radius, h):
#         self.side1 = side1
#         self.side2 = side2
#         self.radius = radius
#         self.h = h
#     def area(self):
#         pass
#
# class Rectangle(Figure):
#     def area(self):
#         return self.side1 * self.side2
#
# class Round(Figure):
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
# class Right_triangle(Figure):
#     def area(self):
#         return (self.side1 * self.side2) / 2
#
# class Trapeze(Figure):
#     def square(self):
#         return self.side1 * self.side2 / 2 * self.h

class Figure:
    def __init__(self, side1, side2, radius, h):
        self.side1 = side1
        self.side2 = side2
        self.radius = radius
        self.h = h
    def area(self):
        pass

class Rectangle(Figure):
    def __str__(self):
        return f"Прямоугольник, сторона 1 = {self.side1} сторона 2 = {self.side2}"
    def __int__(self):
        return f"Площадь = {self.side1 * self.side2}"

class Round(Figure):
    def __str__(self):
        return f"Круг, радиус = {self.radius}"
    def __int__(self):
        return f"Площадь = {3.14 * (self.radius ** 2)}"

class Right_triangle(Figure):
    def __str__(self):
        return f"Прямоугольный треугольник катет 1 = {self.side1} катет 2 = {self.side2}"
    def __int__(self):
        return f"Площадь = {(self.side1 * self.side2) / 2}"

class Trapeze(Figure):
    def __str__(self):
        return f"Трапеция сторона 1 = {self.side1} сторона 2 = {self.side2} высота = {self.h}"
    def __int__(self):
        return f"Площадь = {self.side1 * self.side2 / 2 * self.h}"


figure1 = Round(side1 = None, side2 = None, radius = 4, h = None)
figure2 = Rectangle(side1 = 3, side2 = 5, radius = None, h = None)
figure3 = Right_triangle(side1 = 4, side2 = 4, radius = None, h = None)
figure4 = Trapeze(side1 = 5, side2 = 8, radius = None, h = 4)


print(figure1.__str__())
print(figure1.__int__())

print(figure2.__str__())
print(figure2.__int__())

print(figure3.__str__())
print(figure3.__int__())

print(figure4.__str__())
print(figure4.__int__())

