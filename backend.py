import re

exprecionA = "(A(s|i|r|g|u|t|e|m){0,1})|"
exprecionH = "(H(e|o|f|g){0,1})|"
exprecionL = "(L(i|a|v|r)|)"
exprecionB = "(B(e|r|a|i|k|h){0,1})|"
exprecionC = "(C(i|a|r|o|d|u|s|e|f|m|n){0,1})|"
exprecionN = "(N(e|a|i|b|d|p|o|h){0,1})|"
exprecionO = "(O(s|g){0,1})|"
exprecionF = "(F(e|m|t|r|l){0,1})|"
exprecionM = "(M(g|n|o|d|t|c))|"
exprecionS = "(S(i|c|e|r|n|b|m|g){0,1})|"
exprecionP = "(P(d|r|m|t|b|o|a|u){0,1})|"
exprecionK = "(K(r))|"
exprecionT = "(T(i|c|e|b|m|a|l|h|s))|"
exprecionV = "(V)|"
exprecionZ = "(Z(n|r))|"
exprecionG = "(G(a|e|d))|"
exprecionR = "(R(b|u|h|e|n|a|g|f))|"
exprecionY = "(Y(b){0,1})|"
exprecionI = "(I(n|r){0,1})|"
exprecionEspecial = "(W|U|Hs|Xe)|"
exprecionD = "(D(y|b|s))|"
exprecionE = "(E(u|r|s))"

exprecionConcatenada = exprecionA+exprecionH+exprecionL+exprecionB+exprecionC+exprecionN+exprecionO+exprecionF+exprecionM+exprecionS+exprecionP+exprecionK+exprecionT+exprecionV+exprecionZ+exprecionG+exprecionR+exprecionY+exprecionI+exprecionEspecial+exprecionD+exprecionE

nombresElementos = [
    "Hidrógeno","Helio","Litio","Berilio","Boro","Carbono","Nitrógeno","Oxígeno","Fluorita","Neón","Sodio","Magnesio","Aluminio",
    "Silicio","Fósforo","Azufre","Cloro","Argón","Potasio","Calcio","Escandió","Titanio","Vanadio","Cromo","Manganeso","Hierro","Cobalto",
    "Níquel","Cobre","Cinc","Galio","Germanio","Arsénico","Selenio","Bromo","Criptón","Rubidio","Estroncion","Itrio","Circón","Niobio",
    "Molibdeno","Tecnecio","Rutenio","Rodio","Paladio","Plata","Cadmio","Indio","Estaño","Antimonio","Telurio","Yodo","Xenón","Cesio",
    "Bario","Lantano","Cerio","Praseodimio","Neodimoio","Prometio","Samario","Europio","Gadolilnio","Terbio","Disprosio","Holmio","Erbio",
    "Tulio","Iterbio","Lutecio","Hafnio","Tantalio","Tungsteno","Renio","Osmio","Irisio","Platino","oro","Mercurio","Talio","Plomo",
    "Bismuto","Polomio","Astatina","Radón","Francio","Radio","Actinio","Torio","Protactinio","Uranio","Neptunio","Plutonio","Americio",
    "Curio","Berkelio","Californio","Einstenio","Fermio","Mendelevio","Nobelio","Laurencio","Rutherfordio","Dubnio","Seaborgio","Bohrio",
    "Hasio","Meitnerio","Darmstatio","Roentgenio","Copérnico","Nihonio","Flerovio","Moscovio","Livermorio","Teneso","Oganesón"]


def obtenerSimbolos():
    simbolosElementos = []
    f = open("./resources/Elementos.txt", "r",encoding="utf8")
    lineas = f.readlines()
    f.close()
    contador = 13
    for i in range(len(lineas)):
        if((contador-1)%12 == 0):
           simbolosElementos.append(lineas[i].replace("\n",""))
        contador += 1
    return simbolosElementos

        


def comprobarEntrada(elemento):
    valdator = re.compile(exprecionConcatenada)
    match =valdator.match(elemento)
    try:
        valida = match.group()==elemento
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobadorRe(er,cadena):
    valdator = re.compile(er)
    match =valdator.search(cadena)
    try:
        if (match!=None):
            valida = True
        else:
            valida = False
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobarEntradaNombre(elemento):
    if(nombresElementos.count(elemento)>0):
        return True
    return False

def sugerenciasNombres(elemento):
    listaCoincidenciasNombre = []
    for nombre in nombresElementos:
        if(comprobadorRe(elemento,nombre)):
            listaCoincidenciasNombre.append(nombre)
    return listaCoincidenciasNombre

def sugerenciasElemento(elemento):
    listaSimbolos = obtenerSimbolos()
    print(listaSimbolos)
    listaConincidenciaElemento = []
    for simbolos in listaSimbolos:
        if(simbolos.find(elemento)!=-1):
            listaConincidenciaElemento.append(simbolos)
    return listaConincidenciaElemento

def cambiarNombreSimbolo(nombre):
    listaSimbolos = obtenerSimbolos()
    index = nombresElementos.index(nombre)
    return listaSimbolos[index]

