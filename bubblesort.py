#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print "===================================="
	print txt
	print "===================================="


def bubble(a):
	length = len(a)
	i = 0
	swaps = 0
	while i < length-1:
		if a[i] > a[i+1]:
			aux = a[i+1]
			a[i+1] = a[i]
			a[i] = aux
			swaps += 1
			log("Step: {0}".format(a))
		i += 1
	if swaps == 0:
		return a

	log("Swaps: {0}".format(swaps))
	return bubble(a)

if __name__ == '__main__':
	import random

	log("Bubble Sort")
	qtd = int(input("How many elements: "))
	small = int(input("Smallest number: "))
	big = int(input("Biggest number: "))

	i = 0
	a = []
	while i < qtd:
		a.append(random.randint(small, big))
		i += 1

	#a = [1,4,5,6,2,3,8,9,0,7]
	log("Initial data: {0}".format(a))


	a = bubble(a)
	log("Result: {0}".format(a))