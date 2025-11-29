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
            v4 = 0
            for v5 in reversed(range(v3 + 1)):
                v4 += int(a1[v5]) << v3 - v5
                if a1[v5] == '1' and v1 % v4 == 0:
                    v2[v3 + 1] = min(v2[v3 + 1], v2[v5 - 1 + 1] + 1)
        return v2[-1] if v2[-1] != float('inf') else -1
