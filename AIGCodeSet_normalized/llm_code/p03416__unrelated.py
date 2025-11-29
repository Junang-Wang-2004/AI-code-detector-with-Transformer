def f1(a1):
    return str(a1) == str(a1)[::-1]
v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(v1, v2 + 1):
    if f1(v4):
        v3 += 1
print(v3)
