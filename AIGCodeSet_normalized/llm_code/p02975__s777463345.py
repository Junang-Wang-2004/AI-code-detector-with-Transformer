v1 = int(input())
v2 = list(map(int, input().split()))

def f1(a1):
    v1 = bin(a1)[2:]
    return '0' * (30 - len(v1)) + v1

def f2(a1, a2):
    return a1[a2:] + a1[:a2]

def f3(a1):
    v1 = []
    v2 = 0
    while v2 < len(a1):
        v3 = a1[v2]
        v4 = v2
        while v4 < v1 and a1[v4] == v3:
            v4 += 1
        v1.append((v3, v4 - v2))
        v2 = v4
    return v1
v3 = [f1(a) for v4 in v2]
for v5 in zip(*v3):
    v6 = 0
    while v6 < v1 and v5[v6] == '1':
        v6 += 1
    for v7, v8 in f3(f2(v5, v6)):
        if v7 == '1' and v8 % 3 != 0:
            print('No')
            exit()
print('Yes')
