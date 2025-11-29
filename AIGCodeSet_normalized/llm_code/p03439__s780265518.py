v1 = int(input())
v2 = [0 for v3 in range(v1)]

def f1(a1):
    print(a1, flush=True)

def f2(a1):
    v1 = input()
    if v1 == 'Vacant':
        exit()
    elif v1 == 'Male':
        v2[a1] = 1
    else:
        v2[a1] = 2
f1(0)
f2(0)
f1(v1 - 1)
f2(v1 - 1)
v4 = 0
v5 = v1 - 1
v6 = 0
while True:
    v7 = (v4 + v5) // 2
    f1(v7)
    f2(v7)
    if (v7 - v4) % 2 == 1 and v2[v7] != v2[v4] or ((v7 - v4) % 2 == 0 and v2[v7] == v2[v4]):
        v5 = v7
    else:
        v4 = v7
    v6 += 1
    if v6 >= 30:
        exit()
