v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    v3 += abs(v2[v4])
print(v3)
