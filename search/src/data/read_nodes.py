#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

__all__ = ('read_nodes',  )# Если кортеж из одного элемента в конце должен присутствовать символ , (здесь должны быть представлены все элементы (переменные, функции) из данного модуля).

def read_nodes(filepath, encoding='utf-8'):
    with open(filepath, 'rt', encoding=encoding) as src:
        rdr = csv.reader(src)
        for number, name in rdr:
            yield int(number), name #yield - возвращает элемент последовательности в виде кортежа.

