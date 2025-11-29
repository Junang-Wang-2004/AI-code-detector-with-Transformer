from fractions import gcd
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0]
v4 = [0]
v5 = []
v6 = 0
for v7 in range(v1):
    v3.append(gcd(v2[v7], v3[-1]))
    v4.append(gcd(v2[-v7 - 1], v4[-1]))
v4.reverse()
for v7 in range(v1):
    v5.append(gcd(v3[v7], v4[v7 + 1]))
for v7 in range(v1):
    v6 = max(v6, v5[v7])
print(v6)
