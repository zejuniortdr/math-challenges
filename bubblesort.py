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
	return bubble(a)

if __name__ == '__main__':
	log("Bubble Sort")
	a = [1,4,5,6,2,3,8,9,0,7]
	log("Initial data: {0}".format(a))


	a = bubble(a)
	log("Result: {0}".format(a))