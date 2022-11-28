from string import ascii_lowercase, digits

class FormLogin:
    def __init__(self, lgn, psw) -> None:
        self.login = lgn
        self.password = psw

    
    def render_template(self):
        return '\n'.join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits


    def __init__(self, name, size = 10) -> None:
        self.name = TextInput.check_name(name)
        self.size = size


    def get_html(self):
        return f'<p class=\'login\'>{self.name}: <input type=\'text\' size={self.size} />'


    @classmethod
    def check_name(cls, name):
        if not (2 < len(name) < 51 and set(name) <= set(cls.CHARS_CORRECT)): 
            raise ValueError("некорректное поле name")
        return name
        


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size = 10) -> None:
        self.name = PasswordInput.check_name(name)
        self.size = size


    def get_html(self):
        return f'<p class=\'password\'>{self.name}: <input type=\'text\' size={self.size} />'


    @classmethod
    def check_name(cls, name):
        if not (2 < len(name) < 51 and set(name) <= set(cls.CHARS_CORRECT)): 
            raise ValueError("некорректное поле name")
        return name
    


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

print(html)
 