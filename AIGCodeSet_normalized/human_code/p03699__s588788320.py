v1 = int(input())
v2 = []
sum = 0
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
for v4 in range(v1):
    sum = sum + v2[v4]
if sum % 10 != 0:
    print(sum)
else:
    for v5 in range(v1):
        if v2[v5] % 10 != 0:
            sum = sum - v2[v5]
            break
        else:
            pass
    if sum % 10 == 0:
        sum = 0
    else:
        pass
    print(sum)
