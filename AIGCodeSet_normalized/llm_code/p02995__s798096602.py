"""
Created on Fri May 15 00:52:33 2020

@author: Kanaru Sato
"""
import fractions

def f1(a1, a2, a3):
    if a1 % a3 == 0:
        return a2 // a3 - a1 // a3 + 1
    else:
        return a2 // a3 - a1 // a3
v1, v2, v3, v4 = list(map(int, input().split()))
v5 = v3 * v4 / fractions.gcd(v3, v4)
v6 = f1(v1, v2, v3) + f1(v1, v2, v4) - f1(v1, v2, v5)
print(int(v2 - v1 + 1 - v6))
