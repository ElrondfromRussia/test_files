import os
import ctypes


def print_result(num):
    print("I am heeere ", 5, " years and " , num, "month in ", os.curdir)


def makefile(name, path):
    print(name, " ", path)
    try:
        my_file = open(path + "/" + name, 'w')
        my_file.write("Hello, " + name)
    except BaseException as ex:
        print("Can no create file: ", path + "/" + name, 'w', "  ex: ", ex)

