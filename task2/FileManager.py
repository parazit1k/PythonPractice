import os
import shutil
import pathlib

to_send = ['Создание папки','Удаление папки','Переход в директорию','Создание пустого файла','Запись текста в файл','Просмотр файла','Удаление файла','Копирование файла','Перемещение файла','Переименование файла']
copied = False

for i in range(len(to_send)):
    print(f"[{i+1}] - {to_send[i]}")
way = ''
while True:
    cwd = os.getcwd()
    print("Директория:\n")
    did = False
    for path in sorted(pathlib.Path.cwd().rglob('*')):
        depth = len(path.relative_to(pathlib.Path.cwd()).parts)
        spacer = '    ' * depth
        if way != '':
            if path.name == way.split('/')[len(way.split('/'))-1] and not did:
                print(f"{spacer}-- {path.name} *")
                did = True
            else:
                print(f"{spacer}-- {path.name}")
        else:
            print(f"{spacer}-- {path.name}")
    print('\n')
    text = input("Введи, что хочешь сделать: ")
    if text.lower() == 'stop':
        break
    elif text == '1':
        try:
            if way == '':
                os.mkdir(input("Введи название файла: "))
            else:
                os.mkdir(way+"/"+input("Введи название файла: "))
        except FileExistsError:
            print("Такая папка уже есть!")
    elif text == '2':
        try:
            if way == '':
                shutil.rmtree(input("Введи название файла: "))
            else:
                shutil.rmtree(way+"/"+input("Введи название файла: "))
        except Exception as e:
            print(e)
            print("Такого файла нет:(")
    elif text == '3':
        print("Введи путь вида: 'home/bin/package', '. .', чтобы вернуться")
        toadd = input("Введи путь к папке: ")
        if toadd == '. .':
            way = ''
        else:
            try:
                os.mkdir(way + toadd +'/test')
                os.rmdir(way + toadd +'/test')
                way += toadd
                if input("Использовать этот путь в других параметрах?(1 - да, 2 - нет)\n") == "1":
                    pass
                else:
                    way = ''
            except:
                print("Нет такого пути:(")
    elif text == '4':
        if way == "":
            f = open(f"{input('Введи название файла: ')}.txt",'w+')
            f.close()
        else:
            f = open(f"{way}/{input('Введи название файла: ')}.txt",'w+')
            f.close()
    elif text == '6':
        try:
            if way == "":
                f = open(f"{input('Введи файл, который хочешь прочитать: ')}.txt", "r", encoding = 'utf-8')
                for i in f:
                    print(i)
                f.close()
            else:
                f = open(f"{way}/{input('Введи файл, который хочешь прочитать: ')}.txt", "r", encoding = 'utf-8')
                for i in f:
                    print(i)
                f.close()
        except:
            print("Такого файла нет:(")
    elif text == '5':
        try:
            to_write = ''
            if way == "":
                f = open(f"{input('Введи файл, который хочешь записать: ')}.txt", "a", encoding = "utf-8")
                while True:
                    check = input("Введи, что записать: ")
                    if check.lower() == "stop":
                        break
                    else:
                        to_write += f"{check}\n"
                f.write(to_write)
                f.close()
            else:
                f = open(f"{way}/{input('Введи файл, который хочешь записать: ')}.txt", "a", encoding = "utf-8")
                while True:
                    check = input("Введи, что записать: ")
                    if check.lower() == "stop":
                        break
                    else:
                        to_write += f"{check}\n"
                f.write(to_write)
                f.close()
        except:
            print("Такого файла нет:(")
    elif text == '7':
        try:
            if way == "":
                os.remove(input("Введите какой файл удалить: "))
            else:
                os.remove(f"{way}/{input('Введите какой файл удалить: ')}")
        except:
            print("Нет такого файла:(")
    elif text == '8':
        to_copy = input("Введите имя файла, который надо скопировать: ")
        try:
            copied = False
            os.mkdir(to_copy)
            os.rmdir(to_copy)
            print("Такого файла нет:(")
        except:
            print("Успешно скопировал:)")
            copied = True
    elif text == '9':
        if not copied:
            print("Сначала выбери, что скопировать!")
        else:
            if way == "":
                shutil.copyfile(way + "/" + to_copy,str(input("Введи имя файла: ")))
    elif text == '10':
        try:
            os.rename(way + "/" +str(input("Введите, какой файл переименовать: ")), way + "/" +str(input("В какой "
                                                                                                "переименовать: ")))
        except:
            print("Такого файла нет:(")
    else:
        print("Введи номер слева!")