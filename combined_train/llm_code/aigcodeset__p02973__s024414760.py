from bisect import bisect
v1 = int(input())
v2 = [0] * v1
for v3 in range(v1):
    v2[v3] = int(input())

def f1():
    v1 = len(v2)
    v2 = [10 ** 10] * (v1 + 1)
    v2[0] = -1
    v3 = [0] * (v1 + 1)
    for v4 in range(v1):
        v5 = bisect(v2, v2[v4] - 1)
        if v2[v5] == 10 ** 10:
            if v2[v5] > v2[v4]:
                v2[v5] = v2[v4]
                v3[v5] = v4
            v6 = v2[1:v5 + 1]
            v7 = v3[1:v5 + 1]
        elif v2[v5] > v2[v4]:
            v2[v5] = v2[v4]
            v3[v5] = v4
    for v4 in range(len(v7) - 1, -1, -1):
        del v2[v7[v4]]
v4 = 0
while len(v2) > 0:
    f1()
    v4 += 1
print(v4)
