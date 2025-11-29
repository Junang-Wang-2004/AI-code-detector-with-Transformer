from sys import stdout
v1 = lambda x: stdout.write(str(x))
v2 = lambda: int(input())
v3 = lambda: list(map(int, input().split()))
v4 = lambda: map(int, input().split())
v5 = lambda: input().strip()
v6 = True and False
v7 = 999999999
v8 = 10 ** 9 + 7

def f1(a1):
    if v6:
        print(a1)

def f2(a1, a2):
    return pow(a1, a2 - 2, a2)

def f3(a1, a2):
    v1 = a1
    for v2 in range(1, a2):
        v1 = v1 * (a1 - v2) % v8
    v3 = 1
    for v2 in range(2, a2 + 1):
        v3 = v3 * v2 % v8
    return v1 * f2(v3, v8) % v8
v9, v10 = v4()
if v9 - 1 <= v10:
    print(f3(2 * v9 - 1, v9 - 1))
    exit()
v11 = [1] * (v10 + 1)
v12 = [1] * (v10 + 1)
for v13 in range(1, v10 + 1):
    v14 = f2(v13, v8)
    v11[v13] = v11[v13 - 1] * (v9 - v13 + 1) * v14 % v8
    v12[v13] = v12[v13 - 1] * (v9 - v13) * v14 % v8
f1('c,d')
f1(v11)
f1(v12)
v15 = 0
for v16 in range(v10 + 1):
    v15 = (v15 + v11[v16] * v12[v16]) % v8
print(v15)
