v1 = int(input())
v2 = list(map(int, input().split()))

def f1(a1):
    v1 = True
    for v2 in a1:
        if v2 % 2 != 0:
            v1 = False
            break
    return v1
v3 = 0
v4 = f1(v2)
if v4:
    while v4:
        v4 = f1(v2)
        v3 = v3 + 1
        v2 = [c // 2 for v5 in v2]
    print(v3)
else:
    print(0)
