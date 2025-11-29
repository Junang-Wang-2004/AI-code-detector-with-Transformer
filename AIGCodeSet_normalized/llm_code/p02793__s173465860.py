import fractions
v1 = 1000000007

def f1(a1, a2):
    return (a1 + a2) % v1
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = v3[0]
v5 = 0
for v6 in range(1, v2):
    v4 = v4 * v3[v6] // fractions.gcd(v4, v3[v6])
for v7 in range(0, v2):
    v5 = f1(v5, v4 // v3[v7])
print(int(v5))
