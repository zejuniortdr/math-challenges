#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print("="*50)
	print(txt)
	print("="*50)


def divisors(number):
	return [n for n in range(1, number+1) if number % n == 0]


if __name__ == '__main__':
	log("Divisors of a number")
	log(divisors(int(input("Number:"))))


