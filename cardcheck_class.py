from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    
    
    @classmethod
    def check_card_number(number):
        n = number.split('-')
        if not all(map(lambda s: s.isdigit(), n)) and len(n) == 4:
            return False
        
        return True
        


    @classmethod
    def check_name(cls, name):
        return True if all(map(lambda s: set(s) <= set(cls.CHARS_FOR_NAME) and s.isupper(), name.split())) and len(name.split()) == 2 else False