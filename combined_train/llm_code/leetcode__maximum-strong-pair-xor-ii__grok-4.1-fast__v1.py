class C1:

    def maximumStrongPairXor(self, a1):
        a1.sort()

        class TrieNode:

            def __init__(self):
                self.children = [None, None]
                self.count = 0
        v1 = TrieNode()

        def insert(a1, a2, a3):
            v1 = a1
            for v2 in range(31, -1, -1):
                v3 = a2 >> v2 & 1
                if v1.children[v3] is None:
                    v1.children[v3] = TrieNode()
                v1 = v1.children[v3]
                v1.count += a3

        def get_max_xor(a1, a2):
            v1 = a1
            v2 = 0
            for v3 in range(31, -1, -1):
                v4 = a2 >> v3 & 1
                v5 = 1 - v4
                if v1.children[v5] and v1.children[v5].count > 0:
                    v2 |= 1 << v3
                    v1 = v1.children[v5]
                elif v1.children[v4] and v1.children[v4].count > 0:
                    v1 = v1.children[v4]
                else:
                    break
            return v2
        v2 = 0
        v3 = 0
        for v4 in range(len(a1)):
            insert(v1, a1[v4], 1)
            while v3 <= v4 and a1[v4] > 2 * a1[v3]:
                insert(v1, a1[v3], -1)
                v3 += 1
            v2 = max(v2, get_max_xor(v1, a1[v4]))
        return v2
