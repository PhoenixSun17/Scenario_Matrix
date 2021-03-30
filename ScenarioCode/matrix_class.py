

class Matrix:
    # a Matrix is accessed primarily by row index, then by columns, so m.get_item(i, j) will return
    # item at row i, column j

    # initializer
    def __init__(self, ls_2d: list):
        # ls_2d as a 2-dimensional list
        # rows, then columns - self.matrix[i][j] is row i, column j
        self.matrix = ls_2d.copy()

        # column number fixed as len of ls_2d
        self.row_num: int = len(ls_2d)
        if self.row_num == 0:
            # no elements in this matrix
            print("matrix has no elements")
        self.col_num: int = len(ls_2d[0])

    # copy function, useful to get a fresh copy of existing matrix
    def copy(self) -> 'Matrix':
        mat = Matrix(self.matrix)
        return mat

    # getter function for number of rows
    def get_row_num(self) -> int:
        return self.row_num

    # getter function for number of columns
    def get_col_num(self) -> int:
        return self.col_num

    # auxiliary function that raises exception if index is out of bounds
    def is_valid_index(self, row_i: int, col_i: int) -> bool:
        r = self.get_row_num()
        c = self.get_col_num()
        return r > row_i >= 0 and c > col_i >= 0

    # auxiliary function that returns false if sizes of matrices are not the same
    def size_is_same(self, mat: 'Matrix') -> bool:
        r = self.get_row_num()
        c = self.get_col_num()
        return r == mat.get_row_num() and c == mat.get_col_num()

    # swaps two rows by index, useful for gaussian elimination
    def swap_row(self, row_i_1: int, row_i_2: int):
        tmp = self.matrix[row_i_1]
        self.matrix[row_i_1] = self.matrix[row_i_2]
        self.matrix[row_i_2] = tmp

    # getter function for item by index
    def get_item(self, row_i: int, col_i: int) -> int:
        # check that indexes are valid
        if not self.is_valid_index(row_i, col_i):
            raise IndexError("invalid index")

        return self.matrix[row_i][col_i]

    # getter function for sub-matrix, removing column and row by index. Returns a Matrix object
    def get_sub_matrix(self, row_i: int, col_i: int) -> 'Matrix':
        r = self.get_row_num() - 1
        c = self.get_col_num() - 1
        sub_matrix = [[0 for _ in range(r)] for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if i < row_i:
                    curr_row_i = i
                else:
                    curr_row_i = i + 1
                if j < col_i:
                    curr_col_i = j
                else:
                    curr_col_i = j + 1
                try:
                    sub_matrix[i][j] = self.get_item(curr_row_i, curr_col_i)
                except IndexError:
                    print("invalid indexes")

        return Matrix(sub_matrix)

    # getter function for row, by index - returns a list
    def get_row(self, row_i: int) -> list:
        return self.matrix[row_i].copy()

    # getter function for column, by index - returns a list
    def get_col(self, col_i: int) -> list:
        ls = [0 for _ in range(self.row_num)]
        for i in range(self.row_num):
            try:
                ls[i] = self.get_item(i, col_i)
            except IndexError:
                print("invalid indexes")
        return ls

    # call on matrix 1, give argument matrix 2 to get matrix 1 x matrix 2 - returns Matrix object
    # will throw exception if sizes do not match
    def get_product(self, mat: 'Matrix') -> 'Matrix':  # should ensure type here is a Matrix object):
        if self.col_num != mat.get_row_num():
            raise Exception("Invalid multiplication of matrices")
        ri = self.get_row_num()
        c2 = mat.get_col_num()
        c1 = self.get_col_num()
        ls = [[0 for _ in range(c2)] for _ in range(ri)]
        for i in range(ri):
            for j in range(c2):
                for k in range(c1):
                    try:
                        ls[i][j] += self.get_item(i, k) * mat.get_item(k, j)
                    except IndexError:
                        print("invalid indexes")

        return Matrix(ls)

    # call on matrix 1, give argument matrix 2 to get matrix 1 + matrix 2 - returns Matrix object
    # will throw exception if sizes do not match
    def get_sum(self, mat: 'Matrix') -> 'Matrix':
        if self.size_is_same(mat):
            raise Exception("unmatched sizes")
        r = self.get_row_num()
        c = self.get_col_num()
        ls = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                try:
                    ls[i][j] = self.get_item(i, j) + mat.get_item(i, j)
                except IndexError:
                    print("invalid indexes")

        return Matrix(ls)

    # call on matrix 1, give argument matrix 2 to get matrix 1 - matrix 2 - returns Matrix object
    # will throw exception if sizes do not match
    def get_sub(self, mat: 'Matrix') -> 'Matrix':
        neg_mat = mat.copy()
        neg_mat.multiply_scalar(-1)
        val = 0
        try:
            val = self.get_sum(neg_mat)
        except Exception as e:
            print("problem in get_sub")
            print(e)
        return val

    # call on matrix 1 to get its determinant
    # will throw exception if called on non-square matrix
    def det(self) -> int:
        r = self.get_row_num()
        c = self.get_col_num()
        if r != c:
            raise Exception("called det on non-square matrix")
        elif r == 1:
            return self.get_item(0, 0)
        else:
            s = 0
            for i in range(r):
                m = self.get_sub_matrix(0, i)
                s += m.det() * self.get_item(0, i) * ((-1) ** (i % 2))
            return s

    # call on a matrix to multiply all contents by a scalar value
    # does not return anything - this only changes instance object's values
    def multiply_scalar(self, scalar_val: int):
        for row in self.matrix:
            for c_i in range(len(row)):
                row[c_i] *= scalar_val

    # check if two matrices have same size and values - useful in comparing answers
    def is_equal(self, mat: 'Matrix') -> bool:
        if self.size_is_same(mat):
            raise Exception("sizes unmatched")

        for i in range(self.get_row_num()):
            for j in range(self.get_col_num()):
                if self.get_item(i, j) != mat.get_item(i, j):
                    return False
        return True

    # displays a Matrix object as list of lists - useful in debugging and cmd line interface
    def show(self):
        print("Showing a matrix")
        for i in range(self.get_row_num()):
            for j in range(self.get_col_num()):
                try:
                    print(self.get_item(i, j), end="\t")
                except IndexError:
                    print("invalid indexes")
            print("")
