v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
sum = 0
v4 = 1
for v5 in range(0, v1):
    sum += v3[v5]
    if v2 < sum:
        print(v4)
        break
    else:
        v4 += 1
else:
    print(v4)
