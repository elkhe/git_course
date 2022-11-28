class Translator:
    def add(self, eng, rus):
        if 'dct' not in self.__dict__:
            self.dct = {}

        self.dct.setdefault(eng, [])
        if rus not in self.dct[eng]:
            self.dct[eng].append(rus)

        print(self.dct)

    def remove(self, eng):
        if hasattr(self, 'dct') and eng in self.dct:
            del self.dct[eng]
        print('*')



    def translate(self, eng):
        if hasattr(self, 'dct') and eng in self.dct:
            return self.dct[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.remove('car')
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")



assert tr.translate('tree')[0] == "дерево"
print(tr.translate('tree'))