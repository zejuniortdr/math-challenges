#!/usr/bin/env python
# coding: utf-8

from math import factorial
from datetime import datetime

def log(txt):
	print "===================================="
	print txt
	print "===================================="


def factorial_recursive(number):
	if number == 1 or number == 0:
		return 1
	return number * factorial_recursive(number-1)


def factorial_loop(number):
	result = 1
	while number > 1:
		result *= number
		number -= 1

	return result


if __name__ == '__main__':
	log("Factorial of number")
	number = int(input("Number:"))

	if number >= 0:

		# FACTORIAL BUILT IN
		t1 = datetime.now()
		fb = factorial(number)
		t2 = datetime.now()
		log("BUILT-IN : {0} in {1}".format(fb,t2-t1))

		# FACTORIAL LOOP
		t1 = datetime.now()
		fl = factorial_loop(number)
		t2 = datetime.now()
		log("LOOP     : {0} in {1}".format(fl,t2-t1))

		# FACTORIAL RECURSIVE
		try:
			t1 = datetime.now()
			fr = factorial_recursive(number)
			t2 = datetime.now()
			log("RECURSIVE: {0} in {1}".format(fr,t2-t1))
		except:
			log("RECURSIVE: maximum recursion depth exceeded")

	else:
		log("factorial not defined for negative values")






