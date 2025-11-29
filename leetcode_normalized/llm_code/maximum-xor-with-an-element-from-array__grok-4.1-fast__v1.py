class C1:

    def __init__(self, a1):
        self.bits = a1
        self.nodes = [[-1, -1]]
        self.next_node = 1

    def add(self, a1):
        v1 = 0
        for v2 in range(self.bits - 1, -1, -1):
            v3 = a1 >> v2 & 1
            if self.nodes[v1][v3] == -1:
                self.nodes[v1][v3] = self.next_node
                self.nodes.append([-1, -1])
                self.next_node += 1
            v1 = self.nodes[v1][v3]

    def find_max_xor(self, a1):
        if self.nodes[0][0] == -1 and self.nodes[0][1] == -1:
            return -1
        v1 = 0
        v2 = 0
        for v3 in range(self.bits - 1, -1, -1):
            v4 = a1 >> v3 & 1
            v5 = 1 - v4
            if self.nodes[v1][v5] != -1:
                v2 |= 1 << v3
                v1 = self.nodes[v1][v5]
            else:
                v1 = self.nodes[v1][v4]
        return v2

class C2:

    def maximizeXor(self, a1, a2):
        a1.sort()
        if not a1:
            return [-1] * len(a2)
        v1 = max(a1[-1], max((q[0] for v2 in a2)))
        v3 = v1.bit_length()
        v4 = sorted(enumerate(a2), key=lambda e: e[1][1])
        v5 = C1(v3)
        v6 = [-1] * len(a2)
        v7 = 0
        for v8, (v9, v10) in v4:
            while v7 < len(a1) and a1[v7] <= v10:
                v5.add(a1[v7])
                v7 += 1
            v6[v8] = v5.find_max_xor(v9)
        return v6
