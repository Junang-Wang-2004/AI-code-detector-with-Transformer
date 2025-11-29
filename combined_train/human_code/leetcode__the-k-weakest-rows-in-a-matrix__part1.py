class C1(object):

    def kWeakestRows(self, a1, a2):
        """
        """
        v1, v2 = ([], set())
        for v3 in range(len(a1[0])):
            for v4 in range(len(a1)):
                if a1[v4][v3] or v4 in v2:
                    continue
                v2.add(v4)
                v1.append(v4)
                if len(v1) == a2:
                    return v1
        for v4 in range(len(a1)):
            if v4 in v2:
                continue
            v2.add(v4)
            v1.append(v4)
            if len(v1) == a2:
                break
        return v1
