v1 = int(input())
v2 = list(map(int, input().split()))
sum = v2[0]
for v3 in range(v1 - 1):
    if v2[v3 + 1] > v2[v3]:
        sum += v2[v3 + 1] - v2[v3]
print(sum)
