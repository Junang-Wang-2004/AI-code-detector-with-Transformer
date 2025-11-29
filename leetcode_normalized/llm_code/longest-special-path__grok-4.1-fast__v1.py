class C1:

    def longestSpecialPath(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = {}
        v8 = [0]
        v9 = [float('inf'), float('inf')]

        def traverse(a1, a2, a3, a4):
            v1 = a2[a1] - 1
            v2 = v7.get(v1, -1)
            v7[v1] = a3
            v3 = max(a4, v2)
            v4 = v8[a3] - v8[v3 + 1]
            v5 = a3 - v3
            v9[:] = min(v9, [-v4, v5])
            for v6, v7 in v2[a1]:
                if v6 == a2:
                    continue
                v8.append(v8[-1] + v7)
                traverse(v6, a1, a3 + 1, v3)
                v8.pop()
            v7[v1] = v2
        traverse(0, -1, 0, -1)
        return [-v9[0], v9[1]]
