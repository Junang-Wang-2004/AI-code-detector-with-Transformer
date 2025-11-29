class C1:

    def deleteTreeNodes(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3 in range(1, a1):
            v1[a2[v3]].append(v3)

        def traverse(a1):
            v1 = a3[a1]
            v2 = 1
            for v3 in v1[a1]:
                v4, v5 = traverse(v3)
                v1 += v4
                if v4 != 0:
                    v2 += v5
            if v1 == 0:
                return (0, 0)
            return (v1, v2)
        v2, v4 = traverse(0)
        return v4
