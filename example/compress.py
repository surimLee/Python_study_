# compress.py

from itertools import compress

data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_number = list(compress(data, even_selector))
odd_number = list(compress(data, odd_selector))

print(odd_selector)
print(list(data))
print(even_number)
print(odd_number)
