class C1(object):

    def minimumDistance(self, a1):
        """
        """

        def distance(a1, a2):
            return abs(a1 // 6 - a2 // 6) + abs(a1 % 6 - a2 % 6)
        v1 = [0] * 26
        for v2 in range(len(a1) - 1):
            v3, v4 = (ord(a1[v2]) - ord('A'), ord(a1[v2 + 1]) - ord('A'))
            v1[v3] = max((v1[a] - distance(a, v4) + distance(v3, v4) for v5 in range(26)))
        return sum((distance(ord(a1[v2]) - ord('A'), ord(a1[v2 + 1]) - ord('A')) for v2 in range(len(a1) - 1))) - max(v1)
