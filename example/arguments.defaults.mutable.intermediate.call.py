# arguments.defaults.mutable.intermediate.call.py

def func(a=[], b= {}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))    #this will affect a's default value
    b[len(a)] = len(a)  #this will affect b's value

func()
func(a=[1, 2, 3], b={'B': 1})
func()
