v1 = int(input())
v2 = [0] * v1
v3 = input().split(' ')
v4 = [int(s) for v5 in v3]
for v6 in v4:
    v2[v6 - 1] += 1
print(v2)
