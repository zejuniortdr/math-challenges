#!/usr/bin/env python
# coding: utf-8

def log(texto):
	print "######################################################"
	print texto
	print "######################################################"

def yahtzees():
	from datetime import datetime
	from decimal import Decimal
	from math import pow
	from random import randint

	inicio = datetime.now()

	try:
		y = int(input("How many yahtzees (default 1): "))
	except:
		y = 1

	try:
		n = int(input("How many dices (default 5): "))
	except:
		n = 5

	try:
		f = int(input("How many faces per dice (default: 6): "))
	except:
		f = 6

	log("Probability: {}%".format( pow( Decimal(1)/Decimal(f), Decimal(n)-Decimal(1) ) * 100))
	cont = 0
	while cont < y:
		yahtzee = False
		tries = 0
		while not yahtzee:
			i = 0
			dices = []
			while i < n:
				dices.append(randint(1,f))
				i += 1

			j = 0
			yahtzee = True
			while j + 1 < len(dices):
				if dices[j] != dices[j+1]:
					yahtzee = False
					print("#{}: {} [{}]".format(tries, dices, (datetime.now()-inicio)))
					tries += 1
					break
				j += 1
		log("Tries #{}: {} [{}]".format(tries, dices, (datetime.now()-inicio)))
		log("Probability: {}%".format( pow( Decimal(1)/Decimal(f), Decimal(n)-Decimal(1) ) * 100))
		cont += 1

if __name__ == '__main__':
	yahtzees()


