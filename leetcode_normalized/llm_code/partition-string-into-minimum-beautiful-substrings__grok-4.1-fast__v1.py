class C1(object):

    def minimumBeautifulSubstrings(self, a1):
        v1 = len(a1)
        v2 = [float('inf')] * (v1 + 1)
        v2[0] = 0
        v3 = set()
        v4 = 1
        while v4.bit_length() <= v1:
            v3.add(v4)
            v4 *= 5
        for v5 in range(v1):
            if a1[v5] == '0':
                continue
            v6 = 0
            for v7 in range(v5, v1):
                v6 = v6 << 1 | int(a1[v7])
                if v6 in v3:
                    v2[v7 + 1] = min(v2[v7 + 1], v2[v5] + 1)
        v8 = v2[v1]
        return v8 if v8 != float('inf') else -1
