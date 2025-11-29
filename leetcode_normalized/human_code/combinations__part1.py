class C1(object):

    def combine(self, a1, a2):
        """
        """
        if a2 > a1:
            return []
        v1, v2 = (list(range(1, a1 + 1)), list(range(a2)))
        v3 = [[v1[i] for v4 in v2]]
        while True:
            for v4 in reversed(range(a2)):
                if v2[v4] != v4 + a1 - a2:
                    break
            else:
                break
            v2[v4] += 1
            for v5 in range(v4 + 1, a2):
                v2[v5] = v2[v5 - 1] + 1
            v3.append([v1[v4] for v4 in v2])
        return v3
