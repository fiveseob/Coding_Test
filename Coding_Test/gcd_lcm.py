def gcd(a, b):

    while b > 0:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())

if a < b:
    a, b =  b, a

print(gcd(a, b), lcm(a,b))


def gcd(a, b):
    while b > 0
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a,b)


def gcd(a, b):
    while b > 0:
        a, b = a, a % b
    return a

def lcm(a, b):
    return a * b  //  gcd(a, b)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b // gcd(a, b)