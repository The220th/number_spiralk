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
		while(True):
			self.__i += 1
			bOol = gcd(self.__i, self.__MAX)
			if(bOol == 1):
				break
		if(self.__i < self.__MAX):
			return self.__i
		else:
			raise StopIteration 


def gcd(a, b):
 	# https://www.geeksforgeeks.org/steins-algorithm-for-finding-gcd/
    if (a == 0):
        return b
    if (b == 0):
        return a
    k = 0
    while(((a | b) & 1) == 0):
        a = a >> 1
        b = b >> 1
        k = k + 1
    while ((a & 1) == 0):
        a = a >> 1
    while(b != 0):
        while ((b & 1) == 0):
            b = b >> 1
        if (a > b):
            temp = a
            a = b
            b = temp
        b = (b - a)
    return (a << k)