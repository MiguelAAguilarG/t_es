import random
import os
#import io
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

verbos1_lista = ['amar', 'cantar', 'hablar', 'tomar','temer','partir','anunciar',
'enviar','averiguar','actuar','bailar','averiguar','aislar','causar']

sujetos_lista = ['Yo','Tu', 'El', 'Ella','Nosotros','Ustedes','Ellos']

t_lista = []
v_lista = []
s_lista = []
#conjugado_lista = []
#completo_lista = []
repeticion_t = []
repeticion_v = []
repeticion_s = []

validacion = ''
i=0

def construir(lista1,lista2,repeticion):
	numeros_buscar = [x for x in range(len(lista1))]
	while True:
		r = random.choice(numeros_buscar)

		if not r in repeticion:
			lista2.append(lista1[r])
			print(lista1[r])
			#completo_lista.append(lista1[r])

			repeticion.append(r)
			break

		if len(repeticion) == len(lista1):
			del repeticion[:]

#numero_archivo = input('Ingresar numero de archivo a crear: ')
while validacion == '':
	os.system('cls')

	construir(sujetos_lista,s_lista,repeticion_t)
	construir(verbos1_lista,v_lista,repeticion_v)
	construir(tiempos_lista,t_lista,repeticion_s)

	x = input('Ingresa la conjugacion correcta: ')
	#conjugado_lista.append(x)
	#completo_lista.append(conjugado_lista[i])

	validacion = input('Continuar [enter]: ')
	i = i+1

'''def escribir_fichero(datos,numero,lista):

	datos = io.open(datos+'_{}.txt'.format(numero_archivo),'w')
	for linea in lista:
		datos.writelines(linea+'\n')
	datos.close()

escribir_fichero('datos_s_lista',numero_archivo,s_lista)
escribir_fichero('datos_v_lista',numero_archivo,v_lista)
escribir_fichero('datos_t_lista',numero_archivo,t_lista)
escribir_fichero('datos_conjugado_lista',numero_archivo,conjugado_lista)
escribir_fichero('datos_completo_lista',numero_archivo,completo_lista)'''


'''datos_t_lista = io.open('datos_s_lista_{}.txt'.format(numero_archivo),'r')
datos = datos_t_lista.readlines()

for linea in range(len(datos)): 
	datos[linea] = datos[linea].rstrip('\n')

print(datos)
datos_t_lista.seek(0)
datos_t_lista.close()'''






