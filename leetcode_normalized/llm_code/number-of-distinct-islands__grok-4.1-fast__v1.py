class C1:

    def numDistinctIslands(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def traverse(a1, a2, a3, a4):
            if a1 < 0 or a1 >= v1 or a2 < 0 or (a2 >= v2) or (a1[a1][a2] != 1):
                return False
            a1[a1][a2] = 0
            path.append(str(a1 - a3) + str(a2 - a4))
            for v1, v2 in v3:
                traverse(a1 + v1, a2 + v2, a3, a4)
            return True
        v4 = set()
        for v5 in range(v1):
            for v6 in range(v2):
                v7 = []
                if traverse(v5, v6, v5, v6):
                    v4.add(''.join(v7))
        return len(v4)
