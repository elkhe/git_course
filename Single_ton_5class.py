class SingletonFive:
    __obj_number = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj_number < 5:
            cls.__obj_number += 1
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance



    def __init__(self, name) -> None:
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
# for x in objs:
#     print(x.name)