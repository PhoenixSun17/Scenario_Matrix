import math
from collections.abc import Iterable
from copy import deepcopy
from matrix_class import *

def mod(vector):
    '''
    Find the modulus of a vector
    '''
    sum = 0
    for i in vector:
        sum += i*i
    return math.sqrt(sum)


def scalar_product(v1, v2):
    '''
    Find the inner product of two vectors
    '''
    sum = 0
    for i, j in zip(v1, v2):
        sum += i*j
    return sum


def gram_schmidt(Matrix):
    '''
    Matrix Schmidt Orthogonalization
    '''
    rows = len(Matrix)
    cols = len(Matrix[0])
    Result = [[0 for i in range(cols)] for i in range(rows)]  
    for col in range(cols):
        v_col = [Matrix[row][col] for row in range(rows)]
        beta_col = v_col.copy()
        for i in range(col):
            eta_i = [Result[row][i] for row in range(rows)]
            a = scalar_product(v_col, eta_i)
            beta_col = [i-a*j for i, j in zip(beta_col, eta_i)]
        norm = mod(beta_col)
        if(norm != 0):
            for row in range(rows):
                Result[row][col] = beta_col[row]/norm
    return Result


def roundM(Matrix, precision=5):
    '''
    Keep integers
    '''
    for i in range(len(Matrix)):
        if(isinstance(Matrix[i], Iterable)):
            Matrix[i] = roundM(Matrix[i], precision)
        else:
            Matrix[i] = round(Matrix[i], precision)
    return Matrix


def get_QR(Matrix):
    '''
    Matrix QR decomposition
    A non-singular matrix Matrix=QR, where Q is an orthogonal matrix and R is a non-singular upper triangular matrix
    '''
    Q = gram_schmidt(Matrix)
    rows = len(Q)
    cols = len(Q[0])
    R = [[0 for col in range(cols)] for row in range(rows)]
    for row in range(rows):
        v1 = [Q[i][row] for i in range(rows)]
        for col in range(cols):
            v2 = [Matrix[i][col] for i in range(rows)]
            R[row][col] = scalar_product(v1, v2)
    Q = roundM(Q)
    R = roundM(R)
    return Q, R


def eigenvalue(A):
    # returns a list of all eigenvalues
    '''
    Find all the eigenvalues of the matrix
    '''
    # modified Ak here to take in a Matrix object
    Ak = [A.get_row(i) for i in range(A.get_row_num())]
    rows = len(Ak)
    cols = len(Ak[0])
    flag = 1
    while flag:
        Ak0 = deepcopy(Ak)
        Qk, Rk = get_QR(Ak)
        sum = 0
        for row in range(rows):
            v1 = [Rk[row][i] for i in range(cols)]
            for col in range(cols):
                v2 = [Qk[i][col] for i in range(rows)]
                Ak[row][col] = scalar_product(v1, v2)
                #print(Ak)
                sum += abs(Ak[row][col]-Ak0[row][col])
        if (sum < 1e-6):
            flag = 0
    return roundM([Ak[i][i] for i in range(cols)])


if __name__ == '__main__':
    m = Matrix( [[1, 1, 1], [0, 2, 1], [0, 0, 3]])
    print(eigenvalue(m))