class C1(object):

    def maxEnvelopes(self, a1):
        if not a1:
            return 0
        v1 = sorted(a1, key=lambda p: (p[0], -p[1]))
        v2 = []

        def search(a1):
            v1, v2 = (0, len(v2))
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if v2[v3] < a1:
                    v1 = v3 + 1
                else:
                    v2 = v3
            return v1
        for v3, v4 in v1:
            v5 = search(v4)
            if v5 == len(v2):
                v2.append(v4)
            else:
                v2[v5] = v4
        return len(v2)
