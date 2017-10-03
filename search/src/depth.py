#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
import logging
from contextlib import suppress

import data

# Создание объекта и определение описания.
AP = argparse.ArgumentParser(description='Search path in graph')
# Создание параметров и определение справки.
AP.add_argument('first', type=str, help='First vertex in path')
AP.add_argument('last', type=str, help='Last vertex in path')
# Создание опций и определение справки.
AP.add_argument('--data-path', '-d', dest='path', action='store', type=str, default='.', help='Path to directory where data files are located')
AP.add_argument('--nodes', '-n', dest='nodes', action='store', type=str, default='nodes.csv', help='Name of nodes file')
AP.add_argument('--links', '-l', dest='links', action='store', type=str, default='links.csv', help='Name of links file')
# Создание переключателя и определение справки.
AP.add_argument('--debug', dest='loglevel', action='store_const', const=logging.DEBUG, default=logging.WARNING, help='log level = DEBUG')
AP.add_argument('--no-warning', dest='loglevel', action='store_const', const=logging.ERROR, default=logging.WARNING, help='log level = ERROR')

ARGS = AP.parse_args()


LogPath = os.path.expanduser(os.path.join('~', '.depth'))
# Ловля ошибки в сокращенной форме, вместо конструкции try except.
with suppress(OSError):
	 os.mkdir(LogPath)
logging.basicConfig(
	level=ARGS.loglevel,
	style='{',
	format='{levelname:8} {asctime} {name:10} {message}' # :8 используется для определения формата длинны параметра levelname (на данный момент его длина составляет 8 символов).
	# filename = os.path.join(LogPath, 'general.log') # создание файла лога.
)

data_path = os.path.abspath(ARGS.path)# преобразование в абсолютный путь # os.path.join() - нужно использовать при назначении относительного пути.

logging.debug('First: {0.first} Last: {0.last}'.format(ARGS))# дополнительные возможности форматирования строки.
logging.debug('Data path: {0.path} ({1})'.format(ARGS, data_path))
logging.debug('Nodes: {0.nodes} Links: {0.links}'.format(ARGS))
logging.info('Test')
logging.warning('Test')
logging.error('Test')
logging.critical('Test')


Graph, Names = data.read_all(data_path, ARGS.nodes, ARGS.links)

First = Names[ARGS.first]['number']
Last = Names[ARGS.last]['number']

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

