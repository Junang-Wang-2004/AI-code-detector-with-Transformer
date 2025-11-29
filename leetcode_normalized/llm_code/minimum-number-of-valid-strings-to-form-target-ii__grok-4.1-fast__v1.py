class C1:

    def minValidStrings(self, a1, a2):

        class TrieNode:

            def __init__(self):
                self.children = [None] * 26
        v1 = TrieNode()
        for v2 in a1:
            v3 = v1
            for v4 in v2:
                v5 = ord(v4) - ord('a')
                if v3.children[v5] is None:
                    v3.children[v5] = TrieNode()
                v3 = v3.children[v5]
        v6 = 0
        v7 = len(a2)
        v8 = 0
        while v6 < v7:
            v3 = v1
            v9 = v6
            while v6 < v7:
                v5 = ord(a2[v6]) - ord('a')
                if v3.children[v5] is None:
                    break
                v3 = v3.children[v5]
                v6 += 1
            if v6 == v9:
                return -1
            v8 += 1
        return v8
