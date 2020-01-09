import numpy as np 
import random 


def mut(element):
    if element == 0:
        return 1
    else:
        return 0

def mutation(matrix, p):
    matrix2 = np.zeros((matrix.shape[0],matrix.shape[1]))
    for i in range(0,matrix2.shape[0]):
        for j in range (0,matrix.shape[1]):
            matrix2[i][j] = random.uniform(0,1)

    for i in range(0,matrix.shape[0]):
        for j in range(0,matrix.shape[1]):
            if matrix2[i][j] < p:
                matrix[i][j] = mut(matrix[i][j])

    return matrix


####inversja#############




def inversion(matrix,p):

    list_p = [random.uniform(0,1) for i in range(0,matrix.shape[0])]

    for i in range(0,matrix.shape[0]):
        if list_p[i] < p:
            _from = random.randint(0,matrix.shape[1] - 1)
            _to = random.randint(_from, matrix.shape[1] - 1)
            row_for_invers = matrix[i][_from:_to]
            list_invers = row_for_invers[::-1]
            matrix[i][_from:_to] = list_invers
    return matrix       






