v1, v2 = map(int, input().split())
v3 = v2 - v1

def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1
v4 = f1(v3, v1)
print(v4)
