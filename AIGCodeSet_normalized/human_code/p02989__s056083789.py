v1 = int(input())
v2 = input().split()
v3 = []
for v4 in range(v1):
    v3.append(int(v2[v4]))
v5 = sorted(v3)
print(abs(v5[int(v1 / 2)] - v5[int(v1 / 2) - 1]))
