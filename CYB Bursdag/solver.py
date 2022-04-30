from math import sqrt

a, b = [int(x) for x in input().split()]

i = a
numPrimes = 0
while i <= b:
    for x in range(2, int(sqrt(i) + 1)):
        if i%x==0:
            break
    else:
        numPrimes += 1
    i += 1

print((numPrimes / (b-a))*100)
