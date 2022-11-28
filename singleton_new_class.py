TYPE_OS = 1 # 1 - Windows, 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"

    def __init__(self, name) -> None:
        self.name = name


class DialogLinux:
    name_class = "DialogLinux"



class Dialog:
    def __new__(cls, *args, **kwargs):
        os_class = DialogWindows if not TYPE_OS - 1 else DialogLinux
        obj = super().__new__(os_class)
        obj.name = args[0]
        return obj





dlg_1 = Dialog('blablabla')
TYPE_OS = 0
dlg_2 = Dialog('blablabla1')
print(dlg_1.name, dlg_2.name)