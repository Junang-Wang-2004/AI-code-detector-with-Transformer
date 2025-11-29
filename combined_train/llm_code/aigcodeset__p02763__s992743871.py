def f1(a1, a2):
    v1 = 0
    a2 = a2 + 1
    while a2 > 0:
        v1 += a1[a2]
        a2 -= a2 & -a2
    return v1

def f2(a1, a2, a3, a4):
    a3 += 1
    while a3 <= a2:
        a1[a3] += a4
        a3 += a3 & -a3

def f3(a1, a2):
    v1 = [0] * (a2 + 1)
    for v2 in range(a2):
        f2(v1, a2, v2, a1[v2])
    return v1
v1 = int(input())
v2 = input()
v3 = [f3([0] * (v1 + 1), v1 + 1) for v4 in range(26)]
for v4 in range(v1):
    f2(v3[ord(v2[v4]) - 97], v1, v4, 1)
for v5 in range(int(input())):
    v6 = list(input().split())
    if v6[0] == '1':
        f2(v3[ord(v2[int(v6[1]) - 1]) - 97], v1, int(v6[1]) - 1, -1)
        v2 = v2[:int(v6[1]) - 1] + v6[2] + v2[int(v6[1]):]
        f2(v3[ord(v6[2]) - 97], v1, int(v6[1]) - 1, 1)
    else:
        v7 = 0
        v8, v9 = (int(v6[1]) - 1, int(v6[2]) - 1)
        for v4 in range(26):
            if f1(v3[v4], v9) - f1(v3[v4], v8 - 1) > 0:
                v7 += 1
        print(v7)
