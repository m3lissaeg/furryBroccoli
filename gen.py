import numpy as np 
import random

def rideAndPerformance(cromosome):
    # creating a 4X4 Numpy matrix 
    rideMatrix = np.array([[1,0,0,0], 
                           [0,0,0,0], 
                           [0,0,0,0], 
                           [0,0,0,0]]) 
    
    # Ride operation
    #R = posCol += 1         L = posCol -= 1
    #U = posFila+= 1         D = posFila-= 1
    # array[fila][col]

    posFila = 0
    posCol = 0
    visit = 0
    for l in cromosome:
        if l == 'R':
            # Validate if the movement doesnt get out the matrix
            if posCol < 3:
                # Make movement to the right
                posCol+=1
                rideMatrix[posFila][posCol]+=1
                print('Right')
                # Check if the position has been visited before
                if  rideMatrix[posFila][posCol] > 1:
                    visit +=1
                else:
                    pass
            else:
                #just stay in the same position, waiting for the next movement in the cromo
                pass
                # print('Im not doing it :p')

        elif l == 'L':
            # Validate if the movement doesnt get out the matrix
            if posCol > 0:
                # Make movement to the left
                posCol-=1
                rideMatrix[posFila][posCol]+=1
                print('Left')
                # Check if the position has been visited before
                if  rideMatrix[posFila][posCol] > 1:
                    visit +=1
                else:
                    pass
            else:
                #just stay in the same position, waiting for the next movement in the cromo
                pass
                # print('Im not doing it :p')

        elif l == 'U':
            # Validate if the movement doesnt get out the matrix
            if posFila < 3:
                # Make movement to the left
                posFila+=1
                rideMatrix[posFila][posCol]+=1
                print('Up')
                # Check if the position has been visited before
                if  rideMatrix[posFila][posCol] > 1:
                    visit +=1
                else:
                    pass
            else:
                #just stay in the same position, waiting for the next movement in the cromo
                pass
                # print('Im not doing it :p')

        elif l == 'D':
            # Validate if the movement doesnt get out the matrix
            if posFila > 0:
                # Make movement to the left
                posFila-=1
                rideMatrix[posFila][posCol]+=1
                print('Up')
                # Check if the position has been visited before
                if  rideMatrix[posFila][posCol] > 1:
                    visit +=1
                else:
                    pass
            else:
                #just stay in the same position, waiting for the next movement in the cromo
                pass
                # print('Im not doing it :p')
        
    print(rideMatrix)
    print('{} Positions has been visited more than 1 time'.format(visit) )
    print('Row: {}  Column:{}'.format(posFila, posCol))
    
    # calculating the determinant of matrix 
    det = np.linalg.det(rideMatrix) 
    return det
    

def createPopulation():
    alphabet='UDLR'
    cromo1= random.choices(alphabet, k=15)
    cromo2= random.choices(alphabet, k=15)
    cromo3= random.choices(alphabet, k=15)
    cromo4= random.choices(alphabet, k=15)
    cromo5= random.choices(alphabet, k=15)

    return cromo1, cromo2, cromo3, cromo4, cromo5


if __name__ == "__main__":
    c1, c2, c3, c4, c5 = createPopulation()
    # print(c1)
    t = ['R','R','R','R', 'L','L','L','U','U','U','D','D','D','D','D']
    perfValueC1 = rideAndPerformance(c1)
    # perfValueC2 = rideAndPerformance(c2)
    # perfValueC3 = rideAndPerformance(c3)
    # perfValueC4 = rideAndPerformance(c4)
    # perfValueC5 = rideAndPerformance(c5)
