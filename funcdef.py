# funcdef.py

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

# func_import.py
import lib.funcdef
print(lib.funcdef.square(10))
print(lib.funcdef.cube(10))

# defc_from.py
from lib.funcdef import square, cube
print(square(10))
print(cube(10))
