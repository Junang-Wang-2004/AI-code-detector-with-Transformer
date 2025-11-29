class C1:

    def removeStones(self, a1):
        v1 = {}
        v2 = {}

        def locate(a1):
            if a1 not in v1:
                v1[a1] = a1
                v2[a1] = 0
            if v1[a1] != a1:
                v1[a1] = locate(v1[a1])
            return v1[a1]

        def link(a1, a2):
            v1, v2 = (locate(a1), locate(a2))
            if v1 == v2:
                return
            if v2[v1] < v2[v2]:
                v1[v1] = v2
            elif v2[v1] > v2[v2]:
                v1[v2] = v1
            else:
                v1[v2] = v1
                v2[v1] += 1
        for v3, v4 in a1:
            link('row' + str(v3), 'col' + str(v4))
        v5 = {locate('row' + str(v3)) for v3, v4 in a1}
        return len(a1) - len(v5)
