import os
import sys
import time

print("Cargando...")
time.sleep(1)
os.system('clear')

print("""
 __  __             ____                  
|  \/  | ___  _ __ / ___|  ___ _ ____   __
| |\/| |/ _ \| '_ \\___ \ / _ \ '__\ \ / /
| |  | | (_) | | | |___) |  __/ |   \ V / 
|_|  |_|\___/|_| |_|____/ \___|_|    \_/ 
		by Cañas
			version - 1
""")

# ESCANEOS DE PUERTOS --------------------------------------------------

def analizar_puertos():
    print("Analizando puertos abiertos...")
    time.sleep(1)
    os.system("nmap localhost")
    
def puertos():
    print("Analizando puertos...")
    time.sleep(1)
    os.system("nmap localhost -p 22,80,443")
    
def TOP():
    print("Analizando puertos...")
    time.sleep(1)
    os.system("nmap localhost --top-ports=10")
    
def vuln():
    print("Analizando vulnerabilidades en ssh...")
    time.sleep(1)
    os.system("nmap localhost --script ""vuln"" -p 22")

# ROBUSTEZ DE CONTRASEÑA ----------------------------------------------

def analizar_robustez_contrasena():
    print("Analizando robustez de contraseñas...")
    time.sleep(2)
    os.system("john --show /etc/shadow")
    time.sleep(1)
    
# SERVICIOS ------------------------------------------------------------


def servicios_en_linea():
    print("Mostrando servicios en línea...")
    os.system("systemctl list-units --type=service")

    
# Usuarios -------------------------------------------------------------

def cantidad_usuarios():
    print("Mostrando cantidad de usuarios...")
    time.sleep(1)
    print("user    terminal     Fecha y hora de inicio")
    print("------------------------------------------")
    os.system("who")
    time.sleep(1)
    
def kill():
    print("Matando sesiones...")
    time.sleep(1)
    os.system("""sudo pkill -KILL -u $(users | tr ' ' '\n' | grep -v root)
""")

# FIREWALLD ---------------------------------------------------------------
'''
def FIREWALLD():
	while True:
'''
# MENUS -------------------------------------------------------------------

def menuNmap():
	while True:
		print("------------------------------------------")
		print("Selecciona tipo de Escaneo")
		print("------------------------------------------")
		print("[1] Escaneo general")
		print("[2] Estado de los puertos importantes")
		print("[3] Top 10 puertos")
		print("[4] Escanear vulnerabilidades en SSH")
		print("[c] Limpiar consola")
		print("[0] Regresar al menu principal")
		print("------------------------------------------")
		
		opcion = input("Selecciona una opción: ")
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
			break
		      
		else:
			print("Opción no válida")
			
def usuario():
	while True:
		print("------------------------------------------")
		print("[1] Usuarios en linea")
		print("[2] Matar todas las sesiones (NO usar BETA)")
		print("[c] Limpiar consola")
		print("[0] Regresar al menu principal")
		print("------------------------------------------")
		
		opcion = input("Selecciona una opción: ")
		os.system('clear')
		
		if opcion == "1":
			cantidad_usuarios()
		elif opcion == "2":
			kill()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			menu()
			break
		else:
			print("Opción invalida")
			
def menu():
	while True:
		print("------------------------------------------")
		print("[1] Analizar puertos")
		print("[2] Opciones de usuario")
		print("[3] Servicios en linea")		
		print("[4] Analizar robustez de contraseña")
		print("[c] Limpiar consola")
		print("[0] Salir")
		print("------------------------------------------")
		
		opcion = input("Selecciona una opción: ")
		os.system('clear')

		if opcion == "1":
			menuNmap()
		elif opcion == "2":
			usuario()
		elif opcion == "3":
			servicios_en_linea()		
		elif opcion == "4":
			analizar_robustez_contrasena()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			sys.exit()
			break
		
		else:
			print("Opción no válida")
			
if __name__ == '__main__':
    menu()
	
