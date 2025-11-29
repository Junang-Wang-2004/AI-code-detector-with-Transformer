class C1:

    def countGoodNodes(self, a1):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1 + 1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        self.count = 0

        def traverse(a1, a2):
            v1 = []
            for v2 in v2[a1]:
                if v2 != a2:
                    v1.append(traverse(v2, a1))
            if len(v1) == 0 or len(v1) == 1 or all((sz == v1[0] for v3 in v1)):
                self.count += 1
            return 1 + sum(v1)
        traverse(0, -1)
        return self.count
