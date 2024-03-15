import time 
import random 
import pyautogui as pg
#importo las librerias que usare
personas = []
frases = ["Vamos","Sis","Concursen","Participando","Amonos","Activo","A ganar","Animo","Participando ando","Vamonos","Participen","Con actitud","Si se puede"]
#En el open deben poner la direccion donde esta la lista
#archivo = open('C:\\Users\\Deivisito\\Documents\\Deivith\\Programacion\\Codigos\\ScriptIG\\Script\\lista.txt')
archivo = open('lista.txt')
#archivo = open('listaLilipink.txt')

#Abro el archivo donde tengo los usuarios que etiquetare
num = 3 #El espaciado que agarrara para extraer el usuario
frase = "Amonos"#Si necesito alguna frase en el comentario
nlinea = 1
temporizador = 0
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

time.sleep(5)#Espero el intervalo de 5 segundos para que de tiempo de poner el cursor en la barra de comentarios

for i in range(600):# mis variables a,b y c es para las personas que etiquetare, se configuran de acuerdo a su preferencia
	a = random.choice(personas)#Le asigno una persona aleatoria de mi lista de personas
	b = random.choice(personas)
	#c = random.choice(personas)
	d = random.choice(frases)
	#primer comentario
	pg.hotkey('shift', '2')#si tengo mi teclado en ingles asi es para que haga el @
	pg.write(a)#Escribo mi primera persona
	time.sleep(2)
	pg.press('space')#Aca en frase tengo configurado un espacio
	time.sleep(3)
	#Segundo comentario
	pg.hotkey('shift', '2')#Escribe otra persona @
	pg.write(b)
	pg.press('space')#Dejo un espacio
	time.sleep(2)
	#Tercer coentario
	'''pg.hotkey('shift', '2')#Escribe otra persona @
	pg.write(c)
	pg.press('space')#Dejo un espacio
	time.sleep(2)'''
	#pg.press('space')
	pg.write(d)
	pg.press('enter')#Presiona enter para comentar
	time.sleep(2)
	time.sleep(10)
	pg.press('enter')
	pg.press('esc')
	#Volver a comentar pero con otra secuencia 
	time.sleep(30)#Espero 30 segundos para que no me baneen la cuenta
	a = random.choice(personas)#Le asigno una persona aleatoria de mi lista de personas
	b = random.choice(personas)
	#c = random.choice(personas)
	d = random.choice(frases)
	#Primer comentario
	pg.hotkey('shift', '2')#si tengo mi teclado en ingles asi es para que haga el @
	pg.write(a)#Escribo mi primera persona
	time.sleep(1)
	pg.press('space')#Aca en frase tengo configurado un espacio
	#Segundo comentario
	pg.hotkey('shift', '2')#Escribe otra persona @
	pg.write(b)
	time.sleep(4)
	pg.press('space')#Dejo un espacio
	#pg.press('space')
	#Tercer comentario
	'''pg.hotkey('shift', '2')
	time.sleep(2)
	pg.write(c)
	time.sleep(1)
	pg.press('space')#Dejo un espacio'''
	#pg.press('space')
	time.sleep(3)
	pg.write(d)
	pg.press('space')
	#pg.press('space')
	pg.press('enter')#Presiona enter para comentar
	time.sleep(2)
	#pg.press('backspace')
	time.sleep(30)
	temporizador = temporizador + 1
	if temporizador == 10:
		time.sleep(150)
		temporizador = 0 
#De acerdo a si hay que poner alguna frase, etiquetar un numero especifico de personas se pueden cambiar el orden
#de el codigo o las variables

#Al ejecutrar el programa debemos poner el cursos en la barra de comentarios de instagram
#C:\Users\Deivisito\Documents\Deivith\Programacion\Codigos\ScriptIG\Script mi ruta
#Nota hay cuentas de empresa que no se dejan etiquetar e inactiva el comentar
#Hay nombres de usuarios demasiado largos 
'''Si tienen activadas los atajos de teclado el codigo en algun momento puede abrir alguna ventana emergente
de telegram, usualmente estan activados los atajos de b y n , asi que exeptua usuarios con esas letras
si empiezas a tener algun inconveniente'''
'''
43
: 
"tami.hearts"'''