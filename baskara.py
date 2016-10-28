#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print "===================================="
	print txt
	print "===================================="


def baskara():
	from math import sqrt

	log("Baskara Formula")
	log("axˆ2 + bx + c = 0")

	a = int(input("Type value of A:"))
	b = int(input("Type value of B:"))
	c = int(input("Type value of C:"))

	DELTA = pow(b,2) - 4*a*c

	if DELTA == 0:
		x1 = x2 = (-b + sqrt(DELTA)) / 2*a
		log("Solutions: {0}, {1}".format(x1,x2))

	elif DELTA >= 0:
		x1 = (-b + sqrt(DELTA)) / 2*a
		x2 = (-b - sqrt(DELTA)) / 2*a
		log("Solutions: {0}, {1}".format(x1,x2))

	else:
		log("{0}xˆ2 + {1}x + {2} = 0 | Doesn't have Real solutions".format(a,b,c))



if __name__ == '__main__':
	baskara()


