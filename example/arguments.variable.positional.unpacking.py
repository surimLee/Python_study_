# arguments.variable.positional.unpacking.py

def func(*args):
    print(args)

values = (1, 3, -7, 9)

func(values) # func((1, 3, -7, 9))
func(*values) # func(1, 3, -7, 9)
