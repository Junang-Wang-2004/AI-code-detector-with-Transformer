v1 = int(input())
sum = 0
for v2 in range(1, v1 + 1):
    sum += v2
    if sum >= v1:
        break
print(v2)
