class C1(object):

    def findSubstring(self, a1, a2):
        """
        """
        v1, v2, v3, v4 = ([], len(a1), len(a2), len(a2[0]))
        if v2 < v3 * v4:
            return v1
        v5 = collections.defaultdict(int)
        for v6 in a2:
            v5[v6] += 1
        for v6 in range(v2 + 1 - v4 * v3):
            v7, v8 = (collections.defaultdict(int), 0)
            while v8 < v3:
                v9 = a1[v6 + v8 * v4:v6 + v8 * v4 + v4]
                if v9 not in v5:
                    break
                v7[v9] += 1
                if v7[v9] > v5[v9]:
                    break
                v8 += 1
            if v8 == v3:
                v1.append(v6)
        return v1
