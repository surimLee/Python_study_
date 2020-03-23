# scopes3.py
# Local, Enclosing and Global

def enclosing_func():
    m = 13

    def local():
        # m doesn't belong to the scope defined by the local function
        # so Python will keep looking into the next enclosing scope.
        # m is finally found in the global scope
        print(m, 'printing from the local scope')
    # calling the function local
    local()

m=5
print(m, 'printing from the global scope')

enclosing_func()
