v1, v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
if v1 <= v2:
    print(0)
else:
    v3.sort()
    sum = 0
    for v4 in range(0, v1 - v2):
        sum += v3[v4]
    print(sum)
