# -*- coding: utf-8 -*- 

import math
import random

class CustomRow:
	#__MIN = None
	__MAX = None

	__i = None
	__prev = None
	
	def __init__(self, MIN : int, MAX : int):
		__MIN = MIN
		self.__MAX = MAX
		self.__i = 0
		self.__prev = 0

	def __iter__(self):
		self.__i = 1
		self.__prev = 0
		return self

	def __next__(self):
		__i = self.__i
		self.__i = self.__i + self.__prev
		self.__prev = __i
		if(self.__i < self.__MAX):
			return self.__i
		else:
			raise StopIteration 