class C1(object):

    def minTime(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = [0]
        v5 = [(1, (-1, 0, v4))]
        while v5:
            v6, v7 = v5.pop()
            if v6 == 1:
                v8, v9, v10 = v7
                v11 = [int(a3[v9])]
                v5.append((3, (v11, v10)))
                for v12 in reversed(v1[v9]):
                    if v12 == v8:
                        continue
                    v13 = [0]
                    v5.append((2, (v13, v11, v10)))
                    v5.append((1, (v9, v12, v13)))
            elif v6 == 2:
                v13, v11, v10 = v7
                v10[0] += v13[0]
                v11[0] |= bool(v13[0])
            else:
                v11, v10 = v7
                v10[0] += v11[0]
        return 2 * max(v4[0] - 1, 0)
