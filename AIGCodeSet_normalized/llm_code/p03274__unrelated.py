v1 = int(input())
v2 = int(input())
v3 = list(map(int, input().split()))

def f1(a1, a2):
    v1 = 0
    for v2 in range(a2):
        v1 += abs(a1[v2] - a1[v2 - 1])
    return v1
print(f1(v3, v2))
