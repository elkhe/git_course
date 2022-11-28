import sys
class ListObject:
    def __init__(self, data) -> None:
        self.data = data
        self.next_obj = None


    def link(self, obj):
        self.next_obj = obj



lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

head_obj = ListObject(lst_in[0] if lst_in else None)
prev_obj = head_obj
for x in lst_in[1:]:
    new_obj = ListObject(x)
    prev_obj.link(new_obj)
    prev_obj = new_obj
else:
    prev_obj.link = None


link = head_obj
while link:
    elem = link
    print(elem.data)        
    link = elem.next_obj


    
