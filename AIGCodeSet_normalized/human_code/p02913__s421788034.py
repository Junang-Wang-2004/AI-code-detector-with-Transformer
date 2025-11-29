v1 = 9973
v2 = 2 ** 61 - 1

class C1:

    def __init__(self, a1):
        self.acc = [0]
        v1 = 0
        for v2, v3 in enumerate(a1):
            v4 = ord(v3) - ord('a') + 1
            v5 = pow(v1, v2, v2)
            v1 = (v1 + v4 * v5) % v2
            self.acc.append(v1)

    def hash(self, a1, a2):
        v1 = pow(v1, a1, v2)
        v2 = pow(v1, v2 - 2, v2)
        return (self.acc[a2] - self.acc[a1]) * v2 % v2
v3 = int(input())
v4 = input()
v5 = C1(v4)
v6 = 0
v7 = v3
while v7 - v6 > 1:
    v8 = (v6 + v7) // 2
    v9 = set()
    v10 = False
    for v11 in range(v8, v3):
        v12 = v11 + v8
        if v12 > v3:
            break
        v9.add(v5.hash(v11 - v8, v11))
        if v5.hash(v11, v12) in v9:
            v10 = True
    if v10:
        v6 = v8
    else:
        v7 = v8
v13 = v6
print(v13)
