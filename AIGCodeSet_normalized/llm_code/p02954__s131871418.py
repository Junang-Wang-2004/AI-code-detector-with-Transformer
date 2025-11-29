v1 = input()
v2 = len(v1)
v3 = [1] * v2
v4 = [1] * v2

def f1(a1):
    for v1 in range(v2):
        if a1[v1] == 'R' and v3[v1] != 0:
            v3[v1 + 1] += 1
            v3[v1] -= 1
        elif a1[v1] == 'L' and v3[v1] != 0:
            v3[v1 - 1] += 1
            v3[v1] -= 1
for v5 in range(10 ** 100):
    f1(v1)
print(*v3)
