def f1(a1, a2):
    return max(len(str(a1)), len(str(a2)))

def f2(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    v1.sort()
    return v1

def f3():
    v1 = int(input())
    v2 = f2(v1)
    v3 = 10 ** 10 + 1
    for v4 in v2:
        v3 = min(v3, f1(v4, v1 // v4))
    print(v3)
if __name__ == '__main__':
    f3()
