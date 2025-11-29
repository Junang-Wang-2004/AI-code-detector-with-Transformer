import math
v1 = int(input())
v2 = int((math.log10(v1) - 2) / math.log10(1.01)) - 1
v3 = 100
while v3 < v1:
    v2 += 1
    v3 = 100
    for v4 in range(v2):
        v3 += int(v3 * 0.01)
print(v2)
