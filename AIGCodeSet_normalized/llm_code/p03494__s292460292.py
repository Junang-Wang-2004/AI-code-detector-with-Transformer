v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
while all([i % 2 == 0 for v4 in v2]):
    v2 = [v4 // 2 for v4 in v2]
    v3 += 1
print(v3)
