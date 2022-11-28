from string import ascii_lowercase, digits

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
CHARS_FOR_NAME = ascii_lowercase.upper() + digits

a = "ALEX POPO1."
def check_card_number(number):
    return True if all(map(lambda part: len(part) == 4 and part.isdigit(), number.split('-'))) and len(number) == 19 else False


def check_name(name):
        return True if all(map(lambda s: set(s) <= set(CHARS_FOR_NAME) and s.isupper(), name.split())) and len(name.split()) == 2 else False

print(check_name(a))