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
		{'day':date(ano,1,1), 'txt': 'Ano novo'},
		{'day':date(ano,2,28), 'txt': 'Carnaval'},
		{'day':date(ano,1,01), 'txt': 'Ano novo'},
		{'day':date(ano,4,14), 'txt': 'Sexta-feira da Paixão'},
		{'day':date(ano,4,16), 'txt': 'Páscoa'},
		{'day':date(ano,4,21), 'txt': 'Tiradentes'},
		{'day':date(ano,5,1), 'txt': 'Dia do Trabalho'},
		{'day':date(ano,6,15), 'txt': 'Corpus Christi'},
		{'day':date(ano,6,16), 'txt': 'Corpus Christi'},
		{'day':date(ano,9,7), 'txt': 'Independência do Brasil (Sete de Setembro)'},
		{'day':date(ano,9,8), 'txt': 'Independência do Brasil (Sete de Setembro)'},
		{'day':date(ano,10,12), 'txt': 'Nossa Senhora Aparecida'},
		{'day':date(ano,10,13), 'txt': 'Nossa Senhora Aparecida'},
		{'day':date(ano,11,2), 'txt': 'Finados'},
		{'day':date(ano,11,3), 'txt': 'Finados'},
		{'day':date(ano,11,15), 'txt': 'Proclamação da República'},
		{'day':date(ano,12,25), 'txt': 'Natal'},
	]


	timeoff = int(input("Quandos dias deseja tirar? "))

	best_interval = {'inicio':None, 'termino':None, 'total':0}
	todos = []

	for h in holidays:
		# Iniciando no feriado:
		if h['day'].weekday() == 3:
			# QUINTA / POSSIVEL EMENDA SEX
			for h2 in holidays:
				if h['day']+timedelta(1) == h2['day']:
					# quinta com emenda na sexta
					inicio = h['day']
					inicio_legal = h['day']+timedelta(4)
					termino = inicio_legal+timedelta(timeoff)
					termino_weekday = termino.weekday()
					while termino_weekday in [5,6]:
						termino = termino+timedelta(1)
						termino_weekday = termino.weekday()

					for h3 in holidays:
						if termino == h3['day']:
							termino = termino+timedelta(1)

							while termino_weekday in [5,6]:
								termino = termino+timedelta(1)
								termino_weekday = termino.weekday()

					total = termino - inicio

					todos.append({'inicio':inicio, 'termino':termino, 'total':total.days, 'inicio_legal':inicio_legal})
		elif h['day'].weekday() == 1:
			# TERCA  / POSSIVEL EMENDA SEG
			for h2 in holidays:
				if h['day']-timedelta(1) == h2['day']:
					# quinta com emenda na sexta
					inicio = h['day']
					inicio_legal = h['day']+timedelta(1)
					termino = inicio_legal+timedelta(timeoff)
					termino_weekday = termino.weekday()
					while termino_weekday in [5,6]:
						termino = termino+timedelta(1)
						termino_weekday = termino.weekday()

					for h3 in holidays:
						if termino == h3['day']:
							termino = termino+timedelta(1)

							while termino_weekday in [5,6]:
								termino = termino+timedelta(1)
								termino_weekday = termino.weekday()

					total = termino - inicio

					todos.append({'inicio':inicio, 'termino':termino, 'total':total.days, 'inicio_legal':inicio_legal})

		elif h['day'].weekday() == 0:
			# SEGUNDA
			inicio = h['day']
			inicio_legal = h['day']+timedelta(1)
			termino = inicio_legal+timedelta(timeoff)
			termino_weekday = termino.weekday()
			while termino_weekday in [5,6]:
				termino = termino+timedelta(1)
				termino_weekday = termino.weekday()

			for h3 in holidays:
				if termino == h3['day']:
					termino = termino+timedelta(1)

					while termino_weekday in [5,6]:
						termino = termino+timedelta(1)
						termino_weekday = termino.weekday()

			total = termino - inicio

			todos.append({'inicio':inicio, 'termino':termino, 'total':total.days, 'inicio_legal':inicio_legal})

		elif h['day'].weekday() == 4:
			# SEXTA
			inicio = h['day']
			inicio_legal = h['day']+timedelta(3)
			termino = inicio_legal+timedelta(timeoff)
			termino_weekday = termino.weekday()
			while termino_weekday in [5,6]:
				termino = termino+timedelta(1)
				termino_weekday = termino.weekday()

			for h3 in holidays:
				if termino == h3['day']:
					termino = termino+timedelta(1)

					while termino_weekday in [5,6]:
						termino = termino+timedelta(1)
						termino_weekday = termino.weekday()

			total = termino - inicio

			todos.append({'inicio':inicio, 'termino':termino, 'total':total.days, 'inicio_legal':inicio_legal})

	for t in todos:
		log(t)

if __name__ == '__main__':
	vacation()


