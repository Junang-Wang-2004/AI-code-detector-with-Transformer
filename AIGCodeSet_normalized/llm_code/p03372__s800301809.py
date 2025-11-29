v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]

class C1(object):
    __slots__ = ['elem_size', 'tree', 'default', 'op']

    def __init__(self, a1: list, a2: int, a3):
        from math import ceil, log
        v1 = len(a1)
        self.elem_size = v2 = 1 << ceil(log(v1, 2))
        self.tree = v3 = [a2] * (v2 * 2)
        v3[v2:v2 + v1] = a1
        self.default = a2
        self.op = a3
        for v4 in range(v2 - 1, 0, -1):
            v3[v4] = a3(v3[v4 << 1], v3[(v4 << 1) + 1])

    def get_value(self, a1: int, a2: int) -> int:
        v1, v2 = (a1 + self.elem_size, a2 + self.elem_size)
        v3, v4, v5 = (self.tree, self.default, self.op)
        while v1 < v2:
            if v1 & 1:
                v4 = v5(v3[v1], v4)
                v1 += 1
            if v2 & 1:
                v2 -= 1
                v4 = v5(v3[v2], v4)
            v1, v2 = (v1 >> 1, v2 >> 1)
        return v4

    def set_value(self, a1: int, a2: int) -> None:
        v1 = self.elem_size + a1
        self.tree[v1] = a2
        self.update(v1)

    def update(self, a1: int) -> None:
        v1, v2 = (self.op, self.tree)
        while a1 > 1:
            a1 >>= 1
            v2[a1] = v1(v2[a1 << 1], v2[(a1 << 1) + 1])
v5 = [[0, 0, 0]]
for v4 in range(v1):
    v6, v7 = v3[v4]
    v8 = v5[-1][0] + v7 - (v6 + v5[-1][1])
    v5.append([v8, -v6, v4 + 1])
v9 = [[0, 0] for v4 in range(v1 + 1)]
v9[-2] = [v3[-1][1] - (v2 - v3[-1][0]), v3[-1][0]]
for v4 in range(2, v1 + 1):
    v6, v7 = v3[-v4]
    v8 = v9[-v4][0] + v7 - (v9[-v4][1] - v6)
    v9[-v4 - 1] = [v8, v6]
v9[-1][1] = v2
v10 = sorted(v5, reverse=True)
v11 = 0
v12 = [[0] * 2 for v4 in range(v1 + 1)]
for v4 in range(v1, 0, -1):
    if v4 >= v10[v11][2]:
        v12[v4] = [v10[v11][0], v10[v11][1]]
    else:
        while v4 < v10[v11][2]:
            v11 += 1
        v12[v4] = [v10[v11][0], v10[v11][1]]
v13 = 0
for v4 in range(v1 + 1):
    v14 = v9[v4][0] + v12[v4][0] - min(v2 - v9[v4][1], -v12[v4][1])
    v13 = max(v13, v14)
print(v13)
