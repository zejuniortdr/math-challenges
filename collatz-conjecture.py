#!/usr/bin/env python
# coding: utf-8

def log(texto):
	print "######################################################"
	print texto
	print "######################################################"

def collatz():

	n = int(input("Type an integer > 0: "))

	# range_arr = range(20)
	# for i in range_arr:
	# n = i
	steps = []
	steps.append(n)
	if n < 1:
		log("Impossible")
	else:
		while n != 1:
			if n % 2 == 0:
				n = n/2
			else:
				n = 3*n +1
			steps.append(n)

		log("{0} \n ---  {1} Step(s) for N = {2}".format(steps, len(steps), n))


if __name__ == '__main__':
	collatz()


