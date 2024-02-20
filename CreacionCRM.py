import time

import _mysql_connector
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crmpython",
    port="3306"
)



def mostrar_menu():
    print("1. Añadir Cliente")
    print("2. Eliminar Cliente")
    print("3. Modificar Cliente")
    print("4. Mostrar Cliente")
    print("5. Llamar")
    print("6. Mostrar la Ficha del Cliente")
    print("7. Salir")

def agregarCliente():
    cursor = conexion.cursor()

    # Solicita información al usuario
    nombreApellidos = input("Introduzca el nombre y apellidos del cliente: ")
    DNI = input("Introduzca el DNI del cliente: ")
    direccion = input("Introduzca la dirección del cliente: ")

    # Lista de productos predefinidos
    lista_productos = ["Fibra", "Movil", "TV", "Paquete Completo"]

    # Muestra la lista de productos al usuario
    print("Seleccione el producto: ")
    print("")  # para agregar salto de linea
    for i, producto in enumerate(lista_productos, start=1):
        print(f"{i}. {producto}")

    # Pide al usuario que seleccione un producto
    opcion_producto = int(input("Ingrese el número de producto deseado: "))

    # Valida la selección del usuario
    if 1 <= opcion_producto <= len(lista_productos):
        producto = lista_productos[opcion_producto - 1]
    else:
        print("Opción no válida, Seleccionando 'Otros' por defecto")
        producto = "Otros"

    # Consulta SQL para Insertar los datos
    consulta = "INSERT INTO clientes(nombreApellidos, DNI, direccion, producto) VALUES (%s, %s, %s, %s)"

    # Datos del cliente
    datos_cliente = (nombreApellidos, DNI, direccion, producto)

    cursor.execute(consulta, datos_cliente)  # Ejecutar la consulta
    conexion.commit()  # Guarda los datos en la base de datos

    print("")  # para agregar salto de linea
    print("Cliente " + nombreApellidos + " m baagregado con éxito.")
    print("")  # para agregar salto de linea

def eliminarCliente():
    cursor = conexion.cursor()

    # Muestra opciones para eliminar.
    print("¿Cómo quiere eliminar al Cliente?")
    print("1. Por ID")
    print("2. Por Nombre y Apellido")
    print("3. Por DNI")
    print("4. Por Direccion")
    print("5. No eliminar ningun Cliente")

    opcion_eliminar = input("Introduzca el número de la opción deseada: ")
    print("")  # para agregar salto de línea

    if opcion_eliminar == "5":
        print("No se eliminará ningún Cliente")
        print("")  # para agregar salto de línea
        return

    if opcion_eliminar not in ["1", "2", "3", "4"]:
        print("Opción no válida.")
        return

    if opcion_eliminar == "1":  # eliminar por id
        id_cliente = input("Ingrese el ID del cliente que quiere eliminar: ")
        consulta = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(consulta, (id_cliente,))
        print("Cliente eliminado con éxito.")
        print("")  # para agregar salto de línea
    elif opcion_eliminar == "2":  # eliminar por nombre y apellido
        nombreApellido = input("Introduzca el nombre y apellido del cliente que quiere eliminar: ")
        consulta = "DELETE FROM clientes WHERE nombreApellidos = %s"
        cursor.execute(consulta, (nombreApellido,))
        print("Cliente eliminado con éxito.")
        print("")  # para agregar salto de línea
    elif opcion_eliminar == "3":  # eliminar por el dni
        dni_cliente = input("Introduzca el DNI del usuario que quiere eliminar: ")
        consulta = "DELETE FROM clientes WHERE DNI = %s"
        cursor.execute(consulta, (dni_cliente,))
        print("Cliente eliminado con éxito.")
        print("")  # para agregar salto de línea
    elif opcion_eliminar == "4":  # eliminar por dirección
        direccion_cliente = input("Introduzca la dirección del cliente que quieras eliminar: ")
        consulta = "DELETE FROM clientes WHERE direccion = %s"
        cursor.execute(consulta, (direccion_cliente,))
        print("Cliente eliminado con éxito.")
        print("")  # para agregar salto de línea

    # Guarda los cambios
    conexion.commit()

def modificarCliente():
    cursor = conexion.cursor()
    id_cliente = input("Ingresa el ID del cliente que quieres modificar: ")

    # Consulta para comprobar que el id existe
    consulta_validar = "SELECT * FROM clientes WHERE id=%s"
    cursor.execute(consulta_validar, (id_cliente,))
    if not cursor.fetchone():
        print("El Cliente no se ha encontrado")
        return

    print("¿Qué campo quieres modificar del cliente?")
    print("1. Nombre y Apellido")
    print("2. DNI")
    print("3. Dirección")
    print("4. Producto")
    print("5. Todos los campos")

    opcion_modificar = input("Introduce el número del campo que deseas modificar: ")
    print("")  # salto de línea

    if opcion_modificar not in ("1", "2", "3", "4", "5"):
        print("Opción no válida")
        return

    if opcion_modificar == "1":
        nuevo_nombre_apellido = input("Ingresa el nuevo Nombre y Apellido del cliente: ")
        consulta_modificar = "UPDATE clientes SET nombreApellidos = %s WHERE id = %s"
        datos_nuevos = (nuevo_nombre_apellido, id_cliente)

    elif opcion_modificar == "2":
        nuevo_dni = input("Ingresa el nuevo DNI del cliente: ")
        consulta_modificar = "UPDATE clientes SET DNI = %s WHERE id = %s"
        datos_nuevos = (nuevo_dni, id_cliente)

    elif opcion_modificar == "3":
        nueva_direccion = input("Ingresa la nueva dirección del cliente: ")
        consulta_modificar = "UPDATE clientes SET direccion = %s WHERE id = %s"
        datos_nuevos = (nueva_direccion, id_cliente)

    elif opcion_modificar == "4":
        # Lista de productos predefinidos
        lista_productos = ["Fibra", "Movil", "TV", "Paquete Completo"]
        # Muestra la lista de productos al usuario
        print("Selecciona el nuevo producto: ")
        for i, producto in enumerate(lista_productos, start=1):
            print(f"{i}. {producto}")
        opcion_producto = int(input("Ingresa el número de producto deseado: "))
        if 1 <= opcion_producto <= len(lista_productos):
            nuevo_producto = lista_productos[opcion_producto - 1]
        else:
            print("Opción no válida, seleccionando 'Otros' por defecto.")
            nuevo_producto = "Otros"
        consulta_modificar = "UPDATE clientes SET producto = %s WHERE id = %s"
        datos_nuevos = (nuevo_producto, id_cliente)

    elif opcion_modificar == "5":
        nuevo_nombre = input("Ingresa el nuevo nombre y apellido del cliente: ")
        nuevo_dni = input("Ingresa el nuevo DNI del cliente: ")
        nueva_direccion = input("Ingresa la nueva dirección del cliente: ")
        # Lista de productos predefinidos
        lista_productos = ["Fibra", "Movil", "TV", "Paquete Completo"]
        # Muestrala lista de productos al usuario
        print("Selecciona el nuevo producto: ")
        for i, producto in enumerate(lista_productos, start=1):
            print(f"{i}. {producto}")
        opcion_producto = int(input("Ingresa el número de producto deseado: "))
        if 1 <= opcion_producto <= len(lista_productos):
            nuevo_producto = lista_productos[opcion_producto - 1]
        else:
            print("Opción no válida, seleccionando 'Otros' por defecto.")
            nuevo_producto = "Otros"
        consulta_modificar = "UPDATE clientes SET nombreApellidos = %s, DNI = %s, direccion = %s, producto = %s WHERE id = %s"
        datos_nuevos = (nuevo_nombre, nuevo_dni, nueva_direccion, nuevo_producto, id_cliente)

    cursor.execute(consulta_modificar, datos_nuevos)
    conexion.commit()

    print("----------------------------")
    print("Cliente modificado con éxito")
    print("----------------------------")

    cursor.close()

def mostrarCliente():
    cursor = conexion.cursor()

    # Muestra las opciones para mostrar cliente
    print("¿Cómo quiere mostrar al Cliente?")
    print("1. Por ID")
    print("2. Por Nombre y Apellido")
    print("3. Por DNI")
    print("4. Por Dirección")
    print("5. Por Producto")

    opcion_mostrar = input("Introduzca el número de la opción deseada: ")
    print("")  # para agregar salto de línea

    if opcion_mostrar not in ["1", "2", "3", "4","5"]:
        print("Opción no válida.")
        return

    if opcion_mostrar == "1":  # muestra por id
        id_cliente = input("Ingrese el ID del cliente que quiere mostrar: ")
        consulta = "SELECT * FROM clientes WHERE id = %s"
        cursor.execute(consulta, (id_cliente,))
        print("")  # para agregar salto de línea
    elif opcion_mostrar == "2":  # muestra por nombre y apellido
        nombreApellido = input("Introduzca el nombre y apellido del cliente que quiere mostrar: ")
        consulta = "SELECT * FROM clientes WHERE nombreApellidos = %s"
        cursor.execute(consulta, (nombreApellido,))
        print("")  # para agregar salto de línea
        print("Mostrando todos los clientes cuyo nombre sea: " + nombreApellido + "...")
        print("")
    elif opcion_mostrar == "3":  # muestra por el dni
        dni_cliente = input("Introduzca el DNI del usuario que quiere mostrar: ")
        consulta = "SELECT * FROM clientes WHERE DNI = %s"
        cursor.execute(consulta, (dni_cliente,))
        print("")  # para agregar salto de línea
        print("Mostrando todos los clientes cuyo DNI sea: " + dni_cliente + "...")
        print("")
    elif opcion_mostrar == "4":  # muestra por dirección
        direccion_cliente = input("Introduzca la dirección del cliente que quiere mostrar: ")
        consulta = "SELECT * FROM clientes WHERE direccion = %s"
        cursor.execute(consulta, (direccion_cliente,))
        print("")  # para agregar salto de línea
        print("Mostrando todos los clientes cuya direccion sea: " + direccion_cliente + "...")
        print("")
    elif opcion_mostrar == "5": #muestra por producto
        producto_cliente =input("Introduzca el nombre del producto que quiera eliminar, puede ser Fibra, Movil, TV o Paquete Completo: ")
        consulta = "SELECT * FROM clientes WHERE producto = %s"
        cursor.execute(consulta,(producto_cliente,))
        print("")
        print("Mostrando todos los clientes cuyo producto sea: " + producto_cliente + "...")
        print("")


    # Obtiene los resultados de la consulta
    resultados = cursor.fetchall()
    time.sleep(3)
    if not resultados:
        print("No se encontraron resultados.")
        print("")  # para agregar salto de línea
    else:
        # Muestra la información del cliente
        for cliente in resultados:
            print("DNI:", cliente[0])
            print("Nombre y Apellido:", cliente[1])
            print("DNI:", cliente[2])
            print("Direccion:", cliente[3])
            print("Producto:", cliente[4])
            print("---------------------")

    # Cerramos el cursor
    cursor.close()



def llamada():
    cursor = conexion.cursor()

    dni_Cliente = input("Introduzca el DNI para hacer la llamada: ")
    consulta = "SELECT * FROM clientes WHERE DNI = %s"
    cursor.execute(consulta, (dni_Cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print("No se ha encontrado cliente con DNI: " + dni_Cliente + ".")
    else:
        incidencia = input("Introduzca la Incidencia: ")
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        consulta2 = "INSERT INTO llamadas (dni_cliente, consulta, fecha) VALUES (%s, %s, %s)"
        valores_insertar = (dni_Cliente, incidencia, fecha_actual)
        cursor.execute(consulta2, valores_insertar)
        conexion.commit()

        print("La llamada se ha realizado con éxito.")
    cursor.close()

def mostrarFicha():
    cursor = conexion.cursor()
    dni_cliente = input("Ingrese el DNI del cliente para ver su ficha: ")
    consulta = "SELECT * FROM clientes WHERE DNI = %s"
    cursor.execute(consulta, (dni_cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print("El cliente con DNI " + dni_cliente + " no existe.")
    else:
        print("------------------------")
        print("Ficha Cliente: ")
        print("Nombre y Apellidos: ", cliente[1])
        print("DNI: ", cliente[2])

        consulta2 = "SELECT consulta, fecha FROM llamadas WHERE dni_cliente = %s"
        cursor.execute(consulta2, (dni_cliente,))
        llamadas = cursor.fetchall()

        if llamadas:
            print("")
            print("Consultas realizadas: ")
            for llamada in llamadas:
                print(f"- Consulta: {llamada[0]}, Fecha: {llamada[1]}")
        else:
            print("")
            print("Este cliente no ha realizado ninguna llamada")
    cursor.close()


def menu():
    while True:
        mostrar_menu()
        seleccion = input("Seleccione una opción ")
        print("")#para agregar salto de linea
        if seleccion == "1":
            agregarCliente()
        elif seleccion == "2":
            eliminarCliente()
        elif seleccion == "3":
            modificarCliente()
        elif seleccion == "4":
            mostrarCliente()
        elif seleccion == "5":
            llamada()
        elif seleccion == "6":
            mostrarFicha()
        elif seleccion == "7":
            print("Saliendo del menú. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            print("")
menu()