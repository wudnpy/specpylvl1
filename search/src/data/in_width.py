#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ('in_width', )

def in_width(graph, first, last):
	
	Path = [first]
	
	while Path:
		print('PATH: '+str(Path))
		Node = graph[Path[-1]] # узел
		print('NODE: '+str(Node['name']))		
		R = set(Node['neighbours'].keys()) # соседи
		print('NEIGHBOURS: ' + str(Node['neighbours'].keys()))
		print('PROHIBITED: ' + str(Node['prohibited']))
		R -= Node['prohibited'] # запрещенные ребра
		try:
			next = R.pop() # удаляю элемент из множества
			print('УДАЛЯЮ ЭЛЕМЕНТ ИЗ МНОЖЕСТВА: '+str(next))
			Node['prohibited'].add(next) # добавляю запрещенное ребро
			print('ДОБАВЛЯЮ ЗАПРЕЩЕННОЕ РЕБРО: ' + str(next) + ' в ' + str(Node['name']))
			if next == last:
				print('ВОЗВРАЩАЮ КОРТЕЖ: '+str((Path + [next])))
				yield Path + [next] # возвращаю кортеж
			elif next in Path:
				print('ПАССУЮ')
				pass
			else:
				Path.append(next) # добавляю путь
				print('ДОБАВЛЯЮ ЭЛЕМЕНТ В ПУТЬ: '+str(next))
		except KeyError: # лювлю исключение
			print('ОБНУЛЯЮ МНОЖЕСТВО')
			Node['prohibited'] = set() # обнуляю множество
			print('УДАЛЯЮ ПОСЛЕДНИЙ ЭЛЕМЕНТ ИЗ ПУТИ: ' + str(Path[-1]))
			del Path[-1] # удаляю элемент из пути