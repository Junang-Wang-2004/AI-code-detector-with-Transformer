class C1:

    def longestValidSubstring(self, a1, a2):

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.is_end = False
        v1 = TrieNode()
        for v2 in a2:
            v3 = v1
            for v4 in v2:
                if v4 not in v3.children:
                    v3.children[v4] = TrieNode()
                v3 = v3.children[v4]
            v3.is_end = True
        v5 = len(a1)
        v6 = 0
        v7 = v5 - 1
        for v8 in range(v5 - 1, -1, -1):
            v3 = v1
            for v9 in range(v8, v7 + 1):
                v10 = a1[v9]
                if v10 not in v3.children:
                    break
                v3 = v3.children[v10]
                if v3.is_end:
                    v7 = v9 - 1
                    break
            v6 = max(v6, v7 - v8 + 1)
        return v6
