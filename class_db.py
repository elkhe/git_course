import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a:min(b + 1, len(self.lst_data))]

    def insert(self, data):
        for s in data:
            self.lst_data.append(dict(zip(self.FIELDS, s.split())))



db = DataBase()
db.insert(lst_in)

print(db.lst_data)