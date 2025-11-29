v1 = int(input())
v2 = [0] * (v1 + 1)
for v3 in range(2, v1 + 1):
    v4 = v3
    for v5 in range(2, v3 + 1):
        while v4 % v5 == 0:
            v2[v5] += 1
            v4 //= v5

def f1(a1):
    return len(list(filter(lambda x: x >= a1 - 1, v2)))
print(f1(75) + f1(25) * (f1(3) - 1) + f1(15) * (f1(5) - 1) + f1(5) * (f1(5) - 1) * (f1(3) - 2) // 2)
