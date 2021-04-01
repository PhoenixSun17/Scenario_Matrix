import numpy as np
from matrix_class import Matrix


# Through Householder transformation, the simplified matrix can be
# transformed into an upper triangular matrix.
def householder(x, i=0):
    x = x.reshape(len(x), 1)
    ei = np.zeros((len(x), 1))
    ei[i] = 1
    y = np.linalg.norm(x, ord=2) * ei
    if x[i] > 0:
        w = (x + y) / np.linalg.norm(x + y)
    else:
        w = (x - y) / np.linalg.norm(x - y)
    H = np.eye(len(x)) - 2 * np.dot(w, w.T)
    return H


# QR decomposition of matrix
def QR_decomposion(A):
    dim = len(A)
    Ri = A.copy()
    for i in range(dim - 1):
        x = Ri[i:, i]
        Hi = householder(x)
        Ri[i:, i:] = np.dot(Hi, Ri[i:, i:])
        Qi = np.eye(dim)
        Qi[i:, i:] = Hi
        if i == 0:
            Q = Qi
        else:
            Q = np.dot(Qi, Q)
    D = np.asmatrix(np.diag(np.where(np.diag(Ri) < 0, -1, 1)))
    R = D * np.asmatrix(Ri)  # Make the diagonal elements of the R matrix all positive
    Q = np.asmatrix(Q.T) * D.I
    return Q, R


# Generate [ak] sequence after iteration and find eigenvalue
def eigenvalue(A, eps=1e-6):
    # Ak = A.copy()
    Ak = [A.get_row(i) for i in range(A.get_row_num())]
    Ak = np.array(Ak, dtype='float')
    flag = 1
    n = 0
    while flag:
        Ak0 = Ak.copy()
        Qk, Rk = QR_decomposion(Ak)
        Ak = Rk * Qk
        if (np.sum(np.diag(np.abs(Ak - Ak0))) < eps):
            flag = 0
        n = n + 1
    # print(n) n is the number of iterations
    return np.diag(Ak)


if __name__ == '__main__':
    # A = np.array([[9, 7], [9, 2]], dtype='float')
    A = [[9, 8, 1], [7, 6, 5], [4, 3, 2]]
    m = Matrix(A)
    eig = eigenvalue(m,1e-7)
    # eig = eigenvalue(A, 1e-7)
    print('eig:', eig)
