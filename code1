import time
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def getD_bruteforce(p, q, e):
    L = lcm(p-1, q-1)
    d = 1
    while True:
        if (e * d) % L == 1:
            return d
        d += 1

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def getD_extgcd(p, q, e):
    L = lcm(p-1, q-1)
    g, x, _ = extgcd(e, L)
    return x % L

def measure(func, p, q, e):
    start = time.time()
    try:
        func(p, q, e)
        return time.time() - start
    except:
        return None

pairs = [(10007,10009),(20011,20021),(30011,30013),(40009,40013)]
e = 65537

for p, q in pairs:
    t1 = measure(getD_bruteforce, p, q, e)
    t2 = measure(getD_extgcd, p, q, e)
    print(p, q, t1, t2)
