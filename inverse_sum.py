#!/usr/bin/env python
# coding: utf-8
from decimal import Decimal

def log(txt):
	print "===================================="
	print txt
	print "===================================="


def inverse_sum(number):

	log("Fibonacci list")

	i = 1
	total = Decimal(0)
	while i <= number:
		total += Decimal(1)/Decimal(i)
		i += 1
	return total

if __name__ == '__main__':
	number = int(input("Sum inverses until: "))
	s = inverse_sum(number)
	log("For {0} numbers, the sum is: {1}".format(number, s))

