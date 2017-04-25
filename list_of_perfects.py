#!/usr/bin/env python
# coding: utf-8
from divisors import divisors
from datetime import datetime

def log(txt):
	print "===================================="
	print txt
	print "===================================="



def list_of_perfects():
	start = datetime.now()
	qtd = int(input("How many perfect numbers do you want? Type here: "))
	perfects = []

	n = 2
	while len(perfects) < qtd:
		i = n - 1
		divisors = []
		while i > 0:
			if n % i == 0:
				divisors.append(i)
			i -= 1
		if sum(divisors) == n:
			perfects.append(n)
			log("{}/{} found: {} (in {})".format(len(perfects), qtd, n, datetime.now()-start))

		n += 1
	end = datetime.now()
	print(perfects)
	log("Time to find: {}".format(end-start))





if __name__ == '__main__':
	list_of_perfects()



