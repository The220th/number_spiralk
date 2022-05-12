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
			#print(self.__i)
			bOol = miller_rabin(self.__i, 40)
			if(bOol == True):
				break
		if(self.__i < self.__MAX):
			return self.__i
		else:
			raise StopIteration 


def miller_rabin(n, k):

    if(n == 1 or n == 2 or n == 3):
        return True
	# https://gist.github.com/Ayrx/5884790
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
