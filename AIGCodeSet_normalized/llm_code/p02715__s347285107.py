v1, v2 = list(map(int, input().split()))
v3 = 0
sum = 0
for v4 in range(1, v2 + 1):
    v3 = v2 // v4
    sum += v3 ** v1 * v4
    if v3 > 1:
        for v5 in range(1, v3):
            sum -= (v2 // ((v5 + 1) * v4)) ** v1 * v4
print(sum % (10 ** 9 + 7))
