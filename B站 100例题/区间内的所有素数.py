def is_prime(num):
    if num < 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False;
    return True


def judgePrime(fir, sec):
    for i in range(fir, sec + 1):
        if is_prime(i):
            print(f"{i}是素数")


judgePrime(11, 25)
