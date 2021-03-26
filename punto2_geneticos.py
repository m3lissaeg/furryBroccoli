import random
def generar_poblacion(numero_individuos):
    salida = []
    i = 0
    while i <= numero_individuos:
        alto = random.randint(1,5)
        ancho = random.randint(1,5)
        cromo = (alto,ancho)
        salida.append(cromo)
        i += 1
    return salida

def generar_matriz(individuos):
    matriz = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]

    for individuo in individuos:
        pos_vertical = 0
        while(pos_vertical >= 0):
            if (0 in matriz[pos_vertical]):
                primer_cero = matriz[pos_vertical].index(0)
                try:
                    primer_uno = matriz[pos_vertical].index(1)
                except:
                    primer_uno = 0
                if(10 - primer_cero >= individuo[1]):
                    if(primer_cero > primer_uno):
                        print(f"el indivudo {individuo} entra las pos son ({primer_cero},{pos_vertical})")
                        i = 0 
                        j = 0
                        while i < individuo[0]:
                            j = 0
                            while j < individuo[1]:
                                    
                                matriz[pos_vertical+i][primer_cero+j] = 1
                                j = j + 1
                            i = i + 1 
                        imprimir_matriz(matriz)
                        print("\n")
                        break
                    elif(primer_uno-primer_cero < individuo[1]):
                        print(f"el indivudo {individuo} entra las pos son ({primer_cero},{pos_vertical})")
                        i = 0 
                        j = 0
                        while i < individuo[0]:
                            j = 0
                            while j < individuo[1]:
                                    
                                matriz[pos_vertical+i][primer_cero+j] = 1
                                j = j + 1
                            i = i + 1 
                        imprimir_matriz(matriz)
                        print("\n")
                        break
                    else:
                        return matriz
                else:
                    pos_vertical = pos_vertical+1   
            else:
                pos_vertical = pos_vertical+1

    return matriz

def imprimir_matriz(matriz):
    for elemento in matriz:
        print(elemento)

a = [(2,2),(3,2),(3,6),(2,3)]
matriz = generar_matriz(a)

matriz = [
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [0,0,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]