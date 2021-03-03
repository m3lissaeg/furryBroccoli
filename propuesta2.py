import random
def generar_poblacion(numero_individuos):
    alphabet='UDLR'
    salida = []
    i = 0
    while i <= numero_individuos:
        cromo = random.choices(alphabet, k=15)
        cromo = " ".join(cromo)
        salida.append(cromo)
        i += 1
    return salida


def generar_matriz(individuo):
    matriz_inicial = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [1,0,0,0]
    ]
    print("matriz inicial: \n",matriz_inicial)
    #pos vertical
    i = 3
    #pos horizontal
    j = 0
    for cromosoma in individuo:
        if cromosoma == "U":
            try:
                if matriz_inicial[i-1][j] == 0:
                    matriz_inicial[i-1][j] = 1
                    i -= 1
                    print("movimiento: U \n",matriz_inicial)
                else:
                    return matriz_inicial
            except:
                print("se va a salir")
                
        elif cromosoma == "D":
            try:
                if matriz_inicial[i+1][j] == 0:
                    matriz_inicial[i+1][j] = 1
                    i += 1
                    print("movimiento: D \n",matriz_inicial)
                else:
                    return matriz_inicial
            except:
                pass
        elif cromosoma == "R":
            try:
                if matriz_inicial[i][j+1] == 0:
                    matriz_inicial[i][j+1] = 1
                    j += 1
                    print("movimiento: R \n",matriz_inicial)
                else:
                    return matriz_inicial
            except:
                pass
        elif cromosoma == "L":
            try:
                if matriz_inicial[i][j-1] == 0:
                    matriz_inicial[i][j-1] = 1
                    j -= 1
                    print("movimiento: L \n",matriz_inicial)
                else:
                    return matriz_inicial
            except:
                pass

    return matriz_inicial

def contar_ceros(matriz):
    conteo = 0
    for fila in matriz:
        for columna in fila:
            if columna == 0:
                conteo += 1
    return conteo


def adaptados(poblacion):
    aux = []
    adaptados = []
    for individuo in poblacion:
        matriz = generar_matriz(individuo)
        individuo_dict = {
            "gen":individuo,
            "matriz":matriz,
            "n_ceros":contar_ceros(matriz)
        }
        aux.append(individuo_dict)
    for individuo in aux:
        if individuo["n_ceros"] <= 10:
            adaptados.append(individuo)
    return adaptados

def reproducir(poblacion):
    padre = random.choice(poblacion)
    madre = random.choice(poblacion)
    hijo = madre[0:int(len(madre)/2)] + padre[int(len(padre)/2):]
    return hijo

def factor_mutacion(individuo):
    salida = None
    dado = random.random()
    vocabulario = ['U','D','L','R']
    if dado <= 0.25:
        pos = random.randint(0,16)
        vocabulario.remove(individuo[pos])
        salida = individuo[:pos] + random.choice(vocabulario) + individuo[pos+1:]
        return salida
    else:
        return individuo



generaciones = 5
i = 1
#poblacion = generar_poblacion(10)
#while i <= generaciones:
#    print("poblacion inicial \n",poblacion,"\n")
#    poblacion = adaptados(poblacion)
#    print("poblacion adaptada \n",poblacion,"\n")
#    poblacion = reproducir(poblacion)
#    for individuo in poblacion:
#        individuo = factor_mutacion(individuo)
#    i += 1
#print(poblacion)
a = generar_matriz("RRRR")

        
