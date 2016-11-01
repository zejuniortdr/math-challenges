#!/usr/bin/env python
# coding: utf-8

def log(txt):
	print "===================================="
	print txt
	print "===================================="


def vacation():
	from datetime import date, timedelta

	ano = 2017

	holidays = [
		{'day':date(ano,1,01), 'txt': 'Ano novo'},
		{'day':date(ano,2,28), 'txt': 'Carnaval'},
		{'day':date(ano,1,01), 'txt': 'Ano novo'},
		{'day':date(ano,4,14), 'txt': 'Sexta-feira da Paixão'},
		{'day':date(ano,4,16), 'txt': 'Páscoa'},
		{'day':date(ano,4,21), 'txt': 'Tiradentes'},
		{'day':date(ano,5,01), 'txt': 'Dia do Trabalho'},
		{'day':date(ano,6,15), 'txt': 'Corpus Christi'},
		{'day':date(ano,9,07), 'txt': 'Independência do Brasil (Sete de Setembro)'},
		{'day':date(ano,10,12), 'txt': 'Nossa Senhora Aparecida'},
		{'day':date(ano,11,02), 'txt': 'Finados'},
		{'day':date(ano,11,15), 'txt': 'Proclamação da República'},
		{'day':date(ano,12,25), 'txt': 'Natal'},
	]


	timeoff = int(input("Quandos dias deseja tirar?"))

	best_interval = {'inicio':None, 'termino':None, 'total':0}


	for h in holidays:
		inicio = h['day'] - timedelta(days=timeoff)
		termino = h['day']
		total = termino - inicio
		dias = total.days + 1

		if inicio.weekday() == 5:
			inicio += timedelta(days=2)
			dias += 2
		elif inicio.weekday() == 6:
			inicio += timedelta(days=1)
			dias += 1

		if inicio.year == ano:
			total = h['day'] - inicio
			if total.days + 1 > best_interval['total']:
				best_interval['inicio'] = inicio
				best_interval['termino'] = h['day']
				best_interval['total'] = total.days + 1

			inicio = h['day'] + timedelta(days=1)
			termino = inicio + timedelta(days=timeoff) - timedelta(days=1)
			total = termino - inicio
			dias = total.days + 1

			if inicio.weekday() == 5:
				inicio += timedelta(days=2)
			elif inicio.weekday() == 6:
				inicio += timedelta(days=1)

			if termino.weekday() == 5:
				dias += 2
			elif termino.weekday() == 6:
				dias += 1


			if dias > best_interval['total']:
				best_interval['inicio'] = inicio
				best_interval['termino'] = termino
				best_interval['total'] = dias


	log(best_interval)

if __name__ == '__main__':
	vacation()


