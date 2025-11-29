class C1(object):

    def advantageCount(self, a1, a2):
        """
        """
        v1 = sorted(a1)
        v2 = sorted(a2)
        v3 = {b: [] for v4 in a2}
        v5 = []
        v6 = 0
        for v7 in v1:
            if v7 > v2[v6]:
                v3[v2[v6]].append(v7)
                v6 += 1
            else:
                v5.append(v7)
        return [v3[v4].pop() if v3[v4] else v5.pop() for v4 in a2]
