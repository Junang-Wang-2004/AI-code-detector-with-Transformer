class C1(object):

    def containsCycle(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if not a1[v2][v3]:
                    continue
                v4 = a1[v2][v3]
                v5 = [(v2, v3)]
                while v5:
                    v6 = []
                    for v7, v8 in v5:
                        if not a1[v7][v8]:
                            return True
                        a1[v7][v8] = 0
                        for v9, v10 in v1:
                            v11, v12 = (v7 + v9, v8 + v10)
                            if not (0 <= v11 < len(a1) and 0 <= v12 < len(a1[0]) and (a1[v11][v12] == v4)):
                                continue
                            v6.append((v11, v12))
                    v5 = v6
        return False
