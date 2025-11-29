v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
sum = 0
v4 = 0
for v5 in range(v1):
    v6 = 0
    while v4 < v1 and sum ^ v2[v4] == sum + v2[v4]:
        sum = sum ^ v2[v4]
        v4 += 1
    if v5 == v4:
        v4 += 1
    else:
        sum = sum ^ v2[v5]
    v3 += v4 - v5
print(v3)
