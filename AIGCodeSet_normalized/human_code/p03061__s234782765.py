v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0]
v4 = [0]
import fractions

def f1(a1, a2):
    if a1 * a2 != 0:
        return fractions.gcd(a1, a2)
    else:
        return max(a1, a2)
for v5 in range(v1 - 1):
    v6 = v2[v5]
    v7 = v2[-v5 - 1]
    v3.append(f1(v3[v5], v6))
    v4.append(f1(v4[v5], v7))
v8 = 0
for v5 in range(v1):
    v6 = v3[v5]
    v7 = v4[-v5 - 1]
    v8 = max(f1(v6, v7), v8)
print(v8)
