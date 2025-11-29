v1, v2 = [int(n) for v3 in input().split()]
v4 = input()
v5 = []

def f1(a1):
    v1 = v2
    while v1 > 0:
        if v1 >= a1:
            v5.append(a1)
            return True
        if v4[a1 - v1] == '1':
            if v1 == 1:
                return False
            v1 -= 1
            continue
        a1 -= v1
        if f1(a1) == False:
            v1 -= 1
        else:
            v5.append(v1)
            return True
if f1(v1):
    print(' '.join([str(v3) for v3 in v5[::-1]]))
else:
    print(-1)
