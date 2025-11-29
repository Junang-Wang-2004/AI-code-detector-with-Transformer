v1, v2 = (int(i) for v3 in input().split())
sum = 0
if v1 == 1:
    sum += 300000
elif v1 == 2:
    sum += 200000
elif v1 == 3:
    sum += 100000
else:
    sum += 0
if v2 == 1:
    sum += 300000
elif v2 == 2:
    sum += 200000
elif v2 == 3:
    sum += 100000
else:
    sum += 0
if v1 == 1 and v2 == 1:
    sum += 400000
print(sum)
