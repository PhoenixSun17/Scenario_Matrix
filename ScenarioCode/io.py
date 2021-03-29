from ScenarioCode.matrix_class import Matrix
import config
import sys

normal_stdin = sys.stdin


def menu_main(show=True):
    argument = get_arg(show)
    switcher = {
        "1": "Op",
        "2": "Det",
        "3": "Eig",
        "4": "IO",
        "5": "exit"
    }
    return switcher.get(argument, "Invalid, please retry")


def menu_op(show=True):
    argument = get_arg(show)
    switcher = {
        "1": "Add",
        "2": "Minus",
        "3": "Multiply",
        "4": "Mult Scalar",
        "5": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def menu_det(show=True):
    argument = get_arg(show)
    switcher = {
        "1": "2x2",
        "2": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def menu_eig(show=True):
    argument = get_arg(show)
    switcher = {
        "1": "EigenValue",
        "2": "EigenVector",
        "3": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def menu_io(show=True):
    argument = get_arg(show)
    switcher = {
        "1": "Import",
        "2": "Export",
        "3": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def open_file_stream(filename):
    config.file = open(filename, "r")
    set_file_stream()


def set_file_stream():
    sys.stdin = config.file


def set_user_stream():
    sys.stdin = normal_stdin


def input_matrix(n, show=True):  # num of row
    if show:
        print('N=', n)
        print('input :')
    a = [[] for _ in range(n)]
    for i in range(n):
        line = input()
        if show:
            config.store.append(line)
        int_line = [int(x) for x in line.split()]
        a[i] = int_line

    # a = [[int(x) for x in input().split()] for y in range(N)]
    for i in range(n - 1):
        if (len(a[i]) != len(a[i + 1])) and show:
            print('different number of column')
            return -1
    return Matrix(a)


def output_matrix(output):
    if type(output) == int:
        print(output)
        return -1
    if type(output) == list:
        # r = self.row_num
        # c = self.col_num
        n = 0
        for r in range(len(output)):
            for c in range(len(output[0])):
                # n = len(str(output[r][c]))
                if n < len(str(output[r][c])):
                    n = len(str(output[r][c]))

        for r in range(len(output)):
            for c in range(len(output[0])):
                item = str(output[r][c])
                print(item + ' ' * (n + 4 - len(item)), end='')
            print('\n')


def get_arg(show=True):
    if show:
        print()
        value = input("Please enter a number:")
        config.store.append(str(value))
    else:
        value = input()
    return value


def get_user_mat(n, show=True):
    print()
    matrix = input_matrix(n, show)
    return matrix


def get_ans(row, col):
    set_user_stream()
    print()
    if row == col and row == 0:
        ans = input("Ans is : ")
    else:
        print("Give your answer\nAnswer is ", row, "x", col, " matrix: ")
        ans = input_matrix(int(col), False)
        set_file_stream()
    return ans


def compare_ans(user_ans, sys_ans, is_int=False):
    if is_int:
        check_eq(user_ans == sys_ans, lambda: print(sys_ans))
    else:
        check_eq(user_ans.is_equal(sys_ans), lambda: sys_ans.show())

    print("\nType anything to continue")
    set_user_stream()
    input()
    set_file_stream()


def check_eq(ans_is_correct, display_correct_ans):
    if ans_is_correct:
        print("\nThat is correct!\n")
    else:
        print("\nThat is wrong!\nThis is the correct answer")
        display_correct_ans()
