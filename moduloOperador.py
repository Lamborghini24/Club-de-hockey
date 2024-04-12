
def juntarListas(ListA, ListB, ListC, ListD):
    ListA = (ListA.split(", "))
    return tuple(zip(ListA, ListB, ListC, ListD))

def getGoleador(tupla):
    maxgol = -1
    for element in tupla:
        if element[1] > maxgol:
            maxgol = element[1]
            max = element
    return max[0], max[1]

def getMasInfluyente(tupla):
    maxProm = -1
    for element in tupla:
        prom = element[1]*1.5+element[2]*1.25+element[3]
        if prom > maxProm:
            maxProm = prom
            masInfluyente = element[0]
    return masInfluyente

def getPromedioGoles(tupla):
    goles=0
    for element in tupla:
        goles = goles + element[1]
    return goles/25

def getPromedioGoleador(tupla):
    return tupla[1]/25