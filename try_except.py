try:
    #file = open("my_file.txt", encoding="utf-8")
    with open("my_file.txt", encoding="utf-8") as file:
        s = file.readlines()
        int(s)
        print(s)
    # try:
    #     s = file.readlines()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print('Невозможно открыть файл')
except:
    print('Ошибка при работе с файлом')
finally:
    print(file.closed)


try:
    with open("out.txt", "a+") as file:
        file.seek(0)
        file.writelines(['Hello,47\n', 'hello2\n'])
        s = file.readlines()
        print(s)
        
except:
    print('Ошибка при работе с файлом')
