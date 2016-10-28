#!/usr/bin/env python
# coding: utf-8

def log(texto):
	print "===================================="
	print texto
	print "===================================="


def josephus():
	participantes = int(input("Number of participants: "))
	binario = list(str(bin(participantes)).replace('0b', ''))
	i = 0
	for a in binario:
		if a == '1':
			binario[i] = '0'
			binario.append('1')
			break
		i += 1

	log("Wining Seat: {0}".format(int('0b{0}'.format("".join(binario)),2)))

if __name__ == '__main__':
	josephus()


