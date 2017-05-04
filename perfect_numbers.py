#!/usr/bin/env python
# coding: utf-8
from divisors import divisors

def log(txt):
	print "===================================="
	print txt
	print "===================================="


def is_perfect(number):

	log("Perfect number")

	divisors_list = divisors(number)
	divisors_list.pop()

	if sum(divisors_list) == number:
		return {'is':True, 'divisors':divisors_list}
	return {'is':False,}



if __name__ == '__main__':
	number = int(input("Number:"))
	is_perfect_number = is_perfect(number)
	if is_perfect_number['is']:
		log("{0} is perfect: {1} = {0}".format(number, ' + '.join(str(x) for x in is_perfect_number['divisors'])))
	else:
		log("{0} is not perfect".format(number))



