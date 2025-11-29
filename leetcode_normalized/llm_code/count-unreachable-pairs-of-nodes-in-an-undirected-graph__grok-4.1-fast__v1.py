class C1:

    def countPairs(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * a1
        v6 = []

        def component_size(a1):
            v1 = [a1]
            v5[a1] = True
            v2 = 1
            while v1:
                v3 = v1.pop()
                for v4 in v1[v3]:
                    if not v5[v4]:
                        v5[v4] = True
                        v2 += 1
                        v1.append(v4)
            return v2
        for v7 in range(a1):
            if not v5[v7]:
                v6.append(component_size(v7))
        v8 = 0
        for v9 in v6:
            v8 += v9 * (a1 - v9)
        return v8 // 2
