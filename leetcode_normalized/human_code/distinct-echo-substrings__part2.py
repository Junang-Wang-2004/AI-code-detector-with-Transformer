class C1(object):

    def distinctEchoSubstrings(self, a1):
        """
        """
        v1 = set()
        for v2 in range(1, len(a1) // 2 + 1):
            v3 = sum((a1[i] == a1[i + v2] for v4 in range(v2)))
            for v4 in range(len(a1) - 2 * v2):
                if v3 == v2:
                    v1.add(a1[v4:v4 + v2])
                v3 += (a1[v4 + v2] == a1[v4 + v2 + v2]) - (a1[v4] == a1[v4 + v2])
            if v3 == v2:
                v1.add(a1[len(a1) - 2 * v2:len(a1) - 2 * v2 + v2])
        return len(v1)
