class Viber:
    messages = []

    def add_message(msg):
        Viber.messages.append(msg)


    def remove_message(msg):
        Viber.messages.remove(msg)


    def set_like(msg):
        Viber.messages[Viber.messages.index(msg)].fl_like = not Viber.messages[Viber.messages.index(msg)].fl_like  
        


    def show_last_message(n):
        print(*Viber.messages[:n])


    def total_messages():
        return len(Viber.messages)



class Message:
    def __init__(self, text, fl_like = False) -> None:
        self.text = text
        self.fl_like = fl_like  


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
for i in Viber.messages:
    print(i.text, i.fl_like)
Viber.remove_message(msg)
for i in Viber.messages:
    print(i.text, i.fl_like)
