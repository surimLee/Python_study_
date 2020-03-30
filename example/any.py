# any.py

items = [0, None, 0.0, True, 0, 7]

found = False   # this is called "flas"

for item in items:
    print('scanning item', item)

    if item:
        found = True    # we update the flag
        break

if found:   # we inspect the flag
    print('At least one item evaluates to True')

else:
    print('All items evaluate to False')
