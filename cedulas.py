def digitoVerificador(numero):
    suma = 0
    vec = [8, 1, 2, 3, 4, 7, 6]
    for i in range(0, 7):
        suma += int(numero[i]) * vec[i]
    return suma % 10

def crearDiccionarioCedulas(nombre):
    try:
        cedulas = open(nombre, 'x')
    except FileExistsError:
        print('Error: el archivo %s ya existe' % nombre)
        return
    except Exception:
        print('Error al generar el diccionario')
        return

    for x in range(6000000, -1, -1):
        num = str(x).zfill(7)
        print(num + str(digitoVerificador(num)), file=cedulas)

    cedulas.close()

crearDiccionarioCedulas('cedulas.txt')
