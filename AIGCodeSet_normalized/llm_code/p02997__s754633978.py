import math

def f1(a1, a2):
    return math.factorial(a1) // (math.factorial(a1 - a2) * math.factorial(a2))
v1, v2 = map(int, input().split())
v3 = f1(v1 - 1, 2)
if v2 < v1 - 1 and v3 < v2:
    print('-1')
    quit()
for v4 in range(2, v1 + 1):
    print('1', str(v4))
v5 = v2
v3 = 2
v6 = 3
while v5 > 0:
    print(v3, v6)
    v6 += 1
    if v6 > v1:
        v3 += 1
        v6 = v3 + 1
    v5 -= 1
