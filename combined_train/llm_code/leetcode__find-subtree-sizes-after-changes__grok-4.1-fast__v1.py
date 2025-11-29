class C1:

    def findSubtreeSizes(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4 in range(v1):
            v5 = a1[v4]
            if v5 != -1:
                v2[v5].append(v4)
        v6 = [[] for v3 in range(26)]
        v7 = [1] * v1

        def visit(a1):
            v1 = ord(a2[a1]) - ord('a')
            v6[v1].append(a1)
            for v2 in v2[a1]:
                visit(v2)
                v3 = ord(a2[v2]) - ord('a')
                v4 = v6[v3][-1] if v6[v3] else a1
                v7[v4] += v7[v2]
            v6[v1].pop()
        visit(0)
        return v7
