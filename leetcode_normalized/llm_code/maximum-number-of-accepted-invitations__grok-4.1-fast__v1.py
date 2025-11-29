class C1:

    def maximumInvitations(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])

        def build_graph(a1, a2, a3):
            v1 = {}
            for v2 in range(a1):
                v3 = []
                for v4 in range(a2):
                    if a1[v2][v4] if a3 else a1[v4][v2]:
                        v3.append(v4)
                v1[v2] = v3
            return v1
        if v1 <= v2:
            v3 = build_graph(v1, v2, True)
            v4 = v1
            v5 = v2
        else:
            v3 = build_graph(v2, v1, False)
            v4 = v2
            v5 = v1
        v6 = [-1] * v4
        v7 = [-1] * v5

        def find_path(a1, a2):
            for v1 in v3[a1]:
                if a2[v1]:
                    continue
                a2[v1] = True
                if v7[v1] == -1 or find_path(v7[v1], a2):
                    v6[a1] = v1
                    v7[v1] = a1
                    return True
            return False
        v8 = 0
        for v9 in range(v4):
            if v6[v9] == -1:
                v10 = [False] * v5
                if find_path(v9, v10):
                    v8 += 1
        return v8
