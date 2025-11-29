class C1(object):

    def canPartitionGrid(self, a1):

        def possible(a1, a2):
            v1 = set()
            v2 = 0
            v3 = -1
            v4 = len(a2[0])
            for v5 in a1:
                if v3 == -1:
                    v3 = v5
                for v6 in range(v4):
                    v7 = a2[v5][v6]
                    v2 += v7
                    v1.add(v7)
                    v8 = 2 * v2 - overall_sum
                    if v8 == 0:
                        return True
                    if v5 != v3 and v6 != 0:
                        if v8 in v1:
                            return True
                    elif v5 == v3:
                        if v8 == a2[v3][0] or v8 == a2[v5][v6]:
                            return True
                    elif v8 == a2[v3][0] or v8 == a2[v5][0]:
                        return True
            return False
        v1 = sum((sum(r) for v2 in a1))
        v3 = len(a1)
        v4 = len(a1[0])
        v5 = list(range(v3))
        if possible(v5, a1):
            return True
        v6 = list(range(v3 - 1, -1, -1))
        if possible(v6, a1):
            return True
        v7 = [[a1[i][j] for v8 in range(v3)] for v9 in range(v4)]
        v10 = list(range(v4))
        if possible(v10, v7):
            return True
        v11 = list(range(v4 - 1, -1, -1))
        if possible(v11, v7):
            return True
        return False
