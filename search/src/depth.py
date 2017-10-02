#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


import data

data_path = os.path.join('C:\\', 'WORK', 'search', 'data')
Graph, Names = data.read_all(data_path)

# TODO Это временно, на самом деле так не спрашивают!!!!
First = Names[input('First: ')]['number']
Last = Names[input('Last: ')]['number']

for path in data.in_depth(Graph, First, Last):
    print(path)















	
	
	
	
	



"""
# Чтение данных в формате csv из менеджера контекста
with open(nodes_path, "rt", encoding="utf-8") as src:
        rdr = csv.reader(src)
        for number, name in rdr: #Можно использовать data вместо number, name чтобы получить последовательность списков.
            print(number, name)
"""


# Присваиваю переменной значение открытия файла.
# src = open(nodes_path, 'rt', encoding='utf-8')# 1 буква: может быть r - чтение, w - запись, a - дополнение; 2 буква: t - текстовый файл, b - бинарный/двоичный файл (байтовый);

"""
# Чтение строк из текстового файла
with open(nodes_path, 'rt', encoding='utf-8') as src:
    for line in src:
        if line[-1] == '\n':#проверяем последний символ в строке
            line = line[:-1]#получаем строку без последнего символа
        print(line)
"""

"""
# Менеджер контекста исполнения
with conn:
    aaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaa
"""

"""# Тройные комментарии не желательны, нужно использовать одиночные или возможности среды разработки для комментирования.

conn = connect(...)
........
conn.begin()
try:
    aaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaa
except:
    conn.rollback()
    raise
else:
    conn.commit()

"""

"""
# Правильная запись вместо конструкции with
try:
    for line in src: #контекст исполнения
        print(line)
finally: #
    src.close()
"""
# Python (как и другие языки программирования) - автоматически определяет на какой ОС работает и преобразует символ перехода на новую строку в в юниксовый вид при чтении, а при записи обратно.

# текстовый файл - последовательность строчек текста (должен быть записан в ASCII совмистимой кодировке);
# двочиный файл - последовательность байт, с началом и концом;

# Отображение перехода на новую строку в разных ОС:
    # \n\r - ОС apple
    # \r\n - MS DOS/Windows
    # \n - unix
    # \n - протягивание бумаги; \r - возврат коретки



# r - read; w - write; a - additional
# t - text; b - binary (picture, sound, etc)
# \n - символ перевода строки (протягивание бумаги); \r - возврат коретки

# Генератор-функция - она отличается от обычной функции тем, что она возвращает особый объект, который является последовательностью, которую можно вставить в цикл for и работать как с обычной последовательностью.

#

