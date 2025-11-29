v1 = 10 ** 9 + 7
v2 = 1000002
v3 = [1] * (v2 + 1)
v4 = [1] * (v2 + 1)
for v5 in range(2, v2 + 1):
    v3[v5] = v3[v5 - 1] * v5 % v1
    v4[v5] = v4[v5 - 1] * pow(v5, v1 - 2, v1) % v1

def f1(a1, a2, a3):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return v3[a1] * v4[a2] * v4[a1 - a2] % a3

def f2():
    v1 = int(input())
    v2 = input()
    v3 = len(v2)
    v4 = 0
    v5 = 1
    v6 = pow(26, v1, v1)
    v7 = pow(26, v1 - 2, v1)
    for v8 in range(v1 + 1):
        v4 += f1(v8 + v3 - 1, v8, v1) * v5 * v6
        v4 %= v1
        v5 = v5 * 25 % v1
        v6 = v6 * v7 % v1
    print(v4)
if __name__ == '__main__':
    f2()
