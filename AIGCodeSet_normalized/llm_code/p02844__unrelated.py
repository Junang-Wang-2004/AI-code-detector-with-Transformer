v1 = int(input())
v2 = input()
v3 = set()
for v4 in range(v1 - 2):
    v5 = v2[:v4] + v2[v4 + 3:]
    v3.add(v5)
print(len(v3))
