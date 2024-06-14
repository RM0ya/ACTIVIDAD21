import os
import msvcrt
import csv

datos = []

def printR(texto : str):
    print(f"\033[31m{texto}\033[0m")

def printV(texto : str):
    print(f"\033[32m{texto}\033[0m")

def printA(texto : str):
    print(f"\033[34m{texto}\033[0m")
    
def printM(texto : str):
    print(f"\033[36m{texto}\033[0m")

def limpiar():
    print("PRESS ANY KEY")
    msvcrt.getch()
    os.system("cls")


def listar(lista):
    if len(lista)>0:
        for i in range(len(lista)):
            printA(f"{i+1}.-{lista[i][0]} | {lista[i][1]}")
    else:
        printR("NO HAY AGENTES REGISTRADOS. ")

def guardar(nombre,autor,duracion):
    if len(nombre)>=3:
        centinela = False
        for a in datos:
            if a[0]==nombre:
                centinela=True
        if centinela == False :       
            datos.append([nombre,autor,duracion])
            printV("VIDEO GUARDADO CORRECTAMENTE")
def listar():
    if len(datos)>0:
        for i in range(len(datos)):
            printA(f"{i+1}.-Nombre Video : {datos[i][0]} | Nombre Autor : {datos[i][1]} | Duracion Video : {datos[i][2]}SEGUNDOS")
    else:
        printR("NO HAY VIDEOS REGISTRADOS. ")

def eliminar(nombre):
    for i in datos:
        if i[0] == nombre:
          datos.remove(i)
          printV("VIDEO ELIMINADO")
          return True
    printR("VIDEO NO ENCONTRADO")
    return False

def modificar(nombre):
    for i in range(len(datos)):
        if datos[i][0] == nombre:
            nuevo_nombre = input("INGRESE EL NUEVO NOMBRE DEL VIDEO : ").upper()
            if len(nuevo_nombre) >= 3:
                datos[i][0] = nuevo_nombre
                printV("EL NOMBRE DEL VIDEO HA SIDO MODIFICADO.")
                printV("═══════════════════════════════════════")
            else:
                print("EL NOMBRE NO HA SIDO MODIFICADO.")

            printA("DESEA MODIFICAR EL NOMBRE DEL AUTOR [S/N] : ")
            opc2 = input("SELECCIONE : ").upper()
            if opc2 == "S":
                nuevo_autor = input("INGRESE EL NOMBRE DEL AUTOR : ").upper()
                if len(nuevo_autor) >= 3:
                    datos[i][1] = nuevo_autor
                    printV("EL AUTOR HA SIDO MODIFICADO.")
                else:
                    printR("EL AUTOR NO HA SIDO MODIFICADO.")
            printR("═══════════════════════════════")
            
            printA("DESEA MODIFICAR LA DURACION DEL VIDEO [S/N] : ")
            opc3 = input("SELECCIONE : ").upper()
            if opc3 == "S":
                nueva_duracion = int(input("INGRESE LA DURACION DEL VIDEO [SEGUNDOS] :"))
                if nueva_duracion > 0:
                    datos[i][2] = nueva_duracion
                    printV("DURACION MODIFICADA CORRECTAMENTE")
                    printV("═════════════════════════════════")
                else:
                    printR("DURACION NO VALIDA.")
                    printR("═══════════════════")
            
            return True

    printR("NO SE HA PODIDO MODIFICAR EL VIDEO. [X]")
    return False