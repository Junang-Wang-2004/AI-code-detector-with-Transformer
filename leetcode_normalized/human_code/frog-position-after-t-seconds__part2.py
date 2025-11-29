class C1(object):

    def frogPosition(self, a1, a2, a3, a4):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = [(a3, 1, 0, 1)]
        while v4:
            a3, v6, v7, v8 = v4.pop()
            if not a3 or not len(v1[v6]) - (v7 != 0):
                if v6 == a4:
                    return 1.0 / v8
                continue
            for v9 in v1[v6]:
                if v9 == v7:
                    continue
                v4.append((a3 - 1, v9, v6, v8 * (len(v1[v6]) - (v7 != 0))))
        return 0.0
