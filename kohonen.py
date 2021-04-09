from math import exp, cos, sqrt
from numpy import dot, transpose, array
from numpy.linalg import norm
# Vectores normalizados
u1 = array([1, -1, 0, 2, 1])/ sqrt(7)
u2 = array([0, 1, -1, 1, 1]) / 2
u3 = array([1, 1, 2, 0, -1]) / sqrt(7)
uin = array([0, 1, 1, -1, 0])/ sqrt(3)
#Se calcula el producto punto del vector de entrada y cada una de las neuronas, 
# para posteriormente obtener el coseno, es decir, la distancia, y así determinar 
# cuál es la neurona mas cercana a la entrada uin
distancia_u1_uin = cos(dot(u1, uin))
distancia_u2_uin = cos(dot(u2, uin))
distancia_u3_uin = cos(dot(u3, uin))
# print(f'Dist a n1  {distancia_u1_uin} . Dist a n2  {distancia_u2_uin}. Dist a n3 {distancia_u3_uin} ')

# Actualizacion de pesos de la neurona ganadora
# Wk(t+1) = n2 + alfa x / norma(n2 + alfa x )
n2 = array([0, 1, -1, 1, 1])
x =  array([0, 1, 1, -1, 0])
alfa = 0.4 # learning rate
v = n2 + alfa * x
wkt1 = v / norm(v)
print(wkt1)