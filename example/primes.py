# primes.py

primes = []
upto = 100

for n in range(2, upto + 1) :
    is_prime = True # flag, new at each iteration of outer for

    for divisor in range(2, n):

        if n % divisor == 0:
            is_prime = False
            break

    if is_prime: # check on flag
        primes.append(n)

print(primes)
