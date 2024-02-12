import math
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

p = 16
q = 12
n = p * q
a = p - 1
b = q - 1
lambda_val = (a * b) // math.gcd(a, b)

e = 11
d = modinv(e, lambda_val)

print("d =", d)
