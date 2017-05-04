#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print "===================================="
	print txt
	print "===================================="


def prisonbreak_encode(text):
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
	number = ''
	dots = ''
	for l in text.upper():
		for k, v in convert.items():
			pos = 0
			for v2 in v:
				if v2 == l:
					number += '{}'.format(k)
					i = 0
					while i < pos+1:
						dots += '.'
						i += 1
					dots += ' '
				pos += 1

	dots = dots.strip()
	log([number, dots])
	return [number, dots]

def prisonbreak_decode(text, dots):
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

	number = str(text)
	dots_arr = dots.split(' ')
	decoded_text = ''

	log(dots_arr)

	i = 0
	for d in dots_arr:
		letter = convert[int(number[i])][len(d)-1]
		decoded_text += '{}'.format(letter)
		i += 1


	log(decoded_text)
	return decoded_text

if __name__ == '__main__':
	txt = raw_input("Text to encode: ")
	ret = prisonbreak_encode(txt)
	prisonbreak_decode(ret[0], ret[1])