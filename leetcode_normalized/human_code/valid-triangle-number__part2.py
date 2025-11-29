class C1(object):

    def triangleNumber(self, a1):
        """
        """
        v1 = 0
        a1.sort()
        for v2 in range(len(a1) - 2):
            if a1[v2] == 0:
                continue
            v3 = v2 + 2
            for v4 in range(v2 + 1, len(a1) - 1):
                while v3 < len(a1) and a1[v2] + a1[v4] > a1[v3]:
                    v3 += 1
                v1 += v3 - v4 - 1
        return v1
