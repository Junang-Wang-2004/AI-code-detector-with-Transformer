class C1(object):

    def __init__(self, a1):
        self.__root = {}
        self.__bit_length = a1

    def insert(self, a1):
        v1 = self.__root
        for v2 in reversed(range(self.__bit_length)):
            v3 = a1 >> v2 & 1
            if v3 not in v1:
                v1[v3] = {}
            v1 = v1[v3]

    def query(self, a1):
        if not self.__root:
            return -1
        v1, v2 = (self.__root, 0)
        for v3 in reversed(range(self.__bit_length)):
            v4 = a1 >> v3 & 1
            if 1 ^ v4 in v1:
                v1 = v1[1 ^ v4]
                v2 |= 1 << v3
            else:
                v1 = v1[v4]
        return v2

class C2(object):

    def maxXor(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2):
            lookup[a1] = a3[a1] + sum((dfs(v, a1) for v1 in adj[a1] if v1 != a2))
            return lookup[a1]

        def dfs2(a1, a2):
            v1 = max(trie.query(lookup[a1]), 0)
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v1 = max(v1, dfs2(v2, a1))
            trie.insert(lookup[a1])
            return v1
        v1 = [[] for v2 in range(len(a3))]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * len(a3)
        dfs(0, -1)
        v6 = C1(v5[0].bit_length())
        return dfs2(0, -1)
