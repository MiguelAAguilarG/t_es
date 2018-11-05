import os

#http://www.rae.es/diccionario-panhispanico-de-dudas/apendices/modelos-de-conjugacion-verbal
tiempos_lista= [
'presente',

'preterito perfecto simple/preterito',
'preterito imperfecto/copreterito',
'preterito pluscuamperfecto/antecopreterito',
'preterito perfecto compuesto/antepresente',

'futuro simple/futuro',
'futuro compuesto/antefuturo',


'condicional simple/pospreterito',
'condicional compuesto/antepospreterito']

guardados = []

s =''
veces = 0
r = 0
e = 0

while s =='':
	os.system('cls')
	print('--Tiempos verbales del indicativo en español--')
	for x in range(len(tiempos_lista)):
		print(str(x+1) + '. ' +tiempos_lista[x])
	input('Continuar [enter]: ')

	os.system('cls')

	while r < len(tiempos_lista):

		entrada = input('{}. Ingrese un tiempo verbal: '.format(r+1))

		if  entrada in tiempos_lista:
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


	
	s = input('Continuar [enter]: ')
	r = 0
	guardados = []
	veces = veces + 1

print(veces)

input()