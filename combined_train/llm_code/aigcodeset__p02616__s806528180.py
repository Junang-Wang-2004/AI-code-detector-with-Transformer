import sys

def f1():
    v1, v2 = list(map(int, sys.stdin.readline().split()))
    v3 = list(map(int, sys.stdin.readline().split()))
    v4 = []
    v5 = []
    v6 = 10 ** 9 + 7
    for v7 in v3:
        if v7 >= 0:
            v4.append(v7)
        else:
            v5.append(v7)
    v4.sort(reverse=True)
    v5.sort()
    if not v4:
        v8 = 1
        for v9 in range(len(v5) - v2, len(v5)):
            v8 *= v5[v9]
            v8 %= v6
        print(v8)
        return
    if not v5:
        v8 = 1
        for v9 in range(v2):
            v8 *= v4[v9]
            v8 %= v6
        print(v8)
        return
    v10 = []
    v11 = 0
    v12 = 0
    while len(v10) < v2 and v11 < len(v4) and (v12 < len(v5)):
        if v2 - len(v10) == 1:
            v10.append(v4[v11])
            v11 += 1
            break
        if v12 + 1 < len(v5):
            if v11 + 1 < len(v4):
                if abs(v4[v11] * v4[v11 + 1]) > abs(v5[v12] * v5[v12 + 1]):
                    v10.append(v4[v11])
                    v11 += 1
                else:
                    v10.extend([v5[v12], v5[v12 + 1]])
                    v12 += 2
            else:
                v10.extend([v5[v12], v5[v12 + 1]])
                v12 += 2
        else:
            v10.append(v4[v11])
            v11 += 1
    v8 = 1
    for v9 in range(v2):
        v8 *= v10[v9]
        v8 %= v6
    print(v8)
    return
if __name__ == '__main__':
    f1()
