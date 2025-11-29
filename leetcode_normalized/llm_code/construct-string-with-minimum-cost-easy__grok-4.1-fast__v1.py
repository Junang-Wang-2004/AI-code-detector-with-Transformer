class C1:

    def minimumCost(self, a1, a2, a3):
        v1 = float('inf')
        v2 = len(a1)

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.minc = v1
        v3 = TrieNode()
        v4 = len(a2)
        for v5 in range(v4):
            v6 = v3
            v7 = a2[v5]
            v8 = a3[v5]
            for v9 in v7:
                if v9 not in v6.children:
                    v6.children[v9] = TrieNode()
                v6 = v6.children[v9]
            v6.minc = min(v6.minc, v8)
        v10 = [v1] * (v2 + 1)
        v10[0] = 0
        for v11 in range(v2):
            if v10[v11] == v1:
                continue
            v6 = v3
            for v5 in range(v11, v2):
                v9 = a1[v5]
                if v9 not in v6.children:
                    break
                v6 = v6.children[v9]
                if v6.minc != v1:
                    v10[v5 + 1] = min(v10[v5 + 1], v10[v11] + v6.minc)
        return v10[v2] if v10[v2] != v1 else -1
