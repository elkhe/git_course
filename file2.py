try:
    with open("out.txt", "w") as file:
        file.write("Hello1")
        file.write("Hello2")
        file.write("Hello3")
except:
    print('Ошиька')