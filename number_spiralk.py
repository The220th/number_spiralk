# -*- coding: utf-8 -*- 

from PIL import Image, ImageDraw, ImageFont
import math
import random


class CustomRow:
	__MAX = 100000

	__i = None
	
	def __init__(self):
		self.__i = 0

	def __iter__(self):
		self.__i = 0
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


'''
class CustomRow:
	__MAX = 100000

	__i = None
	
	def __init__(self):
		self.__i = 0

	def __iter__(self):
		self.__i = 0
		return self

	def __next__(self):
		self.__i += 1
		if(self.__i < self.__MAX):
			return self.__i
		else:
			raise StopIteration
'''

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

imgSize = (15000, 10000)
scale = 10
backgroundColor = (0, 0, 0)
NumColor = (0, 255, 0)

fnt = ImageFont.truetype("./font/font.ttf", 10)

pi2 = 2*math.pi

def findCenter(img_size : tuple) -> tuple:
	x = img_size[0] / 2
	x = int(x+0.5)
	y = img_size[1] / 2
	y = int(y+0.5)
	return (x, y)

def Polar2Coord(coord_r_phi : tuple):
	'''
	(r, phi) -> (x, y)
	'''
	x, y = coord_r_phi[0], 0
	phi = coord_r_phi[1]

	phi = phi - (phi//pi2)*pi2

	cos_phi = math.cos(phi)
	sin_phi = math.sin(phi)

	x_new = x*cos_phi - y*sin_phi
	y_new = x*sin_phi + y*cos_phi

	return (x_new, y_new)


def drawStar(next_num : int, d : "ImageDraw.Draw", centerrr : tuple):
	i = next_num
	x_draw, y_draw = Polar2Coord((i, i))
	toDraw = (centerrr[0]+int(x_draw/scale+0.5), centerrr[1]-int(y_draw/scale+0.5))
	d.multiline_text(toDraw, f"{i}", font=fnt, fill=NumColor)

if __name__ == '__main__':
	out = Image.new("RGB", imgSize, backgroundColor)
	centerrr = findCenter(imgSize)

	d = ImageDraw.Draw(out)

	cr = CustomRow()

	for i in cr:
		drawStar(i, d, centerrr)

	out.save("out.png")
	#out.show()