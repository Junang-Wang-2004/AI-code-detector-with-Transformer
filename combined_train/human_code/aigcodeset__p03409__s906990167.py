v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = [list(map(int, input().split())) for v3 in range(v1)]
v5 = 0
v2.sort(reverse=True, key=lambda x: (x[0], x[1]))
v4.sort(key=lambda x: (x[0], x[1]))

def f1(a1, a2):
    v1 = []
    v2 = []
    for v3 in a1:
        if v3 in v1:
            continue
        for v4 in a2:
            if v4 in v2:
                continue
            if v3[0] < v4[0] and v3[1] < v4[1]:
                v1.append(v3)
                v2.append(v4)
                break
    return len(v1)
v5 = f1(v2, v4)
v2.sort(reverse=True, key=lambda x: (x[1], x[0]))
v4.sort(key=lambda x: (x[1], x[0]))
v5 = max(v5, f1(v2, v4))
v2.sort(reverse=True, key=lambda x: (x[1], x[0]))
v4.sort(key=lambda x: (x[0], x[1]))
v5 = max(v5, f1(v2, v4))
v2.sort(reverse=True, key=lambda x: (x[0], x[1]))
v4.sort(key=lambda x: (x[1], x[0]))
v5 = max(v5, f1(v2, v4))
print(v5)
