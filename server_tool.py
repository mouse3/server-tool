import os
import time
import json
import subprocess
import webbrowser
import socket

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    print(banner)
    print(decoracion)
#  <----comprobar IP---->
def comprIP():
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    print("n-host" + nombre_equipo)
    print("IP:" + direccion_equipo)
    time.sleep(5)
    os.system("clear")
    start_menu()

#    <--iptracker-->
def IPtrack():
        os.system("clear")
        print(banner)
        print("una vez instalado y estes en el directorio el comando es ./ipTracker.sh -i (ip) ")
        print("pdt:la IP va sin ()")
        print("              |                    1 -->> Download Tool")
        print("              |                    2 -->> Download Tool 2")
        print("              |                    3 -->> Execute Tool")
        print("              |                    4 -->> Exit")
        x = input("              ↳ ")
        if x == "1":
            os.system("git clone https://github.com/m4lal0/ipTracker")
            print("Download!!!")
            time.sleep(1)
            while True:
                Iptrack()
        if x == "2":
            os.system("cd")
            os.system("cd ipTracker")
            os.system("chmod +x ipTracker.sh")
            time.sleep(5)
            os.system("clear")
            while True:
                Iptrack()
        if x == "3":
            os.system("cd")
            os.system("cd ipTracker")
            while True:
                TWebRS()
        if x == "4":
            os.system("clear")
            start_menu
#    <--netstat-->
def netstat():
        os.system("clear")
        print(banner)
        print("una vez netstat este instalado se puede runear desde la consola")
        print("              |                    1 -->> Download Tool")
        print("              |                    2 -->> Comandos")
        print("              |                    3 -->> Exit")
        x = input("              ↳ ")
        if x == "1":
            os.system("sudo apt update")
            time.sleep(10)
            while True:
                os.system("sudo apt install net-tools")
                time.sleep(15)
                os.system("clear")
                print(banner)
                netstat()
        if x == "2":
            print("Los comandos de netstat son:")
            print("	netstat	Modo estándar que informa sobre todas las conexiones de red activas")
            print("netstat -a	Enumera también los puertos abiertos")
            print("	netstat -b	Muestra el archivo ejecutable de una conexión o de un puerto de escucha (requiere permisos de administrador).")
            print("netstat -e	Estadísticas de interfaz (paquetes de datos recibidos y enviados, etc.)")
            print("netstat -f	Devuelve el nombre de dominio cualificado (FQDN) de las direcciones remotas")
            print("	netstat -i	Abre el menú general de netstat")
            print("netstat -n	Visualización numérica de direcciones y números de puerto")
            print("netstat -o	Añade el ID de proceso correspondiente a cada conexión")
            print("netstat -p TCP	Muestra las conexiones para el protocolo especificado, en este caso TCP (también posible: UDP, TCPv6 o UDPv6)")
            print("	netstat -q	Lista todas las conexiones, todos los puertos TCP en escucha y todos los puertos TCP abiertos que no están en escucha")
            print("	netstat -r	Muestra la tabla de enrutamiento")
            print("	netstat -s	Recupera estadísticas sobre los protocolos de red importantes como TCP, IP o UDP")
            print("netstat -t	Muestra el estado de descarga (descarga TCP para liberar al procesador principal) de las conexiones activas ")
            print("	netstat -x	Informa sobre todas las conexiones, los oyentes y los puntos finales compartidos para NetworkDirect")
            print("	netstat -y	Muestra qué plantillas de conexión se utilizaron para las conexiones TCP activas")
            print("netstat -p 10	Muestra de nuevo las estadísticas respectivas después de un número seleccionado de segundos (aquí 10); puede combinarse según sea necesario (aquí con -p),[CTRL] +[C] finaliza la visualización de intervalos")

        if x == "3":
            os.system("clear")
            start_menu

#    <--TWEBRS-->
def TWebRS():
        os.system("clear")
        red()
        print(banner)
        purple()
        print("              |                    1 -->> Download Tool")
        print("              |                    2 -->> Download Tool 2")
        print("              |                    3 -->> Execute Tool")
        print("              |                    4 -->> Exit")
        x = input("              ↳ ")
        if x == "1":
            os.system("https://github.com/HackeRStrategy/Tool-Web-RS")
            print("Download!!!")
            time.sleep(1)
            while True:
                TWebRS()
        if x == "2":
            os.system("cd")
            os.system("cd Tool-Web-RS")
            os.system("bash ToolWeb-RS.sh")
            time.sleep(5)
            os.system("clear")
            while True:
                TWebRS()
        if x == "3":
            os.system("cd")
            os.system("cd Tool-Web-RS")
            os.system("ls")
            os.system("cd Real-Scann-DNS")
            os.system("ls")
            os.system("python2 Real-DNS")
            while True:
                TWebRS()
        if x == "4":
            os.system("clear")
            start_menu()



# <ddos>
def ddos():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        yellow()
        print("")
        print("Downloading...")
        os.system("curl https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py -o ddos.py")
        red()
        print("Downloaded!!")
        time.sleep(2)
        while True:
            ddos()

    if x == "2":
        print("")
        os.system("python3 ddos.py")

    if x == "3":
        start_menu()



def decoracion():
    # hola
    print("1                            -->comprobacion de ip")
    print("2                            -->IPtrack")
    print("3                            -->netstat")
    print("4                            -->TWebRS")
    print("5                            -->ddos")
    print("6                            -->Exit")
    option = input("              +-> ")

    if option == "1":
        comprIP()

    if option == "2":
        IPtrack()

    if option == "3":
        netstat()

    if option == "4":
        TWebRS()

    if option == "5":
        ddos()

    if option == "6":
        exit


banner = """

                    creditos: NOT 4n0nym4to002#9766 
                              Yorkox0
"""
print(banner)

# <-- iniciar la tool -->
decoracion()
start_menu