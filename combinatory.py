#!/usr/bin/env python
# coding: utf-8

def log(texto):
	print "######################################################"
	print texto
	print "######################################################"

def gerar():
	"""
	Prints every possible combination with stuff elements
	"""
	import itertools

	#stuff = [8, 68, 67, 142, 137, 170, 159, 105, 108, 178, 5, 71, 58, 55, 427, 353, 1674, 421]
	stuff = range(10)

	i = 0
	for L in range(0, len(stuff)+1):
		for subset in itertools.combinations(stuff, L):
			i += 1
			print(subset)

	log("{0} combinations".format(i))

if __name__ == '__main__':
	gerar()


