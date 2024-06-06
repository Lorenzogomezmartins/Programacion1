def crear_empleado(ID: int, DNI: int, Salario: int, Nombre: str, Apellido: str, Puesto: str) -> dict:
    diccionario = {
        "ID" : ID,
        "DNI" : DNI,
        "Salario" : Salario,
        "Nombre" : Nombre,
        "Apellido" : Apellido,
        "Puesto" : Puesto
    }
    return diccionario


def validar(lista_empleados: list)-> None:
    ID = len(lista_empleados) + 1
    while len(lista_empleados) < 20:
        
        Nombre = input("Ingrese su nombre: ").capitalize()
        while len(Nombre) > 20 or not Nombre.isalpha():
            Nombre = input("ERROR, ingrese un nombre válido: ").capitalize()
        Apellido = input("Ingrese su apellido: ").capitalize()
        while len(Apellido) > 20 or not Apellido.isalpha():
            Apellido = input("Error, ingrese un apellido válido: ").capitalize()
        DNI = int(input("Ingrese su DNI: "))
        while DNI <=  5000000 or DNI >=  99999999:
            DNI = int(input("ERROR, ingrese un DNI valido: "))
        Salario = int(input("Ingrese su salario: "))
        while Salario <= 234315:
            Salario = int(input("Error, ingrese un salario valido: "))
        Puesto = input("Ingrese su puesto: ").capitalize()
        while Puesto != "Gerente" and Puesto != "Supervisor" and Puesto != "Analista" and Puesto != "Encargado" and Puesto != "Asistente":
            Puesto = input("Error, ingrese un puesto correcto: ").capitalize
        
        diccionario_empleado = crear_empleado(ID, DNI, Salario, Nombre, Apellido, Puesto)
        lista_empleados.append(diccionario_empleado)
        ID += 1
        
        if len(lista_empleados) >= 20:
            print("Se ha alcanzado el límite de empleados.")
            break
        
        continuar = input("¿Desea ingresar otro empleado? (si/no): ")
        if continuar != 'si':
            break