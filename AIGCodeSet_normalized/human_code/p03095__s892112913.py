v1 = int(input())
v2 = input()
v3 = set(v2)
v4 = []
for v5 in v3:
    v4.append(v2.count(v5))
v6 = 1
for v5 in v4:
    v6 *= v5 + 1
    v6 %= 10 ** 9 + 7
print(v6 - 1)
