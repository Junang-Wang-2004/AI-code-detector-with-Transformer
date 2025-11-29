class C1(object):

    def stringIndices(self, a1, a2):
        v1 = float('inf')

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.minpair = (v1, v1)
        v2 = TrieNode()
        for v3, v4 in enumerate(a1):
            v5 = len(v4)
            v6 = v2
            v6.minpair = min(v6.minpair, (v5, v3))
            for v7 in range(v5 - 1, -1, -1):
                v8 = v4[v7]
                if v8 not in v6.children:
                    v6.children[v8] = TrieNode()
                v6 = v6.children[v8]
                v6.minpair = min(v6.minpair, (v5, v3))
        v9 = []
        for v10 in a2:
            v6 = v2
            v11 = len(v10)
            for v7 in range(v11 - 1, -1, -1):
                v8 = v10[v7]
                if v8 not in v6.children:
                    break
                v6 = v6.children[v8]
            v12, v13 = v6.minpair
            v9.append(int(v13))
        return v9
