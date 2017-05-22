#!/usr/bin/env python
# coding: utf-8

def log(txt):
	print "===================================="
	print txt
	print "===================================="


def josephus():
	participants = int(input("Number of participants: "))
	binary_form = list(str(bin(participants)).replace('0b', ''))
	i = 0
	for a in binary_form:
		if a == '1':
			binary_form[i] = '0'
			binary_form.append('1')
			break
		i += 1

	log("Wining Seat: {0}".format(int('0b{0}'.format("".join(binary_form)),2)))

if __name__ == '__main__':
	josephus()


