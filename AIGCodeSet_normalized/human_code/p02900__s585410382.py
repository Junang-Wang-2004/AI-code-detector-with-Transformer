import math
v1, v2 = map(int, input().split())

def f1(a1):
    v1 = [1]
    while a1 % 2 == 0:
        v1.append(2)
        a1 //= 2
    v3 = 3
    while v3 * v3 <= a1:
        if a1 % v3 == 0:
            v1.append(v3)
            a1 //= v3
        else:
            v3 += 2
    if a1 != 1:
        v1.append(a1)
    v1.sort()
    return v1
print(len(list(set(f1(math.gcd(v1, v2))))))
