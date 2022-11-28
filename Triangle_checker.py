class TriangleChecker:
    def __init__(self, a, b, c) -> None:
        self.sides = (a, b, c)

    
    def is_triangle(self):
        if any([type(x) not in (int, float) for x in self.sides]) or any([x <= 0 for x in self.sides]):
            return 1
        elif sorted(self.sides)[2] >= sorted(self.sides)[0] + sorted(self.sides)[1]:
            return 2
        else:
            return 3


a, b, c = '3', 4, 5
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


        
