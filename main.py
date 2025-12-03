
from red import ScanRed
import time
from banner import Banner
import os

def main():

    # Limpiar pantalla e imprimir banner
    os.system("clear")
    Banner()

    # Opciones de uso
    done = True
    while(done):
        print("""\033[33m
        (1) Scan (NMAP)
        (2) Sniff
        (3) Banner
        (4) EXIT
    \033[0m""")
        op = int(input("Opción >> "))

        if op == 1:
            ScanRed()
        elif op == 2:
            print("Nada")
        elif op == 3:
            Banner()
        elif op == 4:
            print("[\033[31m!\033[0m] Saliendo...")
            time.sleep(1)
            done = False

main()