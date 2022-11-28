class Cart:
    def __init__(self) -> None:
        self.goods = []


    def add(self, gd):
        self.goods.append(gd)

    
    def remove(self, indx):
        self.goods = self.goods[:indx] + self.goods[indx + 1:]
    

    def get_list(self):
        return [f'{good.name}: {good.price}' for good in self.goods]


class Table:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price




cart = Cart()
cart.add(Table('table1', 123))
cart.add(Table('table2', 124))
cart.add(TV('t1', 200))
cart.add(TV('t2', 201))
cart.add(Notebook('ta3', 320))
cart.add(Notebook('ta4', 321))


#print(cart.get_list())
