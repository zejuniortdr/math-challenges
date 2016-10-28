#!/usr/bin/env python
# coding: utf-8

from math import factorial
from datetime import datetime
from divisors import divisors

def log(txt):
	print "===================================="
	print txt
	print "===================================="



def is_prime(number):
	if number % 2 == 0:
		log("{0} is not prime".format(number))
	else:
		divisors_list = divisors(number)
		if len(divisors_list) > 2:
			log("{0} is not prime, here the divisors:{1}".format(number,divisors_list))
		else:
			log("{0} is prime, here the divisors:{1}".format(number,divisors_list))


if __name__ == '__main__':
	log("Is Prime")
	number = int(input("Number:"))

	is_prime(number)



