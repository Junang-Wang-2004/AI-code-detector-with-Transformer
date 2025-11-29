class C1:

    def countComponents(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * a1

        def explore(a1):
            v1 = [a1]
            v5[a1] = True
            while v1:
                v2 = v1.pop()
                for v3 in v1[v2]:
                    if not v5[v3]:
                        v5[v3] = True
                        v1.append(v3)
        v6 = 0
        for v7 in range(a1):
            if not v5[v7]:
                explore(v7)
                v6 += 1
        return v6
