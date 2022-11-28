import pickle

book1 = ["Евгений Онегин", "Пушник А. С.", 200]
book2 = ["Муму", "Тургенев И. С. 250", 231]

try:
    with open("out.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
except:
    print('Ошибка')

print(b1, b2, sep='\n')