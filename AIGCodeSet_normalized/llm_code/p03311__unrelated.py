v1 = int(input())
v2 = list(map(int, input().split()))
v3 = float('inf')
for v4 in range(-10 ** 9, 10 ** 9 + 1):
    v5 = sum((abs(v2[i] - (v4 + i + 1)) for v6 in range(v1)))
    v3 = min(v3, v5)
print(v3)
