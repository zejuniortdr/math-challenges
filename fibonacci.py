#!/usr/bin/env python
# coding: utf-8

def log(txt):
	print "===================================="
	print txt
	print "===================================="


def fibonacci(number):

	log("Fibonacci list")

	f = [1,1]

	if 0 < number < 3:
		return f[:number]
	else:
		i = 2
		while i < number:
			f.append(f[i-1] + f[i-2])
			i += 1

	return f


if __name__ == '__main__':
	number = int(input("How many numbers:"))
	fibonacci_list = fibonacci(number)
	log("{0}".format(fibonacci_list))

