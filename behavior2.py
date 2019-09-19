import os
import ctypes


def print_result(num):
    print("I am heeere ", 10, " years and ", num, "month in ", os.curdir)


def makefile(name):
    print(name)
    try:
        my_file = open(name, 'w')
        my_file.write("Bye-bye, " + name)
    except BaseException as ex:
        print("Can no create file: ", name, 'w', "  ex: ", ex)

