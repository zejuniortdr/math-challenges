#!/usr/bin/env python
# coding: utf-8
from divisors import divisors
from datetime import datetime

def log(txt):
	print "===================================="
	print txt
	print "===================================="



def list_of_primes():
	start = datetime.now()

	# Input: an integer n > 1.
	try:
		limit = int(input("List of primes until (Default: 13) : "))
	except:
		limit = 13

	#  Let A be an array of Boolean values, indexed by integers 2 to n,
	#  initially all set to true.
	i = 2
	a = {0:False, 1:False}
	while i <= limit:
		a[i] = True
		i += 1


	i = 2
	j = 2
	while i <= limit:
		j = 2 * i
		while j <= limit:
			a[j] = False
			j += i
		i += 1

	primes = [k for k, v in a.iteritems() if v]
	log(primes)



	end = datetime.now()
	log("Time to find: {}".format(end-start))


if __name__ == '__main__':
	list_of_primes()



