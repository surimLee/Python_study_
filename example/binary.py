# binary.py

n = 39
remainders = []

while n > 0:
    remainder = n % 2 # remainder if division by 2
    remainders.insert(0, remainder) # we keep track of remainders
    n //= 2 # we devide n by 2

print(remainders)
