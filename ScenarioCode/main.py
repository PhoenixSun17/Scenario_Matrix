from display import *
# noinspection PyUnresolvedReferences
from matrix_class import *
import sys

# global variables needed to change input streams
normal_stdin = sys.stdin
file = None
global store
store = []


def Menu_main():

    argument = GetArg()
    switcher = {
        "1": "Op",
        "2": "Det",
        "3": "Eig",
        "4": "IO",
        "5": "exit"
    }
    return switcher.get(argument, "Invalid, please retry")


def Menu_operation():
    argument = GetArg()
    switcher = {
        "1": "Add",
        "2": "Minus",
        "3": "Multiply",
        "4": "Mult Scalar",
        "5": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def Menu_Det():
    argument = GetArg()
    switcher = {
        "1": "2x2",
        "2": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def Menu_eigenvalue():
    argument = GetArg()
    switcher = {
        "1": "EigenValue",
        "2": "EigenVector",
        "3": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def Menu_IO():
    argument = GetArg();
    switcher = {
        "1": "Import",
        "2": "Export",
        "3": "Break"
    }
    return switcher.get(argument, "Invalid, please retry")


def Go():
    print()
    while True:
        printMenu_main()
        key = Menu_main()
        if key == "Op":
            while True:
                printMenu_op()
                key_op = Menu_operation()
                if key_op == "Break":
                    break
                elif key_op == "Add":
                    addc = int(input("Please enter the number of columns:"))
                    store.append(addc)
                    Mat1 = GetUserMat(addc)
                    Mat2 = GetUserMat(addc)
                    Mat_Ans = Mat1.get_sum(Mat2)
                    getAns(Mat_Ans.row_num, Mat_Ans.col_num)
                    Mat_Ans.show()
                elif key_op == "Minus":
                    minc = int(input("Please enter the number of columns:"))
                    store.append(minc)
                    Mat1 = GetUserMat(minc)
                    Mat2 = GetUserMat(minc)
                    Mat_Ans = Mat1.get_sub(Mat2)
                    getAns(Mat_Ans.row_num, Mat_Ans.col_num)
                    Mat_Ans.show()
                elif key_op == "Multiply":
                    mulc1 = int(input("Please enter the number of columns of first matrix:"))
                    store.append(mulc1)
                    Mat1 = GetUserMat(mulc1)
                    mulc2 = int(input("Please enter the number of columns of second matrix:"))
                    store.append(mulc2)
                    Mat2 = GetUserMat(mulc2)
                    Mat_Ans = Mat1.get_product(Mat2)
                    getAns(Mat_Ans.row_num, Mat_Ans.col_num)
                    Mat_Ans.show()
                elif key_op == "Mult Scalar":
                    scc = int(input("Please enter the number of columns:"))
                    store.append(scc)
                    Mat1 = GetUserMat(scc)
                    Mat2 = GetArg()
                    try:
                        Mat2 = int(Mat2)
                    except ValueError as e:
                        print("The input is Invalid")
                    else:
                        (Mat1.mult_scalar(Mat2)).show()
                elif key_op == "Invalid, please retry":
                    print(Menu_operation())
        elif key == "Det":
            while True:
                printMenu_Det()
                key_det = Menu_Det()
                if key_det == "Break":
                    break
                elif key_det == "2x2":
                    print("Please Enter one Matrix to calculate Determinant")
                    Mat = GetUserMat(2)
                    try:
                        i = Mat.det()
                    except ValueError:
                        print("The Matrix you input is invalid, please retry")
                    else:
                        print("The Determinant of the Matrix is: ", i)
                elif key_det == "Invalid, please retry":
                    print(Menu_Det())
        elif key == "Eig":
            while True:
                printMenu_Eig()
                if Menu_eigenvalue() == "Break":
                    break
                elif Menu_eigenvalue() == "Invalid, please retry":
                    print(Menu_eigenvalue())
        elif key == "exit":
            exit()
        elif key == "IO":
            while True:
                printMenu_IO()
                key_Io = Menu_IO()
                if key_Io == "Break":
                    break
                if key_Io == "Import":
                    filename = input("file name:")
                    setFileStream(filename)
                    # need to not exit program at this point
                    alternateGo()
                    setUserStream()
                if key_Io == "Export":
                    store.pop()
                    store.pop()
                    store.append("5")
                    # get filename
                    # write to that file
                    filename = input("file name: ")
                    file = open(filename, "w")
                    for line in store:
                        # might need to add \n
                        file.write(str(line))
                    file.close()
                    print("Your file has been saved!")
                elif key_Io == "Invalid, please retry":
                    printMenu_IO()
        else:
            print("Invalid, please retry")


def alternateGo():
    print()
    while True:
        printMenu_main2()
        key = Menu_main()
        if key == "Op":
            while True:
                printMenu_op()
                key_op = Menu_operation()
                if key_op == "Break":
                    break
                elif key_op == "Add":
                    addc = int(input("Please enter the number of columns:"))
                    store.append(addc)
                    Mat1 = GetUserMat(addc)
                    Mat2 = GetUserMat(addc)
                    Mat_Ans = Mat1.get_sum(Mat2)
                    getAns(Mat_Ans.row_num, Mat_Ans.col_num)
                    Mat_Ans.show()
                elif key_op == "Minus":
                    minc = int(input("Please enter the number of columns:"))
                    store.append(minc)
                    Mat1 = GetUserMat(minc)
                    Mat2 = GetUserMat(minc)
                    Mat_Ans = Mat1.get_sub(Mat2)
                    getAns(Mat_Ans.row_num, Mat_Ans.col_num)
                    Mat_Ans.show()
                elif key_op == "Multiply":
                    mulc1 = int(input("Please enter the number of columns of first matrix:"))
                    store.append(mulc1)
                    Mat1 = GetUserMat(mulc1)
                    mulc2 = int(input("Please enter the number of columns of second matrix:"))
                    store.append(mulc2)
                    Mat2 = GetUserMat(mulc2)
                    Mat_Ans = Mat1.get_product(Mat2)
                    getAns(Mat_Ans.row_num, Mat_Ans.col_num)
                    Mat_Ans.show()
                elif key_op == "Mult Scalar":
                    scc = int(input("Please enter the number of columns:"))
                    store.append(scc)
                    Mat1 = GetUserMat(scc)
                    Mat2 = GetArg()
                    try:
                        Mat2 = int(Mat2)
                    except ValueError:
                        print("The input is Invalid")
                    else:
                        Mat_Ans = Mat1.mult_scalar(Mat2)
                        getAns(Mat_Ans.row_num, Mat_Ans.col_num)
                        Mat_Ans.show()
                elif key_op == "Invalid, please retry":
                    print(Menu_operation())
        elif key == "Det":
            while True:
                printMenu_Det()
                key_det = Menu_Det()
                if key_det == "Break":
                    break
                elif key_det == "2x2":
                    print("Please Enter one Matrix to calculate Determinant")
                    Mat = GetUserMat(2)
                    try:
                        i = Mat.det()
                    except ValueError:
                        print("The Matrix you input is invalid, please retry")
                    else:
                        getAns(0, 0)
                        print("The Determinant of the Matrix is: ", i)
                elif key_det == "Invalid, please retry":
                    print(Menu_Det())
        elif key == "Eig":
            while True:
                printMenu_Eig()
                if Menu_eigenvalue() == "Break":
                    break
                elif Menu_eigenvalue() == "Invalid, please retry":
                    print(Menu_eigenvalue())
        elif key == "exit":
            return


def printMenu_main():
    print("Welcome to Matrix Practice system Ver 1.0.0")
    print("1: Basic Matrix Operation Practice")
    print("2: Determinant Operation Practice")
    print("3: Eigenvalue/Eigenvector Operation Practice")
    print("4: File IO Function Menu")
    print("5: Quit the System")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to main menu")
    return


def printMenu_main2():
    print("Welcome to Matrix Practice system Ver 1.0.0")
    print("1: Basic Matrix Operation Practice")
    print("2: Determinant Operation Practice")
    print("3: Eigenvalue/Eigenvector Operation Practice")
    print("5: Quit the System")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to main menu")
    return


def printMenu_op():
    print("This is the sub menu of operation practice")
    print("1: Do Add Operation")
    print("2: Do Minus Operation")
    print("3: Do Multiply Matrix Operation")
    print("4: Do Multiply Scalar Operation")
    print("5: Quit to Main Menu")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to this menu")
    return


def printMenu_Det():
    print("This is the sub menu of determinant practice")
    print("1: Do Determinant Operation")
    print("2: Quit to Main Menu")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to this menu")
    return


def printMenu_Eig():
    print("This is the sub menu of Eigenvalue/vector practice")
    print("1: Do Eigenvalue Operation")
    print("2: Do Eigenvector Operation")
    print("3: Quit to Main Menu")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to this menu")
    return


def printMenu_IO():
    print("This is the sub menu of imported practice")
    print("1: Import exercise")
    print("2: Export exercise")
    print("3: Quit to Main Menu")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to this menu")
    return


def GetArg():
    print()
    value = input("Please enter a number:")

    store.append(str(value))
    return value


def GetUserMat(n):
    print()
    matrix = input_dis(n)
    store.append(matrix)
    return matrix


def setFileStream():
    sys.stdin = file


def setUserStream():
    sys.stdin = normal_stdin


def getAns(row, col):
    setUserStream()
    if row == col and row == 0:
        ans = input("Ans is : ")
    else:
        print("Answer is ", row, "x", col, " matrix: ")
        ans = input_dis(int(col))
        setFileStream()
    return ans


Go()