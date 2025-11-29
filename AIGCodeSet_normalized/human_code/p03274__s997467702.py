v1 = 300000001
v2, v3 = map(int, input().split())
v4 = [int(i) for v5 in input().split()]

def f1():
    if 0 <= v4[0]:
        print(v4[v3 - 1])
        return
    if v4[v2 - 1] < 0:
        print(abs(v4[v2 - v3]))
        return
    v1 = v1
    for v2 in range(v2 - v3 + 1):
        v1 = min(v1, 2 * abs(v4[v2]) + abs(v4[v2 + v3 - 1]), abs(v4[v2]) + 2 * abs(v4[v2 + v3 - 1]))
    print(v1)
    return
f1()
