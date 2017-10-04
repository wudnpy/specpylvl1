#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging


def timing(function):
	def timed_function(*args, **kwargs): # при определении функции * означает сохранение неопознаных параметров в переменную args, ** означают сохранение именованых неопознаных параметров в переменную kwargs
		T0 = datetime.now()
		Result = function(*args, **kwargs)
		T0 = datetime.now() - T0
		logging.debug('{function.__name__}: {T0.microseconds}'\
		.format(**locals())) # locals - это словарь содержащий все переменные функции, который разбирается при запуске программы на ключ/значение.
		return Result
	return timed_function