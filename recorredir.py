import os
import tempfile


fichero = os.path.join(tempfile.gettempdir(), "recorredir.txt")


def listadir(dir1):
    files = []
    dires = []
    try:
        contenido = os.listdir(dir1)
    except:
        contenido = []
    if " " in dir1:
        # print("excepto", dir1, "tiene espacios")
        return []
    if (len(contenido) > 59):
        # print("excepto(tiene mas de 59)", dir1, len(contenido))
        return []
    if "$Windows.~WS" in dir1:
        # print("excepto($Windows.~WS)", dir1, len(contenido))
        return []
    # print("24")
    if "$WINDOWS.~BT" in dir1:
        # print("excepto($Windows.~BT)", dir1, len(contenido))
        return []
    for i in contenido:
        if os.path.isfile(os.path.join(dir1, i)):
            files.append(os.path.join(dir1, i))
        else:
            dires.append(os.path.join(dir1, i))
            dires += listadir(os.path.join(dir1, i))
    return dires


def actualiza():
    dires = listadir('c:\\')
    for i in dires:
        # print(i)
        pass
    f = open(fichero, "wt")
    for i in dires:
        f.write(i + "\r")
    f.close()


def busca():
    try:
        f = open(fichero, "r").readlines()
    except:
        return None
    encontrado = None
    lista = []
    repes = 0
    # argv = os.sys.argv
    for i in f:
        if len(argv) > 1 and (argv[1].upper()) in os.path.split(i)[1].upper():
            # print("'" + i.strip() + "'\r")
            # print(i.strip())
            encontrado = i
            lista.append(i.strip())
            repes = repes + 1
    encontrado = None
    if len(lista) > 1:
        cd = os.getcwd()
        for i in range(len(lista)):
            if cd.upper() == lista[i].upper():
                j = (i + 1) % len(lista)
                # print(lista[j])
                encontrado = lista[j]
        if not encontrado:
            encontrado = lista[0]
    elif len(lista) >= 1:
        # print(lista[0])
        encontrado = lista[0]
    # if encontrado:
    #    print(encontrado)
    return encontrado, repes


rescan = False
argv = os.sys.argv
# print(76, argv, len(argv))
if len(argv) == 2 and argv[1]=="-v":
    print(fichero)
if len(argv) == 1:
    argv = [0, "python", "r"]
if (len(argv) > 2):
    if argv[2][0] == 'r':
        rescan = True
encontrado = None
if rescan is False:
    encontrado, repes = busca()
    if encontrado:
        print(encontrado)
if not encontrado:
    actualiza()
    busca()
