import misfunciones2 as m


while True:
    m.limpiar()
    m.printM("SISTEMA DE VIDEOS EN YOUTUBE")
    m.printM("════════════════════════════")
    print("1) REGISTRAR VIDEO")
    print("2) MODIFICAR VIDEO")
    print("3) ELIMINAR VIDEO")
    print("4) LISTAR VIDEO")
    print("0) SALIR")
    m.printM("════════════════════════════")
    opc = input("SELECCIONE : ")

    if opc == "0":
        m.printM("SALIENDO...")
        break
    elif opc == "1":
        m.printA("REGISTRAR VIDEO")
        m.printA("═══════════════")
        nombre = input("INGRESE EL NOMBRE DEL VIDEO : ").upper()
        autor = input("INGRESE EL NOMBRE DEL AUTOR : ").upper()
        duracion = int(input("INGRESE LA DURACION DEL VIDEO EN [SEGUNDOS] : "))
        if len(nombre)>=3 and len(autor)>=3 and duracion>=1:
            m.guardar(nombre,autor,duracion)
        else:
            m.printR("LOS DATOS INGRESADOS NO SON VALIDOS [X]")

    elif opc == "2":
        m.printA("MODIFICAR REGISTRO")
        m.printA("══════════════════")
        nombre = input("INGRESE EL NOMBRE DEL VIDEO A MODIFICAR : ").upper()
        m.modificar(nombre)
    elif opc == "3":
        m.printA("ELIMINAR REGISTRO")
        m.printA("═════════════════")
        nombre = input("INGRESE EL NOMBRE DEL VIDEO A ELIMINAR : ").upper()
        m.eliminar(nombre)
    elif opc == "4":
        m.printA("LISTAR VIDEOS")
        m.printA("═════════════")
        m.listar()
    else:
        m.printR("OPCION NO VALIDA [X]")


