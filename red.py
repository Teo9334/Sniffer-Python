
import nmap
from tabulate import tabulate
import os

def ScanRed():
    os.system("clear")
    print("\n[\033[32m+\033[0m] Escaneando RED...")
    nm = nmap.PortScanner()

    # Dirección ip del router
    ROUTER = "192.168.1.1"
    # Máscara de la red
    MASK = "24"

    # Scan No-Port (-sn)
    nm.scan(hosts=f'{ROUTER}/{MASK}', arguments='-sn')

    # TABLA
    cabeza = ["IP", "MAC"]
    datos = list()

    for x in nm.all_hosts():
        direccion = nm[x]['addresses']
        MAC = direccion.get('mac', "No disponible")
        datos.append([x, MAC])

    print("\n\033[32m\t>> DISPOSITIVOS <<\033[0m")
    print(tabulate(datos, headers=cabeza, tablefmt="grid"))

