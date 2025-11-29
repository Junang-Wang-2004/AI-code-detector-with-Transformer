import collections

class C1(object):

    def findSubstring(self, a1, a2):
        """
        """
        if not a2:
            return []
        v1, v2, v3, v4 = ([], len(a1), len(a2), len(a2[0]))
        if v2 < v3 * v4:
            return v1
        v5 = collections.defaultdict(int)
        for v6 in a2:
            v5[v6] += 1
        for v6 in range(v4):
            v7, v8 = (v6, 0)
            v9 = collections.defaultdict(int)
            for v10 in range(v6, v2 - v4 + 1, v4):
                v11 = a1[v10:v10 + v4]
                if v11 in v5:
                    v9[v11] += 1
                    v8 += 1
                    while v9[v11] > v5[v11]:
                        v9[a1[v7:v7 + v4]] -= 1
                        v8 -= 1
                        v7 += v4
                    if v8 == v3:
                        v1.append(v7)
                else:
                    v9 = collections.defaultdict(int)
                    v8 = 0
                    v7 = v10 + v4
        return v1
