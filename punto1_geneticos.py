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
    matriz = [   
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [1,0,0,0]
    ]
    i = 3
    j = 0
    for letra in individuo:
        if letra == "U":
            if i -1 >= 0:
                if matriz[i-1][j] == 0:
                    matriz[i-1][j] = 1
                    i = i -1
                else:
                    break
            else:
                continue
        elif letra == "D":
            try:
                if matriz[i+1][j] == 0:
                    matriz[i+1][j] = 1
                    i = i + 1
                else:
                    break
            except:
                continue
        elif letra == "L":
            if j-1 >= 0:
                if matriz[i][j-1] == 0:
                    matriz[i][j-1] = 1
                    j = j - 1
                else:
                    break
            else:
                continue
        elif letra == "R":
            try:
                if matriz[i][j+1] == 0:
                    matriz[i][j+1] = 1
                    j = j + 1
                else:
                    break
            except:
                continue
    return matriz

def contar_ceros(matriz):
    conteo = 0
    for fila in matriz:
        for columna in fila:
            if columna == 0:
                conteo += 1
    return conteo


def adaptados(poblacion,n_ceros):
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
        if individuo["n_ceros"] < 16-n_ceros:
            adaptados.append(individuo["gen"])
    return adaptados

def reproducir(poblacion):
    padre = random.choice(poblacion)
    madre = random.choice(poblacion)
    hijo = madre[:int(len(madre)/2)] + padre[int(len(padre)/2):]
    return hijo

def factor_mutacion(individuo):
    salida = None
    dado = random.random()
    vocabulario = ['U','D','L','R']
    if dado <= 0.25:
        pos = random.randint(0,16)
        try:
            vocabulario.remove(individuo[pos])
        except:
            pass
        salida = individuo[:pos] + random.choice(vocabulario) + individuo[pos+1:]
        return salida
    else:
        return individuo

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

generaciones = 13
i = 1
poblacion = generar_poblacion(10000)
while i <= generaciones:
    poblacion = adaptados(poblacion,i)
    poblacion.append(reproducir(poblacion))
    for individuo in poblacion:
        individuo = factor_mutacion(individuo)
    i += 1
print(poblacion)