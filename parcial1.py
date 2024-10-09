
pacientes = []


#primeras funciones: validaciones

def validar_nombre(nombre_completo : str) -> bool:
    """
    valida que el valor del nombre cumpla con caracteres alfabeticos
    nombre_completo = nombre completo del paciente
    """
    valido = True
    while not(valido): 
        while nombre_completo != "": # or nombre_completo == None:
            valido = True
            nombre_completo = input("error! ingrese un valor valido:").capitalize()
    return nombre_completo

def validar_edad(edad: int) -> int:
    """
    verifica que la persona no este poniendo una edad falsa
    edad = edad del paciente
    """
    while edad > 120 or edad < 0:        
        edad = int(input("Edad NO VALIDA. Ingrese una edad valida (entre 1 y 120):): "))
        return edad

#segundas funciones: operativas

def cargar_pacientes():
    """solicita al usuario una cantidad elegida de cargas y luego almacena los datos proporcionados en el array de todos los pacientes"""
    id = 0000
    cant = int(input("cuantos pacientes quiere ingresar?: "))
    for i in range(cant):
        nombre_completo = input("ingrese el nombre del paciente: ").capitalize()
        validar_nombre(nombre_completo)
        edad = int(input("ingrese la edad del paciente: "))
        validar_edad(edad)
        sintoma = input("ingrese la enfermedad del paciente: ").upper()
        dias = int(input("ingrese la cantidad de dias de internacion: "))
        id_paciente = id
        id += 1
        pacientes.append([id_paciente, nombre_completo, edad, sintoma, dias])

def mostrar_pacientes(pacientes: list):
    """muestra una lista de pacientes de manera ordenada"""
    for i in pacientes:
                print(f"HC: {i[0]}, NOMBRE: {i[1]}, EDAD: {i[2]}, SINTOMA: {i[3]}, DIAS DE INTERNACION: {i[4]}")

def ord_pacientes(pacientes: list):
    """ordena los pacientes a traves de HC de manera ascendiente con un bubble sort"""
    n = len(pacientes)

    for i in range(n-1):
        for j in range(n-1-i):
            if pacientes[j][0] > pacientes[j+1][0]:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]

def menos_dias_paciente():
    """retorna el paciente con menos dias de internacion"""
    lista_menos_dias = []
    contador_menos_dias = float("inf")
    for i in pacientes:
        if i[4] < contador_menos_dias:
            contador_menos_dias = i[4]
            lista_menos_dias = i
    return lista_menos_dias

def mas_dias_paciente():
    """retorna el paciente con mas dias de internacion"""
    lista_mas_dias = []
    contador_mas_dias = 0
    for i in pacientes:
        if i[4] > contador_mas_dias:
            contador_mas_dias = i[4]
            lista_mas_dias = i
    return lista_mas_dias

def cinco_dias_paciente() -> list:
    """retorna un array con todos los pacientes con mas de 5 dias de internacion"""
    lista_cinco_dias = []
    for i in pacientes:
        if i[4] >= 5:
            lista_cinco_dias.append(i)
    return lista_cinco_dias

def buscar_paciente(pacientes: list, id: int):
    """
    proceso por el cual luego se le proporciona un paciente para ser almacenado en el retorno
    """
    for i in pacientes:
        if i[0] == id:
            return i
    return None

def menu():
    """menu por el cual se imprime las instrucciones y se le permite al usuario entregar un numero"""
    print("-----------------------------------------------------")
    print("sistema de gestion clinica")
    print("1. cargar pacientes")
    print("2. mostrar todos los pacientes")
    print("3. buscar pacientes por numero de historia clinica")
    print("4. ordenar pacientes por numero de historia clinica")
    print("5. mostrar paciente con mas dias de internacion")
    print("6. mostrar paciente con menos dias de internacion")
    print("7. mostrar pacientes con mas de 5 dias de internacion")
    print("8. promedio de internacion de todos los pacientes")
    print("9. salir")
    eleccion = int(input("ingrese su seleccion: "))
    if eleccion not in range(1,10):
        eleccion = int(input("ingrese un valor dentro de los mostrados: "))
    return eleccion

#bucle while true para poder hacer que el menu se este ejecutando indefinidamente hasta que el usuario decida salir (continuar = false)
continuar = True

while continuar == True:
    
    eleccion = menu()
    #evalua que funcion y proceso ejecutar dependiendo el input del usuario proporcionado
    match eleccion:
        case 1:
            cargar_pacientes()
            
        case 2:
            mostrar_pacientes(pacientes)
            
        case 3:
            buscar = int(input("ingrese el historial clinico del paciente que quiere buscar: "))
            paciente_buscado = buscar_paciente(pacientes, buscar)
            if paciente_buscado:
                print(f"HC: {paciente_buscado[0]}, NOMBRE: {paciente_buscado[1]}, EDAD: {paciente_buscado[2]}, SINTOMA: {paciente_buscado[3]}, DIAS DE INTERNACION: {paciente_buscado[4]}")
            else:
                print("Error! No existe ese paciente.")

        case 4:
            ord_pacientes(pacientes)
            mostrar_pacientes(pacientes)
            
        case 5:
            mas_dias = mas_dias_paciente()
            if mas_dias:
                print(f"HC: {mas_dias[0]}, NOMBRE: {mas_dias[1]}, EDAD: {mas_dias[2]}, SINTOMA: {mas_dias[3]}, DIAS DE INTERNACION: {mas_dias[4]}")
            else:
                print("error. ingrese un usuario")
                
        case 6:
            menos_dias = menos_dias_paciente()
            if menos_dias:
                print(f"HC: {menos_dias[0]}, NOMBRE: {menos_dias[1]}, EDAD: {menos_dias[2]}, SINTOMA: {menos_dias[3]}, DIAS DE INTERNACION: {menos_dias[4]}")
            else:
                print("error. ingrese un usuario")
                
        case 7:
            cinco_dias = cinco_dias_paciente()
            if cinco_dias:
                mostrar_pacientes(cinco_dias)
            else:
                print("error. ingrese un usuario")
                
        case 8:
            cantidad_pacientes = len(pacientes)
            total_dias_internados = 0
            for i in pacientes:
                total_dias_internados += i[4]
            promedio_dias = total_dias_internados / cantidad_pacientes
            print(f"El promedio entre todos los pacientes de dias internados es de {promedio_dias}")  
            
        case 9:
            print("Hasta luego!")
            continuar = False
    