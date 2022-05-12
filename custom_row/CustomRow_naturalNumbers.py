# -*- coding: utf-8 -*- 

import math
import random

class CustomRow:
	__MIN = None
	__MAX = None

	__i = None
	
	def __init__(self, MIN : int, MAX : int):
		self.__MIN = MIN
		self.__MAX = MAX
		self.__i = 0

	def __iter__(self):
		self.__i = self.__MIN-1
		return self

	def __next__(self):
		self.__i += 1
		
		if(self.__i < self.__MAX):
			return self.__i
		else:
			raise StopIteration 
