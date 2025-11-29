def f1(a1, a2):
    return max(a1[:a2 - 1] + a1[a2 + 1:])

def f2():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    for v3 in range(1, v1 + 1):
        print(f1(v2, v3))
f2()
