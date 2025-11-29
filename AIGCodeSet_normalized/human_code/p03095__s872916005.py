v1 = 10 ** 9 + 7
v2 = int(input())
v3 = input().strip()
v4 = {chr(i): [] for v5 in range(97, 123)}
for v5 in range(v2):
    v4[v3[v5]].append(v5)
v6 = 1
for v7 in range(97, 123):
    v6 = v6 * (1 + len(v4[chr(v7)])) % v1
print((v6 - 1) % v1)
