class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides):
        self.__sides = sides
        self.__color = color
        self.filed = bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
                return False
            else:
                return True

    def set_color(self, r, g, b):
        if Figure.__is_valid_color(self, r, g, b):
            self.__color = [r, g, b]
        else:
            return self.__color

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        self.__is_valid_sides(*self.__sides)
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def __len__(self):
        P = 0
        for j in self.__sides:
            P += j
            return P


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], *sides):
        if isinstance(sides[0], (int, float)) and sides[0] > 0 and len(sides) == 1:
            new_sides = sides
        else:
            new_sides = [1] * self.sides_count
        super().__init__(color, *new_sides)
        self.__sides = new_sides[0]

    def get_square(self):
        c = self.get_sides()[0]
        __radius = c / 2 * 3.14
        return 3.14 * __radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *sides):
        if isinstance(sides[0], (int, float)) and sides[0] > 0 and len(sides) == 3:
            new_sides = sides
        else:
            new_sides = [1] * self.sides_count
        self.__sides = sides
        super().__init__(color, *new_sides)

    def get_square(self):
        a = int(self.get_sides()[0])
        b = int(self.get_sides()[1])
        c = int(self.get_sides()[2])
        p = 1 / 2 * (a + b + c)
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return S


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], *sides):
        if isinstance(sides[0], (int, float)) and sides[0] > 0 and len(sides) == 1:
            new_sides = sides * self.sides_count
        else:
            new_sides = [1] * self.sides_count
        super().__init__(color, *new_sides)
        self.__sides = new_sides[0]

    def get_volume(self):
        a = self.get_sides()[0]
        return a ** 3


print(Circle.mro())
circle1 = Circle((200, 200, 100), 10)
print(circle1.get_sides())

circle1.set_color(55, 66, 77)
print(circle1.get_color())
print(circle1.get_square())
circle1.set_sides(15)
print(circle1.get_sides())
print(circle1.get_square())
print(len(circle1))

triangle1 = Triangle((200, 200, 100), 10, 15, 20)
print(triangle1.get_sides())
print(triangle1.get_square())
triangle1.set_sides(15, 1, 33)
print(triangle1.get_sides())
print(triangle1.get_square())
print(triangle1.get_color())
triangle1.set_color(115, 30, 300)
print(triangle1.get_color())

cube1 = Cube((222, 35, 130), 6)
print(cube1.get_color())
cube1.set_color(30, 70, 15)
print(cube1.get_color())
print(cube1.get_volume())
print(cube1.get_sides())
cube1.set_sides(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
print(cube1.get_sides())
print(cube1.get_volume())
