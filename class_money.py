import random


class Line:
    def __init__(self, x_1, y_1, x_2, y_2) -> None:
        self.sp = (x_1, y_1)
        self.ep = (x_2, y_2)


class Rect:
    def __init__(self, x_1, y_1, x_2, y_2) -> None:
        self.sp = (x_1, y_1)
        self.ep = (x_2, y_2)


class Elipse:
    def __init__(self, x_1, y_1, x_2, y_2) -> None:
        self.sp = (x_1, y_1)
        self.ep = (x_2, y_2)


class_names = [Line, Rect, Elipse]
elements = []

for i in range(217):
    x_1, y_1 = random.random(), random.random()
    x_2, y_2 = random.random(), random.random()
    cl_n = random.choice(class_names)
    if cl_n == Line:
        elements.append(cl_n(0, 0, 0, 0))
    else:
        elements.append(cl_n(x_1, y_1, x_2, y_2))

