def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = []
    for v4 in range(v1):
        for v5 in range(v1):
            if v4 != v5:
                v3.append(f2(v2[v4], v2[v5]))
    print(sum(v3))

def f2(a1, a2):
    return a1 * a2
f1()
