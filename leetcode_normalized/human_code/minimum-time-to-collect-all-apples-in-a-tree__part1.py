import collections

class C1(object):

    def minTime(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = [0, 0]
        v5 = [(1, (-1, 0, v4))]
        while v5:
            v6, v7 = v5.pop()
            if v6 == 1:
                v8, v9, v10 = v7
                v10[:] = [0, int(a3[v9])]
                for v11 in reversed(v1[v9]):
                    if v11 == v8:
                        continue
                    v12 = [0, 0]
                    v5.append((2, (v12, v10)))
                    v5.append((1, (v9, v11, v12)))
            else:
                v12, v10 = v7
                v10[0] += v12[0] + v12[1]
                v10[1] |= bool(v12[0] + v12[1])
        return 2 * v4[0]
