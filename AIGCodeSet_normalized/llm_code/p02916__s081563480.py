v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
sum = 0
for v5 in range(len(v2)):
    sum += v3[v2[v5] - 1]
    if v5 != len(v2) - 1 and v2[v5] + 1 == v2[v5 + 1]:
        sum += v4[v2[v5] - 1]
print(sum)
