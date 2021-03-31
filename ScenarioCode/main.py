from ScenarioCode.print_menu import *
# noinspection PyUnresolvedReferences
from ScenarioCode.io import *
import config
from eigenvalue_v2 import *

def go():
    print()
    while True:
        print_menu_main()
        key = menu_main()
        if key == "Op":
            while True:
                current_store = config.store.copy()
                print_menu_op()
                key_op = menu_op()
                if key_op == "Break":
                    break
                elif key_op == "Add":
                    add_c = int(input("Please enter the number of rows:"))
                    config.store.append(add_c)
                    mat_1 = get_user_mat(add_c)
                    mat_2 = get_user_mat(add_c)
                    try:
                        mat_ans = mat_1.get_sum(mat_2)
                    except ArithmeticError as e:
                        print("Invalid sum operation on matrices of different sizes\n")
                        config.store = current_store
                    else:
                        mat_ans.show()
                elif key_op == "Minus":
                    min_c = int(input("Please enter the number of rows:"))
                    config.store.append(min_c)
                    mat_1 = get_user_mat(min_c)
                    mat_2 = get_user_mat(min_c)
                    try:
                        mat_ans = mat_1.get_sub(mat_2)
                    except ArithmeticError as e:
                        print("Invalid subtraction operation on matrices of different sizes\n")
                        config.store = current_store
                    else:
                        mat_ans.show()
                elif key_op == "Multiply":
                    mul_c_1 = int(input("Please enter the number of rows of first matrix:"))
                    config.store.append(mul_c_1)
                    mat_1 = get_user_mat(mul_c_1)
                    mul_c_2 = int(input("Please enter the number of rows of second matrix:"))
                    config.store.append(mul_c_2)
                    mat_2 = get_user_mat(mul_c_2)
                    try:
                        mat_ans = mat_1.get_product(mat_2)
                    except ArithmeticError:
                        print("Invalid multiplication operation on matrices of unmatched sizes\n")
                        config.store = current_store
                    else:
                        mat_ans.show()
                elif key_op == "Mult Scalar":
                    scc = int(input("Please enter the number of rows:"))
                    config.store.append(scc)
                    mat_1 = get_user_mat(scc)
                    mat_2 = get_arg()
                    try:
                        mat_2 = int(mat_2)
                    except ValueError as e:
                        print("The input is Invalid\n")
                        config.store = current_store
                    else:
                        mat_ans = mat_1.multiply_scalar(mat_2)
                        mat_ans.show()
                elif key_op == "Invalid, please retry":
                    print(menu_op())
                elif key == "Det":
            while True:
                current_store = config.store.copy()
                print_menu_det()
                key_det = menu_det()
                if key_det == "Break":
                    break
                elif key_det == "2x2":
                    n = int(input("Please enter the number of rows:"))
                    config.store.append(n)
                    print("Please Enter one Matrix to calculate Determinant")
                    mat = get_user_mat(n)
                    try:
                        i = mat.det()
                    except ValueError:
                        print("The Matrix you input is invalid, please retry\n")
                        config.store = current_store
                    else:
                        print("The Determinant of the Matrix is: ", i)
                elif key_det == "Invalid, please retry":
                    print(menu_det())
        elif key == "Eig":
            while True:
                current_store = config.store.copy()
                print_menu_eig()
                key_eig = menu_eig()
                if key_eig == "Break":
                    break
                elif key_eig == "EigenValue":
                    print("Please Enter one Matrix to calculate Eigenvalue")
                    c = int(input("Please enter the number of rows:"))
                    config.store.append(c)
                    mat = get_user_mat(c)

                    try:
                        eigenvalues = eigenvalue(mat)
                    except Exception as e:
                        print("invalid matrix\n")
                        config.store = current_store
                    else:
                        print("Eigenvalues are: ")
                        for val in eigenvalues:
                            print(val, end="\t\t")
                        print("\n")

                    eigenvalues = eigenvalue(mat)
                    print("Eigenvalues are: ")
                    for val in eigenvalues:
                        print(val, end="\t")

                elif key_eig == "Invalid, please retry":
                    print(menu_eig())
        elif key == "exit":
            exit()
        elif key == "IO":
            current_store = config.store.copy()
            while True:
                print_menu_io()
                key_io = menu_io()
                if key_io == "Break":
                    config.store = current_store
                    break
                if key_io == "Import":
                    filename = input("file name:")
                    try:
                        open_file_stream(filename)
                    except FileNotFoundError as fnfe:
                        print("invalid file")
                    else:
                        alt_go()
                    set_user_stream()
                if key_io == "Export":
                    config.store.pop()
                    config.store.pop()
                    config.store.append("5")
                    filename = input("file name: ")
                    try:
                        file = open(filename, "w")
                    except FileNotFoundError as fnfe:
                        print("file not found")
                    else:
                        for line in config.store:
                            file.write(str(line))
                            file.write("\n")
                        print("Your file has been saved!")
                    finally:
                        file.close()
                elif key_io == "Invalid, please retry":
                    print_menu_io()
        else:
            print("Invalid, please retry")


def alt_go():
    print()
    while True:
        # print_menu_main_alt()
        key = menu_main(False)
        if key == "Op":
            while True:
                # print_menu_op()
                key_op = menu_op(False)
                if key_op == "Break":
                    break
                elif key_op == "Add":
                    add_c = int(input())
                    mat_1 = get_user_mat(add_c, False)
                    mat_1.show()
                    print("\n+")
                    mat_2 = get_user_mat(add_c, False)
                    mat_2.show()
                    mat_ans = mat_1.get_sum(mat_2)
                    user_ans = get_ans(mat_ans.row_num, mat_ans.col_num)
                    compare_ans(user_ans, mat_ans)
                elif key_op == "Minus":
                    min_c = int(input())
                    mat_1 = get_user_mat(min_c, False)
                    mat_1.show()
                    print("\n-")
                    mat_2 = get_user_mat(min_c, False)
                    mat_2.show()
                    mat_ans = mat_1.get_sub(mat_2)
                    user_ans = get_ans(mat_ans.row_num, mat_ans.col_num)
                    compare_ans(user_ans, mat_ans)
                elif key_op == "Multiply":
                    mul_c_1 = int(input())
                    mat_1 = get_user_mat(mul_c_1, False)
                    mat_1.show()
                    print("\nx")
                    mul_c_2 = int(input())
                    mat_2 = get_user_mat(mul_c_2, False)
                    mat_2.show()
                    mat_ans = mat_1.get_product(mat_2)
                    user_ans = get_ans(mat_ans.row_num, mat_ans.col_num)
                    compare_ans(user_ans, mat_ans)
                elif key_op == "Mult Scalar":
                    scc = int(input())
                    config.store.append(scc)
                    mat_1 = get_user_mat(scc, False)
                    mat_1.show()
                    print("\nx")
                    mat_2 = get_arg(False)
                    try:
                        mat_2 = int(mat_2)
                    except ValueError:
                        print()
                    else:
                        print(mat_2)
                        mat_1.multiply_scalar(mat_2)
                        mat_ans = mat_1
                        user_ans = get_ans(mat_ans.row_num, mat_ans.col_num)
                        compare_ans(user_ans, mat_ans)
                elif key_op == "Invalid, please retry":
                    print(menu_op(False))
        elif key == "Det":
            while True:
                # print_menu_det()
                key_det = menu_det(False)
                if key_det == "Break":
                    break
                elif key_det == "2x2":
                    n = int(input("Please enter the number of rows:"))
                    config.store.append(n)
                    print("Please Enter one Matrix to calculate Determinant")
                    mat = get_user_mat(n, False)
                    print("\nDeterminant of : ")
                    mat.show()
                    try:
                        i = mat.det()
                    except ValueError:
                        print()
                    else:
                        user_ans = get_ans(0, 0)
                        compare_ans(user_ans, i, True)

                elif key_det == "Invalid, please retry":
                    print(menu_det(False))
        elif key == "Eig":
            while True:
                # print_menu_eig()
                key_eig = menu_eig()
                if key_eig == "Break":
                    break
                elif key_eig == "EigenValue":
                    print()
                    c = int(input())
                    mat = get_user_mat(c, False)
                    eigenvalues = eigenvalue(mat)
                    print("\nGive eigenvalues for: ")
                    mat.show()
                    user_ans = get_list_ans()
                    missed_ans = []
                    for ans in eigenvalues:
                        if ans not in user_ans:
                            missed_ans.append(ans)
                    if len(missed_ans) == 0:
                        print("\nThat is correct!")
                    else:
                        print("\nYou missed: ", end="")
                        for ans in missed_ans:
                            print(ans, end="\t")

                elif key_eig == "Invalid, please retry":
                    print(menu_eig(False))
        elif key == "exit":
            print("Exercise is complete!\n")
            return


go()

