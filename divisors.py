#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print "===================================="
	print txt
	print "===================================="


def divisors():

	log("Divisors of a number")

	number = int(input("Number:"))
	divisor_candidate = number-1
	divisors = []

	while divisor_candidate > 0:
		if number % divisor_candidate == 0:
			divisors.append(divisor_candidate)
		divisor_candidate -= 1



	log(divisors)




if __name__ == '__main__':
	divisors()


