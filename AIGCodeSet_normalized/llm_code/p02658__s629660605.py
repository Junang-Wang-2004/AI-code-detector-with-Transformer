v1 = int(input())
v2 = [int(x) for v3 in input().split() if v3 != '1']
sum = v2[0]
for v4 in range(1, len(v2)):
    sum = sum * v2[v4]
    if 0 in v2:
        sum = 0
        break
    elif sum > 10 ** 18:
        break
if sum > 10 ** 18:
    print(-1)
else:
    print(sum)
