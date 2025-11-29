import sys
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readline
v4 = 10 ** 9 + 7
v5 = int(v2())
v6 = v2().decode()
v7 = len(v6)
v8 = v7 + v5
v9 = [1] * (v8 + 1)
v10 = [1] * (v8 + 1)
for v11 in range(1, v8 + 1):
    v9[v11] = v9[v11 - 1] * v11 % v4
v10[v8] = pow(v9[v8], v4 - 2, v4)
for v11 in range(v8, 0, -1):
    v10[v11 - 1] = v11 * v10[v11] % v4

def f1(a1, a2):
    return v9[a1] * v10[a2] * v10[a1 - a2] % v4
v12 = 0
for v11 in range(v5 + 1):
    v12 += f1(v11 + v7 - 1, v7 - 1) * pow(25, v11, v4) % v4 * pow(26, v5 - v11, v4) % v4
print(v12 % v4)
