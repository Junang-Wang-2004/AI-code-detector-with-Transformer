def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f2(a1):
    """Miller Rabin primality test. 2 <= n <= 2 ** 64 is required"""
    if a1 % 2 == 0:
        return a1 == 2
    v1 = a1 - 1
    v2 = (v1 & -v1).bit_length() - 1
    v1 >>= v2
    if a1 < 2152302898747:
        if a1 < 9080191:
            if a1 < 2047:
                v3 = [2]
            else:
                v3 = [31, 73]
        elif a1 < 4759123141:
            v3 = [2, 7, 61]
        else:
            v3 = [2, 3, 5, 7, 11]
    elif a1 < 341550071728321:
        if a1 < 3474749660383:
            v3 = [2, 3, 5, 7, 11, 13]
        else:
            v3 = [2, 3, 5, 7, 11, 13, 17]
    elif a1 < 3825123056546413051:
        v3 = [2, 3, 5, 7, 11, 13, 17, 19]
    else:
        v3 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for v4 in v3:
        v5 = pow(v4, v1, a1)
        if v5 == 1 or v5 == a1 - 1:
            continue
        for v6 in range(v2 - 1):
            v5 *= v5
            v5 %= a1
            if v5 == a1 - 1:
                break
        else:
            return False
    return True

def f3(a1):
    """Find a non-trivial factor of n by using Pollard's rho algorithm."""
    v1 = int(a1 ** 0.125) + 1
    v2 = 1
    while True:
        v3 = 1
        v4 = 1
        v5 = 1
        v6 = 1
        while v6 == 1:
            v7 = v3
            for v8 in range(v4):
                v3 = (v3 * v3 + v2) % a1
            for v9 in range(0, v4, v1):
                v10 = v3
                for v8 in range(v1):
                    v3 = (v3 * v3 + v2) % a1
                    v5 = v5 * (v7 - v3) % a1
                v6 = f1(v5, a1)
                if v6 != 1:
                    break
            else:
                v10 = v3
                for v8 in range(v4 - v9):
                    v3 = (v3 * v3 + v2) % a1
                    v5 = v5 * (v7 - v3) % a1
                v6 = f1(v5, a1)
            v4 *= 2
        if v6 == a1:
            v6 = 1
            while v6 == 1:
                v10 = (v10 * v10 + v2) % a1
                v6 = f1(v7 - v10, a1)
        if v6 == a1:
            v2 += 1
        else:
            return v6

def f4(a1):
    """計算量は O(n ^ 1/4) 程度。"""
    if a1 == 1:
        return []
    if f2(a1):
        return [a1]
    v1 = []
    for v2 in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        while a1 % v2 == 0:
            v1.append(v2)
            a1 //= v2
        if a1 == 1:
            return v1
    while a1 != 1 and (not f2(a1)):
        v4 = f3(a1)
        if f2(v4):
            while a1 % v4 == 0:
                v1.append(v4)
                a1 //= v4
        elif f2(a1 // v4):
            v1.append(a1 // v4)
            a1 = v4
        else:
            return sorted(v1 + f4(v4) + f4(a1 // v4))
    if a1 == 1:
        return sorted(v1)
    else:
        v1.append(a1)
        return sorted(v1)
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in v2:
    v3 = f1(v3, v4)
if v3 != 1:
    print('not coprime')
    exit()
v5 = set()
for v4 in v2:
    v6 = set(f4(v4))
    if v6 & v5:
        print('setwise coprime')
        exit()
    else:
        v5 |= v6
print('pairwise coprime')
