import fractions
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 10 ** 9
for v4 in range(v1 - 1):
    if fractions.gcd(v2[v4], v2[v4 + 1]) < v3:
        v3 = fractions.gcd(v2[v4], v2[v4 + 1])
    if v3 == 1:
        print(v3)
        exit()
print(v3)
