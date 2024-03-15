import pyautogui as pg
import time 
#Con este metodo agarro todos los usuarios de ig , via el HTML de la pagina
#En la consola del HTML del instagram genero la lista y todo eso que es lo que tengo en mi archivo ListaIG.txt
time.sleep(5)

for i in range(150):
	pg.write(f'lista.push(obj[{i}].innerText);')
	pg.press('enter')
	time.sleep(1)