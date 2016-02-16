def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

Say = 0
for i in range(1, 1000):
    if isPrime(i):
        print("{:>3}".format(str(i)), end= " ")
        Say += 1
        if Say % 10 == 0:
            print(" ")
    else:
        continue
