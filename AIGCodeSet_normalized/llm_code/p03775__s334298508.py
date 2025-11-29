from math import sqrt
v1 = int(input())
v2 = []
for v3 in range(1, int(sqrt(v1)) + 1):
    if v3 * (v1 // v3) == v1:
        v2.append(max(len(str(v3)), len(str(v1 // v3))))
print(min(v2))
