def f1(a1, a2, a3):
    v1 = 0
    for v2 in range(3):
        v3 = a3[v2]
        for v4 in range(len(a1[v2])):
            v1 += a1[v2][v4] * a2[v4][v3]
    return v1

def f2():
    v1, v2 = map(int, input().split())
    v3 = [list(map(int, input().split())) for v4 in range(v2)]
    v5 = [list(map(int, input().split())) for v4 in range(v1)]
    v6 = [[0] * v2 for v4 in range(3)]
    for v7 in range(v1):
        for v8 in range(v1):
            v6[(v7 + v8) % 3][v5[v7][v8] - 1] += 1
    v9 = float('inf')
    for v10 in range(v2):
        for v11 in range(v2):
            if v10 == v11:
                continue
            for v12 in range(v2):
                if v10 == v12 or v11 == v12:
                    continue
                v9 = min(v9, f1(v6, v3, [v10, v11, v12]))
    print(v9)
if __name__ == '__main__':
    f2()
