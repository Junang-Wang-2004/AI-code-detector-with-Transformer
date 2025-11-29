v1 = int(input())
v2 = input().split(' ')

def f1(a1, a2):
    v1 = 1
    v2 = 10 ** 18
    if '0' in a2:
        return print(0)
    else:
        for v3 in range(a1):
            v1 *= int(a2[v3])
            v2 /= int(a2[v3])
            if v2 < 0:
                return print(-1)
        return print(v1)
f1(v1, v2)
