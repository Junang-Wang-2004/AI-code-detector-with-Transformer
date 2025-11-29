v1 = int(input())
v2 = map(int, input().split())
v3 = map(int, input().split())
sum = 0
for v4, v5 in zip(v2, v3):
    if v4 - v5 > 0:
        sum += v4 - v5
print(sum)
