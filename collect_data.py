import script
import file_parser
import numpy as np
import os
import time


def collect_data(path, app):
    num = int(input("Введите количество классов обучения: "))
    classes_names = []
    answers = []
    for i in range(num):
        classes_names.append(int(input("Имя класса " + str(i + 1) + ": ")))
    exp = int(input("Колличество экзкмпляров на класс: "))
    for i in range(num):
        classes_names[i] = list(bin(classes_names[i]))[2:]
        for j in range(len(classes_names[i])):
            classes_names[i][j] = int(classes_names[i][j])
        while len(classes_names[i]) < 6:
            classes_names[i].insert(0, 0)
    for i in classes_names:
        for j in range(exp):
            answers.append(i)
    print(classes_names)
    print(answers)
    data = []
    for i in range(num):
        os.system('cls')
        input("Класс " + str(i+1) + '\nPress Enter to continue...')
        for j in range(exp):
            print("Экземпляр", j + 1, end=' ..... ')
            script.save_data(app)
            time.sleep(2)
            data.append(file_parser.open_file(path))
            os.remove(path)
            print("Готово!")
    output = np.array(data)
    classes = np.array(answers)
    return output, classes


