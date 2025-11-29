def f1():
    v1, v2 = map(int, input().split())
    v3 = []
    for v4 in range(v1):
        v5, v6 = map(int, input().split())
        v3.append((v5, v6))
    v3.sort(key=lambda x: x[1] / x[0], reverse=True)
    v7 = 0
    v8 = 0
    for v5, v6 in v3:
        if v7 + v5 <= v2 - 0.5:
            v7 += v5
            v8 += v6
        else:
            break
    return v8
print(f1())
