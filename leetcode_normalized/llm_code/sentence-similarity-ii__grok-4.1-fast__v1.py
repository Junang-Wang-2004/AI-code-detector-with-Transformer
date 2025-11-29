class C1:

    def areSentencesSimilarTwo(self, a1, a2, a3):
        if len(a1) != len(a2):
            return False
        v1 = {}
        v2 = {}

        def get_root(a1, a2):
            if a1[a2] != a2:
                a1[a2] = get_root(a1, a1[a2])
            return a1[a2]

        def connect(a1, a2, a3, a4):
            v1 = get_root(a1, a3)
            v2 = get_root(a1, a4)
            if v1 == v2:
                return
            if a2[v1] > a2[v2]:
                a1[v2] = v1
            elif a2[v1] < a2[v2]:
                a1[v1] = v2
            else:
                a1[v2] = v1
                a2[v1] += 1
        for v3, v4 in a3:
            if v3 not in v1:
                v1[v3] = v3
                v2[v3] = 0
            if v4 not in v1:
                v1[v4] = v4
                v2[v4] = 0
            connect(v1, v2, v3, v4)
        for v5, v6 in zip(a1, a2):
            if v5 == v6:
                continue
            if v5 not in v1 or v6 not in v1:
                return False
            if get_root(v1, v5) != get_root(v1, v6):
                return False
        return True
