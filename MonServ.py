import itertools
import random
from datetime import datetime, timedelta
import sys
import os
from colorama import init
from termcolor import colored
import time

init()

print(colored("Cargando...", 'yellow'))
time.sleep(1)
os.system('clear')

print(colored("""
 __  __             ____                  
|  \/  | ___  _ __ / ___|  ___ _ ____   __
| |\/| |/ _ \| '_ \\___ \ / _ \ '__\ \ / /
| |  | | (_) | | | |___) |  __/ |   \ V / 
|_|  |_|\___/|_| |_|____/ \___|_|    \_/ 
""", 'cyan'))
print(colored("			By Cañas", 'green'))
print(colored("				Version - 1.2.1", 'green'))
print(colored("Ubuntu-server version...", 'magenta'))

# ESCANEOS DE PUERTOS --------------------------------------------------

def analizar_puertos():
    print(colored("Analizando puertos abiertos...", 'yellow'))
    time.sleep(1)
    print(colored("------------------------------------------", "blue"))
    os.system("nmap localhost")
    
def puertos():
    print(colored("Analizando puertos...", 'yellow'))
    time.sleep(1)
    print(colored("------------------------------------------", "blue"))
    os.system("nmap localhost -p 22,80,443")
    
def TOP():
    print(colored("Analizando puertos...", 'yellow'))
    time.sleep(1)
    print(colored("------------------------------------------", "blue"))
    os.system("nmap localhost --top-ports=10")
    
def vuln():
    print(colored("Analizando vulnerabilidades en ssh...", 'yellow'))
    time.sleep(1)
    print(colored("------------------------------------------", "blue"))
    os.system("nmap localhost --script ""vuln"" -p 22")

# ROBUSTEZ DE CONTRASEÑA ----------------------------------------------

def analizar_robustez_contrasena():
    print(colored("Analizando robustez de contraseñas...", 'yellow'))
    time.sleep(2)
    os.system("john --show /etc/shadow")
    time.sleep(1)
    
# SERVICIOS ------------------------------------------------------------


def servicios_en_linea():
    print("Mostrando servicios en línea...")
    os.system("systemctl list-units --type=service")

    
# Usuarios -------------------------------------------------------------

def cantidad_usuarios():
    print(colored("Mostrando cantidad de usuarios...", 'yellow'))
    time.sleep(1)
    print("user    terminal     Fecha y hora de inicio")
    print(colored("------------------------------------------", "blue"))
    os.system("who")
    time.sleep(1)
  
def kill():
    print("users   Terminal     Feheca de inicio")
    print(colored("------------------------------------------", "blue"))
    time.sleep(1)
    os.system("who")
    print(colored("------------------------------------------", "blue"))
    terminal = input("Ingresa la terminal: ")
    opc = input("Estas seguro? [yes or no]: ")
    os.system('clear')
    
    if opc == "yes":
    	os.system('pkill -9 -t' + terminal)
    	print(colored("Lista actualizada:", 'yellow'))
    	time.sleep(1)
    	print(colored("------------------------------------------", "blue"))
    	os.system("who")
    	time.sleep(2)
    elif opc == "no":
    	usuario()   

    else:
    	     print("Opción invalida")
    	     time.sleep(1)


# firewall ---------------------------------------------------------------

def statusF():
	print("Verificando servicio...")
	time.sleep(1)
	os.system('service firewalld status')
	
def Habilitar():
	print("Habilitando Firewall")
	time.sleep(1)
	os.system('systemctl start firewalld && systemctl enable firewalld')
	
def Deshabilitar():
	print("Deshabilitando Firewall")
	time.sleep(1)
	os.system('systemctl stop firewalld && systemctl disable firewalld')
	
def cargarConf():
	print("Cargando Configuraciones")
	time.sleep(1)
	os.system('firewall-cmd --reload')
	
def Lista():
	print("Enlistando servicios...")
	time.sleep(1)
	print(colored("------------------------------------------", 'blue'))
	os.system('firewall-cmd --zone=public --list-all')
	
	
			


# MENUS -------------------------------------------------------------------

def FIREWALLD():
	while True:
		print(colored("------------------------------------------", 'blue'))
		print(colored("FirewallD", 'yellow'))
		print(colored("------------------------------------------", 'blue'))
		print(colored("[1]", 'yellow'), "Estado del Firewall")
		print(colored("[2]", 'yellow'), "Habilitar Firewall")
		print(colored("[3]", 'yellow'), "Deshabilitar Firewall")
		print(colored("[4]", 'yellow'), "Listar servicios protegidos")
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Regresar al menu")
		print(colored("------------------------------------------", 'blue'))
		
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			statusF()
		elif opcion == "2":
			Habilitar()
		elif opcion == "3":
			Deshabilitar()
		elif opcion == "4":
			Lista()
		elif opcion == "0":
			menu()
		elif opcion == "c":
			os.system('clear')	
		else:
			print(colored("Opción no válida", 'red'))
			time.sleep(1)


def menuNmap():
	while True:
		print(colored("------------------------------------------", 'blue'))
		print(colored("Selecciona tipo de Escaneo", 'yellow'))
		print(colored("------------------------------------------", 'blue'))
		print(colored("[1]", 'yellow'), "Escaneo general")
		print(colored("[2]", 'yellow'), "Estado de los puertos importantes")
		print(colored("[3]", 'yellow'), "Top 10 puertos")
		print(colored("[4]", 'yellow'), "Escanear vulnerabilidades en SSH")
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Regresar al menu principal")
		print(colored("------------------------------------------", 'blue'))
		
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			analizar_puertos()
		elif opcion == "2":
			puertos()
		elif opcion == "3":
			TOP()
		elif opcion == "4":
			vuln()
		elif opcion == "0":
			menu()
		else:
			print(colored("Opción no válida", 'red'))
			time.sleep(1)
			
def usuario():
	while True:
		print(colored("------------------------------------------", "blue"))
		print(colored("Usuarios", 'yellow'))
		print(colored("------------------------------------------", "blue"))
		print(colored("[1]", 'yellow'), "Usuarios en linea")
		print(colored("[2]", 'yellow'), "Matar sesiones")
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Regresar al menu principal")
		print(colored("------------------------------------------", "blue"))
		
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			cantidad_usuarios()
		elif opcion == "2":
			kill()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			menu()
		else:
			print(colored("Opción no válida", 'red'))
			time.sleep(1)
			
def menu():
	while True:
		print(colored("------------------------------------------", "blue"))
		print(colored("[1]", 'yellow'), "Firewall")
		print(colored("[2]", 'yellow'), "Analizar puertos")
		print(colored("[3]", 'yellow'), "Opciones de usuario")
		print(colored("[4]", 'yellow'), "Servicios en linea")		
		print(colored("[5]", 'yellow'), "Analizar robustez de contraseña")
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Salir")
		print(colored("------------------------------------------", "blue"))
		
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			FIREWALLD()
		elif opcion == "2":
			menuNmap()
		elif opcion == "3":
			usuario()
		elif opcion == "4":
			servicios_en_linea()		
		elif opcion == "5":
			analizar_robustez_contrasena()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			print(colored("Saliendo...", 'yellow'))
			time.sleep(1)
			os.system('clear')
			sys.exit()
		else:
			print(colored("Opción no válida", 'red'))
			time.sleep(1)
			
if __name__ == '__main__':
    menu()
	
