class C1(object):

    def maximizeSquareArea(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7

        def diff(a1, a2):
            a1.append(1)
            a1.append(a2)
            return {abs(a1[i] - a1[j]) for v1 in range(len(a1)) for v2 in range(v1 + 1, len(a1))}
        v2 = diff(a3, a1)
        v3 = -1
        for v4 in diff(a4, a2):
            if v4 in v2:
                v3 = max(v3, v4 ** 2)
        return v3 % v1 if v3 != -1 else -1
