class C1:

    def countPrefixSuffixPairs(self, a1):

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.val = 0
        v1 = TrieNode()
        v2 = 0
        for v3 in a1:
            v4 = v1
            v5 = len(v3)
            for v6 in range(v5):
                v7 = v3[v6]
                v8 = v3[v5 - 1 - v6]
                v9 = (v7, v8)
                if v9 not in v4.children:
                    v4.children[v9] = TrieNode()
                v4 = v4.children[v9]
                v2 += v4.val
            v4.val += 1
        return v2
