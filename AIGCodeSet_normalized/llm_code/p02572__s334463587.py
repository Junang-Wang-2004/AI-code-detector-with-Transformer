v1 = int(input())
v2 = list(map(int, input().split()))
sum = 0
for v3 in range(1, v1):
    sum += v2[v3 - 1] * v2[v3]
    sum = sum % (10 ** 9 + 7)
print(sum)
