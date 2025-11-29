v1, v2 = map(int, input().split())

def f1(a1, a2):
    v1 = 0
    if a1 == 1:
        v1 += 300000
    elif a1 == 2:
        v1 += 200000
    elif a1 == 3:
        v1 += 100000
    if a2 == 1:
        v1 += 300000
    elif a2 == 2:
        v1 += 200000
    elif a2 == 3:
        v1 += 100000
    if a1 == 1 and a2 == 1:
        v1 += 400000
    print(v1)
f1(v1, v2)
