#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print "===================================="
	print txt
	print "===================================="


def text2cellpad(number):
	import itertools
	convert = {
		0: ['+'],
		1: [' '],
		2: ['A','B','C'],
		3: ['D','E','F'],
		4: ['G','H', 'I'],
		5: ['J','K', 'L'],
		6: ['M','N', 'O'],
		7: ['P','Q', 'R', 'S'],
		8: ['T','U', 'V'],
		9: ['W','X', 'Y', 'Z'],
	}


	lists = []
	for d in str(number):
		lists.append(convert[int(d)])

	words = []
	for i in list(itertools.product(*lists)):
		words.append(''.join(i))

	return words







if __name__ == '__main__':

	number = int(input("Number: "))
	text = text2cellpad(number)

	log(text)