#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

# + - предыдущий символ повторяется один или более раз.
# . - любой символ.
# \d - цифра.
# [] - шаблон
# [<>] - содержит <>.
# [^<>] - содержит любой символ кроме <> .

Deprecated = re.compile('\xa9')
def to_print(text):
	while True:
		M = Deprecated.search(text)
		if not M: return text
 		text = text[:M.start()] + '?' + text[M.end():]

TABLE = re.compile(r'<table\s?[^>]*>.+</table>', re.DOTALL)
ITEM = re.compile(r'''
	<td\b[^<>]*>\d\d\.\d\d\.\d\d\d\d</td> # дата
	<td\b[^<>]*>\d+</td>                  # кол. едениц
	<td\b[^<>]*>\d+\.\d+</td>             # курс
	<td\b[^<>]*>[-+]?\d+\.\d+</td>        # динамика
	''', re.VERBOSE)

with open('history.htm', 'rt', encoding='windows-1251') as src:
	data = src.read()
		
for M  in ITEM.finditer(data)
if M:
	#if '<table' in M.group(0) : continue
	print(to_print(M.group(0)))
	