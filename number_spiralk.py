# -*- coding: utf-8 -*- 

from PIL import Image, ImageDraw, ImageFont
import math
import random
import sys

from custom_row.CustomRow import CustomRow

imgSize = (15000, 10000)
scale = 10
MIN = 1
MAX = 10000
fontSize = 11
outFileName = "out.png"
backgroundColor = (0, 0, 0)
NumColor = (0, 255, 0)

fnt = ImageFont.truetype("./font/font.ttf", fontSize)

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

def main():
	out = Image.new("RGB", imgSize, backgroundColor)
	centerrr = findCenter(imgSize)

	d = ImageDraw.Draw(out)

	cr = CustomRow(MIN, MAX) # https://oeis.org/?language=russian
	dif = (MAX-MIN)//500
	_dif = dif
	j = 0

	for i in cr:
		if(j > dif):
			dif += _dif
			print(f"{'%.3f'%((100*j)/(MAX-MIN))}%")
		drawStar(i, d, centerrr)
		j+=1

	out.save(outFileName)
	print(f"{100}%")
	#out.show()

def help() -> str:
	helpstr='''
-w - width of output picture (default 15000)
-h - hight of output picture (default 10000)
-o - path to the output image (default \"out.png\")
-min - the minimum possible number in polar coordinates (default 1)
-max - the maximum possible number in polar coordinates (default 10000)
-scale - How many times to reduce the output image (default 10)
-fontsize - font size (default 11)
-help or -?- show help (this message)
'''
	return helpstr

def printError() -> str:
	return "Syntax error\n\n" + help()

def getArg(arg : str, argv : list) -> str:
	if(arg in argv):
		index = sys.argv.index(arg)
		if(index+1 >= len(argv)):
			print(printError())
			exit()
		else:
			return argv[index+1]
	else:
		return None

if __name__ == '__main__':
	# python number_spiralk -w -h -o -max -frontsize -scale -help

	if("-help" in sys.argv or "-?" in sys.argv):
		print(help())

	arg_w = getArg("-w", sys.argv)
	if(arg_w == None):
		W = 15000
	else:
		W = int(arg_w)

	arg_h = getArg("-h", sys.argv)
	if(arg_h == None):
		H = 10000
	else:
		H = int(arg_h)

	imgSize = (W, H)

	arg_o = getArg("-o", sys.argv)
	if(arg_o != None):
		outFileName = arg_o

	arg_min = getArg("-min", sys.argv)
	if(arg_min != None):
		MIN = int(arg_min)

	arg_max = getArg("-max", sys.argv)
	if(arg_max != None):
		MAX = int(arg_max)

	arg_scale = getArg("-scale", sys.argv)
	if(arg_scale != None):
		scale = float(arg_scale)

	arg_fontsize = getArg("-fontsize", sys.argv)
	if(arg_fontsize != None):
		fontSize = int(arg_fontsize)

	main()