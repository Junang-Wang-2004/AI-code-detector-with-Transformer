class C1(object):

    def validSequence(self, a1, a2):
        """
        """
        v1 = len(a2) - 1
        v2 = [-1] * len(a2)
        for v3 in reversed(range(len(a1))):
            if a1[v3] != a2[v1]:
                continue
            v2[v1] = v3
            v1 -= 1
            if v1 == -1:
                break
        v4 = []
        v5 = 0
        for v3 in range(len(a1)):
            if not (a1[v3] == a2[len(v4)] or (v5 == 0 and (len(v4) + 1 == len(a2) or v3 < v2[len(v4) + 1]))):
                continue
            if a1[v3] != a2[len(v4)]:
                v5 += 1
            v4.append(v3)
            if len(v4) == len(a2):
                return v4
        return []
