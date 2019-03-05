import os

#http://www.rae.es/diccionario-panhispanico-de-dudas/apendices/modelos-de-conjugacion-verbal
tiempos_lista = []
tiempos_lista.append(['presente',

'pretérito perfecto simple/pretérito',
'pretérito imperfecto/copretérito',
'pretérito pluscuamperfecto/antecopretérito',
'pretérito perfecto compuesto/antepresente',

'futuro simple/futuro',
'futuro compuesto/antefuturo',


'condicional simple/pospretérito',
'condicional compuesto/antepospretérito'])
tiempos_lista.append(['presente',

'pretérito imperfecto/pretérito',
'pretérito pluscuamperfecto/antepretérito',
'pretérito perfecto compuesto/antepresente',

'futuro simple/futuro',
'futuro compuesto/antefuturo'])

guardados = []

s =''
veces = 0
r = 0
e = 0

while s =='':
	os.system('cls')
	print('--Tiempos verbales del indicativo en español--')
	for x in range(len(tiempos_lista[0])):
		print(str(x+1) + '. ' +tiempos_lista[0][x])
	print('\n--Tiempos verbales del subjuntivo en español--')
	for x in range(len(tiempos_lista[1])):
		print(str(x+1) + '. ' +tiempos_lista[1][x])
	input('Continuar [enter]: ')

	os.system('cls')

	contador = 0
	while contador < 2:

		if contador == 0:
			lista_maestra = tiempos_lista[0]
		else:
			lista_maestra = tiempos_lista[1]

		while r < len(lista_maestra):

			if contador == 0:
				entrada = input('{}. Ingrese un tiempo verbal del indicativo: '.format(r+1))
			else:
				entrada = input('{}. Ingrese un tiempo verbal del subjuntivo: '.format(r+1))

			if  entrada in lista_maestra:
				if not entrada in guardados:
					guardados.append(entrada)
					r = r+1
				else:
					print('WARNING. Ya esta dentro de la lista ')
			else:
				print('ERROR. No es un tiempo verbal')
				e = e + 1

			if e >= 5:
				print('DEMASIADOS ERRORES')
				e = 0
				break

		r = 0
		guardados = []
		veces = veces + 1

		contador = contador + 1

	s = input('Continuar [enter]: ')

print(veces)

input()