v1 = int(input())
sum = 0
for v2 in range(v1):
    v3, v4 = map(int, input().split())
    sum += v4 - v3 + 1
print(sum)
