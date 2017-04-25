#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print "===================================="
	print txt
	print "===================================="


def divisors(number):
	divisor_candidate = number
	divisors = []

	while divisor_candidate > 0:
		if number % divisor_candidate == 0:
			divisors.append(divisor_candidate)
		divisor_candidate -= 1


	divisors.sort()
	return divisors




if __name__ == '__main__':
	log("Divisors of a number")
	log(divisors(int(input("Number:"))))


