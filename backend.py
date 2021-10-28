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


def comprobarEntrada(elemento):
    print(exprecionConcatenada)
    valdator = re.compile(exprecionConcatenada)
    match =valdator.match(elemento)
    try:
        valida = match.group()==elemento
    except (TypeError, AttributeError):
        valida = False
    return  valida

print(comprobarEntrada("H"))