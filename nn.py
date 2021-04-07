from math import exp
from numpy import dot, transpose, array
# A continuación se define la matriz w, que es la matriz de los pesos sinapticos de la capa oculta de 3 neuronas
w  =array( [
    [-0.5 , 0.2],
    [ 0.3 ,-0.1],
    [-0.2,  0.6]
])
# El vector b representa los pesos de la neurona de la capa de salida 
b = array([1, -1, 1])

# Se define la función de activación sigmoidal
def sigmoid(x):
    return  1/(1+exp(-x) ) 

if  __name__ == "__main__":
    x = array([1, -1])
    # A continuación se aplica el producto punto entre cada una de las filas de la 
    # matriz w (los pesos sinapticos) y el vector de entrada x
    # Se aplica también la función de activación sigmoid. 
    
    hiddenLayerOutput0 = sigmoid( dot(w[0] , x.transpose()) )
    hiddenLayerOutput1 = sigmoid( dot(w[1] , x.transpose()) )
    hiddenLayerOutput2 = sigmoid( dot(w[2] , x.transpose()) )
    hiddenLayerOutputArray = array([hiddenLayerOutput0, hiddenLayerOutput1, hiddenLayerOutput2])
    # print (f'{hiddenLayerOutput0, hiddenLayerOutput1, hiddenLayerOutput2}')

    # Este resultado representa la entrada que debe multiplicarse con los pesos B_i de la capa de salida
    outputLayer = sigmoid( dot( hiddenLayerOutputArray, b.transpose() ) )

    # Ya que el valor esperado es 0 y el valor que predice la red es 1, se aplicará el descenso gradiente en uno de los pesos 
    # (el que se considera que más influye en el error: w[1][1])
    y = 0
    residual = ( outputLayer - y )**2
    GLossW = 2 * residual * hiddenLayerOutput1
    # Tamaño de paso estará definido con un valor de 0.3
    learningRate = 0.6
    # El nuevo peso
    newW = w[1][1] - learningRate * GLossW
    # Se modifica la matriz de los pesos
    w[1][1] = newW
    # Se realiza nuevamente el proceso para clasificar el punto de entrada
    hiddenLayerOutputArray = array([ sigmoid( dot(w[0] , x.transpose()) )  ,  sigmoid( dot(w[1] , x.transpose()) ),  sigmoid( dot(w[2] , x.transpose()) )  ])    
    # Este resultado representa la entrada que debe multiplicarse con los pesos B_i de la capa de salida
    outputLayer = sigmoid( dot( hiddenLayerOutputArray, b.transpose() ) )
    print('Matriz con el peso modificado:')
    print(w)
    print('Nuevo valor para y gorrito:')
    print(outputLayer)
