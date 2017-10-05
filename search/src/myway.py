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
AP.add_argument('--debug', dest='loglevel', action='store_const', const=logging.DEBUG, default=logging.WARNING, help='Log level = DEBUG')
AP.add_argument('--no-warning', dest='loglevel', action='store_const', const=logging.ERROR, default=logging.WARNING, help='Log level = ERROR')
AP.add_argument('--width', dest='search_type', action='store_const', const= data.in_width, default = data.in_depth, help='Breadth-First Search')


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
print(ARGS.search_type.__name__)
for path in ARGS.search_type(Graph, First, Last):
    print(path)


