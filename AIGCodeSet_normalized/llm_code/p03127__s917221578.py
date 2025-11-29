def f1(a1):
    while 0 in a1:
        a1.remove(0)
    return a1

def f2():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v2 = sorted(v2)
    while True:
        for v3 in range(1, len(v2)):
            v2[v3] = v2[v3] % v2[0]
        v2 = f1(v2)
        v2 = sorted(v2)
        if len(v2) == 2:
            v4 = int(abs(v2[1] - v2[0]))
            v2[0] = v4
            v2.remove(v2[1])
        if len(v2) == 1:
            break
    print(v2[0])
f2()
