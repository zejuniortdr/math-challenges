#!/usr/bin/env python
# coding: utf-8

def pi_by_probability():
	from random import randint
	from fractions import gcd
	from decimal import Decimal
	from math import sqrt, pi

	try:
		tries = int(input("Number of tries (blank for 500): "))
	except:
		tries = 500

	try:
		random_start = int(input("Random start (blank for 1): "))
	except:
		random_start = 1

	try:
		random_end = int(input("Random end (blank for 120): "))
	except:
		random_end = 120

	i = 0
	cofactors = 0
	coprimes = 0
	while i < tries:
		a = randint(random_start,random_end)
		b = randint(random_start,random_end)

		if gcd(a, b) == 1:
			coprimes += 1
		i += 1
		print("{0}/{1} - {2}%".format(i, tries, Decimal(i)/Decimal(tries)*100))

	cofactors = tries - coprimes

	print("{0} cofactors, {1} coprimes, total: {2}".format(cofactors, coprimes, cofactors+coprimes))
	x = Decimal(coprimes) / Decimal(tries)
	print("X: {0}".format(x))

	PI = sqrt(6/x)

	print("Constant PI: {0}".format(pi))
	print("PI found: {0}".format(PI))

	diff = abs(PI-pi)
	print("DIFF: {0}, {1}%".format(diff, round((diff/PI)*100,2)))


def do_until_pi():
	from random import randint
	from fractions import gcd
	from decimal import Decimal
	from math import sqrt, pi


	try:
		random_start = int(input("Random start (blank for 1): "))
	except:
		random_start = 1

	try:
		random_end = int(input("Random end (blank for 120): "))
	except:
		random_end = 120

	try:
		precision = int(input("Precision: (blank for 0.0001): "))
	except:
		precision = float(0.0001)


	PI = 0
	diff = abs(PI-pi)
	tries = 0
	cofactors = 0
	coprimes = 0
	while diff > precision:
		a = randint(random_start,random_end)
		b = randint(random_start,random_end)
		if gcd(a, b) == 1:
			coprimes += 1
		tries += 1

		cofactors = tries - coprimes
		x = float(coprimes) / float(tries)

		PI = sqrt(6/x)
		diff = abs(PI-pi)
		print("PI CONSTANT: {0} / PI found: {1} / DIFF: {2}, {3}%".format(pi, PI, diff, round((diff/PI)*100,2)))


if __name__ == '__main__':
	#pi_by_probability()
	do_until_pi()



