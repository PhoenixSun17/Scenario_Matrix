class Matrix:

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

    def copy(self):
        mat = Matrix(self.matrix)
        return mat

    def get_row_num(self) -> int:
        return self.row_num

    def get_col_num(self) -> int:
        return self.col_num

    def get_item(self, row_i: int, col_i: int) -> int:
        # check that indexes are valid
        if not self.is_valid_index(row_i, col_i):
            raise IndexError("invalid index")

        return self.matrix[row_i][col_i]

    def is_valid_index(self, row_i: int, col_i: int) -> bool:
        return self.row_num > row_i >= 0 and self.col_num > col_i >= 0

    def swap_row(self, row_i_1: int, row_i_2: int):
        tmp = self.matrix[row_i_1]
        self.matrix[row_i_1] = self.matrix[row_i_2]
        self.matrix[row_i_2] = tmp

    def get_submatrix(self, row_i: int, col_i: int):
        submatrix = [[None for i in range(self.row_num - 1)] for j in range(self.col_num - 1)]
        for i in range(self.row_num - 1):
            for j in range(self.col_num - 1):
                if i < row_i:
                    curr_row_i = i
                else:
                    curr_row_i = i + 1
                if j < col_i:
                    curr_col_i = j
                else:
                    curr_col_i = j + 1
                try:
                    submatrix[i][j] = self.get_item(curr_row_i, curr_col_i)
                except IndexError:
                    print("invalid indexes")

        return Matrix(submatrix)

    def show(self):
        print("Showing a matrix")
        for i in range(self.row_num):
            for j in range(self.col_num):
                try:
                    print(self.get_item(i, j), end="\t")
                except IndexError:
                    print("invalid indexes")
            print("")

    def get_row(self, row_i: int) -> list:
        return self.matrix[row_i].copy()

    def get_col(self, col_i: int) -> list:
        ls = [0 for i in range(self.row_num)]
        for i in range(self.row_num):
            try:
                ls[i] = self.get_item(i, col_i)
            except IndexError:
                print("invalid indexes")
        return ls

    def get_product(self, mat):  # should ensure type here is a Matrix object):
        if self.col_num != mat.get_row_num():
            return None
        ls = [[0 for i in range(self.row_num)] for j in range(mat.get_col_num())]
        ri = self.row_num
        c2 = mat.get_col_num()
        c1 = self.col_num
        for i in range(ri):
            for j in range(c2):
                for k in range(c1):
                    try:
                        ls[i][j] = ls[i][j] + self.get_item(i, k) * mat.get_item(k, j)
                    except IndexError:
                        print("invalid indexes")

        return Matrix(ls)

    def size_is_same(self, mat):
        # check sizes of matrices match
        if not (self.row_num == mat.get_row_num() and self.col_num == mat.get_col_num()):
            print("self.row_num is ", self.row_num, "\nself.col_num is ", self.col_num)
            print("mat.row_num is ", mat.get_row_num, "mat.col_num is ", mat.get_col_num)
            raise Exception("unmatched sizes")

    def get_sum(self, mat):
        try:
            self.size_is_same(mat)
        except Exception as e:
            raise Exception("unmatched sizes")

        ls = [[None for _ in range(self.col_num)] for _ in range(self.row_num)]
        for i in range(self.row_num):
            for j in range(self.col_num):
                try:
                    ls[i][j] = self.get_item(i, j) + mat.get_item(i, j)
                except IndexError:
                    print("invalid indexes")

        return Matrix(ls)

    def mult_scalar(self, coeff: int):
        for row in self.matrix:
            for c_i in range(len(row)):
                row[c_i] *= coeff

    def transposition(self):
        ls = [[None for i in range(self.row_num)] for j in range(self.col_num)]
        for i in self.matrix:
            for j in self.matrix[i]:
                ls[i][j] = self.get_item(j, i)
        return Matrix(ls)

    def get_sub(self, mat):
        neg_mat = mat.copy()
        neg_mat.mult_scalar(-1)
        val = 0
        try:
            val = self.get_sum(neg_mat)
        except Exception as e:
            print("problem in get_sub")
            print(e)
        return val

    def is_equal(self, mat):
        try:
            self.size_is_same(mat)
        except Exception as e:
            raise Exception("sizes unmatched")

        for i in range(self.row_num):
            for j in range(self.col_num):
                if self.get_item(i, j) != mat.get_item(i, j):
                    return False
        return True

    def det(self) -> int:
        r = self.row_num
        if r != self.col_num:
            raise Exception("called det on square matrix")
        elif r == 1:
            return self.get_item(0,0)
        else:
            s = 0
            for i in range(r):
                m = self.get_submatrix(0,i)
                s += m.det() * self.get_item(0,i) * ((-1) ** (i % 2))
            return s
