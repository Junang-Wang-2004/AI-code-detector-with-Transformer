class C1(object):

    def minimumBeautifulSubstrings(self, a1):
        """
        """
        v1 = 1
        while v1 * 5 <= (1 << len(a1)) - 1:
            v1 *= 5
        v2 = [float('inf')] * (len(a1) + 1)
        v2[0] = 0
        for v3 in range(len(a1)):
            if a1[v3] == '0':
                continue
            v4 = 0
            for v5 in range(v3, len(a1)):
                v4 = v4 * 2 + int(a1[v5])
                if v1 % v4 == 0:
                    v2[v5 + 1] = min(v2[v5 + 1], v2[v3 - 1 + 1] + 1)
        return v2[-1] if v2[-1] != float('inf') else -1
