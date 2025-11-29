v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * v1
for v4 in range(v1 - 1):
    v3[v2[v4] - 1] += 1
for v4 in range(v1):
    print(v3[v4])
