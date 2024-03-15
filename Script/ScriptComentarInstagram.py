import time 
import random 
import pyautogui as pg
from os import system
#importo las librerias que usare
personas = []
frases = ["Vamos","Sis","Concursen","Participando","Amonos","Activo","A ganar","Animo","Participando ando","Vamonos","Participen","Con actitud","Si se puede"]
#En el open deben poner la direccion donde esta la lista
#archivo = open('C:\\Users\\Deivisito\\Documents\\Deivith\\Programacion\\Codigos\\ScriptIG\\Script\\lista.txt')
archivo = open('lista.txt')
#archivo = open('listaLilipink.txt')
opc = 2
maximo = False

#Abro el archivo donde tengo los usuarios que etiquetare
 #El espaciado que agarrara para extraer el usuario
frase = "Amonos"#Si necesito alguna frase en el comentario

def RellenarPersonas():#Con esto relleno mi lista de personas basada en mi txt
	num = 3
	nlinea = 1
	for linea in archivo:
		word = linea.split()
		if(len(word)) == 0:continue
		if nlinea == num:#Aca agarro todos los nombres y lo meto en mi lista de personas
			donde = word[0].find('\"')#Las exepciones necesarias para que solo me tome el usuario e ignore el numero
			new = word[0] #los : y las comillas
			palabra = new[donde + 1:]
			palabra = palabra[:len(palabra) - 1]
			#print(palabra)#PAra corroborar que si esta agarrando la lista
			personas.append(palabra)
			num = num + 3 
		nlinea = nlinea + 1#Para agarrar las lineas

def ciclo (numpersona):#El ciclo que hace para escribir una persona
	global maximo
	if numpersona == len(personas):#Para sorteos donde no se puede repetir personas
		#print("Ha etiquetado a todos, se reiniciara el bucle")
		#system("pause")
		#time.sleep(5)
		numpersona = 0
		maximo = True
	a = personas[numpersona]
	#primer comentario
	pg.hotkey('shift', '2')#si tengo mi teclado en ingles asi es para que haga el @
	pg.write(a)#Escribo mi primera persona
	time.sleep(2)
	pg.press('space')#Aca en frase tengo configurado un espacio
	time.sleep(3)
	if maximo == True:
		numpersona = ((len(personas)) - 2)
	numpersona = numpersona + 1
	return numpersona
 
def main():
	global maximo
	numpersona = 0
	temporizador = 0
	RellenarPersonas()#Relleno mi lista
	Cantidad = len(personas)
	opc = int(input("Cuantas personas etiquetaras : "))
	time.sleep(5)#Espero el intervalo de 5 segundos para que de tiempo de poner el cursor en la barra de comentarios
	for i in range(600):#cantidad de comentarios que hare
		frase = random.choice(frases)#Escojo una frase aleatoria
		if opc == 1:#Depende de cuantas personas quiero etiquetar
			numpersona = ciclo(numpersona)
		else:
			if opc == 2:
				numpersona = ciclo(numpersona)
				numpersona = ciclo(numpersona)
			else:
				if opc == 3:
					numpersona = ciclo(numpersona)
					numpersona = ciclo(numpersona)
					numpersona = ciclo(numpersona)
				else :
					if opc == 4:
						numpersona = ciclo(numpersona)
						numpersona = ciclo(numpersona)
						numpersona = ciclo(numpersona)
						numpersona = ciclo(numpersona)
		time.sleep(3)
		pg.write(frase)
		pg.press('space')
		pg.press('enter')#Presiona enter para comentar
		pg.press('esc')	
		time.sleep(59)#Espero 30 segundos para que no me baneen la cuenta
		temporizador = temporizador + 1
		#if temporizador == 10:#Si hago 10 comentarios espero un rato mas
		#	time.sleep(60)
		#	temporizador = 0

		if maximo == True:
			maximo = False
			numpersona = len(personas)

		#if numpersona == len(personas):#Para sorteos donde no se puede repetir personas
		#	print("Has etiquetado a todos tus contactos, desea seguir aunque se repitan?")
		#	print("si es asi pulsa enter")
		#	system("pause")

		if numpersona == Cantidad:
			numpersona = 0

main()

#De acerdo a si hay que poner alguna frase, etiquetar un numero especifico de personas se pueden cambiar el orden
#de el codigo o las variables

#Al ejecutrar el programa debemos poner el cursos en la barra de comentarios de instagram
#C:\Users\Deivisito\Documents\Deivith\Programacion\Codigos\ScriptIG\Script mi ruta
#Nota hay cuentas de empresa que no se dejan etiquetar e inactiva el comentar
#Hay nombres de usuarios demasiado largos 
'''Si tienen activadas los atajos de teclado el codigo en algun momento puede abrir alguna ventana emergente
de telegram, usualmente estan activados los atajos de b y n , asi que exeptua usuarios con esas letras
si empiezas a tener algun inconveniente'''