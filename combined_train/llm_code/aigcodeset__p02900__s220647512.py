from fractions import gcd

def f1(a1):
    if a1 == 1:
        return 1
    v1 = 1
    for v2 in range(2, a1 + 1):
        if v2 % 2 == 0 and v2 != 2:
            continue
        if pow(2, v2 - 1, v2) == 1:
            v1 += 1
    return v1

def f2(a1, a2):
    v1 = gcd(a1, a2)
    v2 = set()
    v3 = 2
    while v3 * v3 <= v1:
        if v1 % v3:
            v3 += 1
        else:
            v1 //= v3
            v2.add(v3)
    if v1 > 1:
        v2.add(v1)
    return len(v2)
if __name__ == '__main__':
    v1, v2 = map(int, input().split())
    print(f2(v1, v2))
