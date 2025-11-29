import math
v1, v2 = map(int, input().split())
for v3 in range(1, v2 + 1):
    v4 = math.factorial(v1 - v2 + 1) // (math.factorial(v3) * math.factorial(v1 - v2 + 1 - v3))
    v5 = math.factorial(v2 - 1) // (math.factorial(v3 - 1) * math.factorial(v2 - v3))
    print(v4 * v5 % (pow(10, 9) + 7))
