#!/usr/bin/python3 
# -*- coding: utf-8 -*-

import csv

__all__ = ('read_links',  )# Если кортеж из одного элемента в конце должен присутствовать символ , (здесь должны быть представлены все элементы (переменные, функции) из данного модуля).

def read_links(filepath, encoding='utf-8'):
    with open(filepath, 'rt', encoding=encoding) as src:
        rdr = csv.reader(src)
        for n1, n2, penalty in rdr:
            yield int(n1), int(n2), float(penalty) #yield - выдает элемент последовательности который нам нужен.