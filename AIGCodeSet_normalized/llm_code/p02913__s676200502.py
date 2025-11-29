import sys

def f1():
    return sys.stdin.readline()[:-1]
v1 = int(f1())
v2 = f1()
v3 = 0
for v4 in range(len(v2)):
    v5 = v2[v4:]
    v6 = [0] * len(v5)
    v7 = len(v5)
    v8 = 0
    v9 = 0
    for v10 in range(1, v7):
        if v10 > v9:
            v8 = v10
            v9 = v10
            while v9 < v7 and v5[v9 - v8] == v5[v9]:
                v6[v10] = v9 - v8 + 1
                if v6[v10] > v10:
                    v6[v10] = v10
                    break
                v9 += 1
        else:
            v11 = v10 - v8
            if v6[v11] < v9 - v10 + 1:
                if v6[v11] <= v10:
                    v6[v10] = v6[v11]
                else:
                    v6[v10] = v10
            else:
                v8 = v10
                while v9 < v7 and v5[v9 - v8] == v5[v9]:
                    v6[v10] = v9 - v8 + 1
                    if v6[v10] > v10:
                        v6[v10] = v10
                        break
                    v9 += 1
    v12 = max(v6)
    if v12 > v3:
        v3 = max(v6)
print(v3)
