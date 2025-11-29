v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sum(v2)
v4 = abs(v3 - 2 * v2[0])
for v5 in range(1, v1):
    v4 = min(v4, abs(v3 - 2 * sum(v2[:v5])))
print(v4)
