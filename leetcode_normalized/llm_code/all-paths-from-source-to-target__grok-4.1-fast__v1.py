class C1:

    def allPathsSourceTarget(self, a1):
        v1 = len(a1)
        v2 = []
        v3 = [(0, [0])]
        while v3:
            v4, v5 = v3.pop()
            if v4 == v1 - 1:
                v2.append(v5)
                continue
            for v6 in a1[v4]:
                v3.append((v6, v5 + [v6]))
        return v2
