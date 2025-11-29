class C1:

    def __init__(self, a1, a2, a3):
        self.from_node = a1
        self.to_node = a2
        self.cost = a3
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5, v6, v7 = map(int, input().split())
    v5, v6 = (v5 - 1, v6 - 1)
    v3.append(C1(v6, v5, -v7))

def f1(a1):
    v1 = 10 ** 30
    v2 = [v1] * v1
    v2[a1] = 0
    for v3 in range(v1):
        v4 = False
        for v5 in v3:
            if v2[v5.from_node] != v1 and v2[v5.to_node] > v2[v5.from_node] + v5.cost:
                v2[v5.to_node] = v2[v5.from_node] + v5.cost
                v4 = True
        if not v4:
            return (v2, True)
    return (0, False)
v8, v9 = f1(v1 - 1)
if v9:
    print(-v8[0])
else:
    print('in')
