diccionario_planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

diccionario_inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
}


def menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================
          """)

def espacios(texto):
    for i in texto:
        if(i.isspace()):
            return True
    return False
        
def leer_opcion():
    op = int(input("Ingrese una opcion: "))
    return op

def cupos_tipo(plan):
    lista_tmp = []
    suma_tmp = 0
    for i,j in diccionario_planes.items():
        if(j[1] == plan):
            lista_tmp.append(i)
    if (lista_tmp):
        for i in lista_tmp:
            suma_tmp += diccionario_inscripciones.get(i)[1]
        print(f"La cantidad de cupos disponibles para su plan son: {suma_tmp}")
    else:
        print("Ingrese un plan mensual valido...")

def busqueda_precio(p_min, p_max):
    lista_tmp = []
    for i,j in diccionario_inscripciones.items():
        if(j[1] > 0):
            if(j[0] >= p_min and j[0] <= p_max):
                lista_tmp.append(i)
    for i in lista_tmp:
        print(f"Los planes disponibles son: {diccionario_planes.get(i)[0]}--{i}: {diccionario_inscripciones.get(i)[1]} cupos")
        
def buscar_codigo(codigo):
    if(diccionario_inscripciones.get(codigo) == None):
        return False
    else:
        return True

def actualizar_precio(codigo, nuevo_precio):
    if(buscar_codigo(codigo) == False):
        return False
    else:
        diccionario_inscripciones.get(codigo)[0] = nuevo_precio
        return True

### VALIDACIONES OPCION 4
def val_codigo(codigo):
    if(espacios(codigo) or codigo == " " or diccionario_inscripciones.get(codigo) != None):
        return False
    else:
        return True

def val_nombre(nombre):
    if(nombre == " " or nombre.isspace()):
        return False
    else:
        return True

def val_tipo(tipo):
    if(tipo == "mensual" or tipo == "trimestral" or tipo == "anual"):
        return True
    else:
        return False

def val_duracion(numero):
    if(numero > 0 and numero.is_integer() and numero <= 12):
        return True
    else:
        return False

def val_acceso_piscina(texto):
    texto.lower()
    if(texto == "s"):
        return True
    else:
        return False

def val_incluye_clases(texto):
    texto.lower()
    if(texto == "s"):
        return True
    else:
        return False
    
def val_horario(horario):
    if(espacios(horario) or horario == " "):
        return False
    else:
        return True

def val_precio(precio):
    if(precio > 0 and precio.is_integer()):
        return True
    else:
        return False
    
def val_cupos(cupos):
    if(cupos >= 0 and cupos.is_integer()):
        return True
    else:
        return False

def agregar_plan(codigo, nombre, tipo, duracion, acceso_p, incluye_c, horario, precio, cupos):
    lista_planes = [nombre, tipo, duracion, acceso_p, incluye_c, horario]
    lista_inscripciones = [precio, cupos]
    diccionario_inscripciones[codigo] = lista_inscripciones
    diccionario_planes[codigo] = lista_planes

### FIN CASO 4

def eliminar_plan(codigo):
    if(buscar_codigo(codigo) == False):
        return False
    else:
        diccionario_inscripciones.pop(codigo)
        diccionario_planes.pop(codigo)
        return True
    
while True:
    try:
        menu()
        opcion = leer_opcion()
        if (opcion <= 0 or opcion > 6):
            print("Debe seleccionar una opción válida")
            continue
        match opcion:
            case 1:
                tipo_plan = input("Ingrese su tipo de plan: ")
                tipo_plan = tipo_plan.lower()
                
                cupos_tipo(tipo_plan)
            
            case 2:
                min = int(input("Ingrese un precio minimo: "))
                max = int(input("Ingrese un precio maximo: "))
                
                if(min < 0 or max < 0 or min > max):
                    print("Ingrese un rango de precio valido...")
                busqueda_precio(min, max)
            
            case 3:
                resp = ""
                while resp != "n":
                    codigo = input("Ingrese el codigo del plan que se desea asignar: ")
                    precio_a = int(input("Ingrese el nuevo precio: "))

                    codigo.capitalize()
                    if(actualizar_precio(codigo, precio_a) == False):
                        print("El codigo no existe")
                        resp = input("¿Desea actualizar otro precio (s/n)?")
                        resp = resp.lower()
                    else:
                        print("Precio actualizado!")
                        resp = "n"
            
            case 4:
                resp = ""
                while resp != "n":
                    c_ingresado = input("Ingrese el codigo que desea agregar: ")
                    if(val_codigo(c_ingresado) == False):
                        print("[!] Hay un error con el codigo ingresado ")
                        continue
                    n_ingresado = input("Ingrese el nombre del plan que desea ingresar: ")
                    if(val_nombre(n_ingresado) == False):
                        print("[!] Hay un error con el nombre de plan ingresado ")
                        continue
                    t_ingresado = input("Ingrese el tipo del plan que desea ingresar: ")
                    if(val_tipo(t_ingresado) == False):
                        print("[!] Hay un error con el tipo de plan ingresado ")
                        continue
                    d_ingresado = int(input("Ingrese la duracion del plan en meses: "))
                    if(val_duracion(d_ingresado) == False):
                        print("[!] Hay un error con la duracion del plan ingresada ")
                        continue
                    ap_ingresado = input("Ingrese si el plan incluye acceso a piscina (s/n): ")
                    if(ap_ingresado.isalpha() == False):
                        print("[!] La informacion solo puede ser de tipo string (s/n): ")
                        continue
                    ic_ingresado = input("Ingrese si el plan incluye clases grupales (s/n): ")
                    if(ic_ingresado.isalpha() == False):
                        print("[!] La informacion solo puede ser de tipo string (s/n) ")
                        continue
                    h_ingresado = input("Ingrese la franja horaria disponible del plan (puede ser libre): ")
                    if(val_horario(h_ingresado) == False):
                        print("[!] Hay un error con la franja horaria ingresada")
                        continue

                    p_ingresado = int(input("Ingrese el precio para su plan: "))
                    if(val_precio(p_ingresado) == False):
                        print("[!] Hay un error con el precio ingresado ")
                        continue

                    cup_ingresado = int(input("Ingrese la cantidad de cupos de inscripcion disponibles: "))
                    if(val_cupos(cup_ingresado) == False):
                        print("[!] Hay un error con los cupos ingresados ")
                        continue

                    agregar_plan(c_ingresado, n_ingresado, t_ingresado, d_ingresado, ap_ingresado, ic_ingresado, h_ingresado, p_ingresado, c_ingresado)
                    print("Plan Agregado")
                    resp = "n"
                
            case 5:
                cod_ingresado = input("Ingrese el codigo del plan que desea eliminar: ")
                cod_ingresado = cod_ingresado.lower()
                if(eliminar_plan(cod_ingresado) == False):
                    print("[!] El codigo ingresado no existe")
                else:
                    print("Plan eliminado")

            case 6:
                print("Programa finalizado")
                break
    except ValueError:
        print("[!] Debe ingresar valores enteros")
        continue


                        
                    




