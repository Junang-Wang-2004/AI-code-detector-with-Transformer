class C1(object):

    def minimumCost(self, a1, a2):
        """
        """

        def lens(a1):
            v1 = len(a1) - 1
            for v2 in reversed(range(-1, len(a1))):
                if v2 == -1 or a1[v2] == ' ':
                    yield (v1 - v2)
                    v1 = v2 - 1
        v1, v2 = ([], [])
        v3 = -1
        for v4 in lens(a1):
            v1.append(v4)
            v2.append(float('inf'))
            v3 += v4 + 1
            if v3 <= a2:
                v2[-1] = 0
                continue
            v5 = v4
            for v6 in reversed(range(len(v2) - 1)):
                v2[-1] = min(v2[-1], v2[v6] + (a2 - v5) ** 2)
                v5 += v1[v6] + 1
                if v5 > a2:
                    v1 = v1[v6:]
                    v2 = v2[v6:]
                    break
        return v2[-1] if v2 else 0
