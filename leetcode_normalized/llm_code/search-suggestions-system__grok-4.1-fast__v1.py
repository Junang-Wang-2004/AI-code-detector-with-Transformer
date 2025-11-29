import bisect

class C1:

    def suggestedProducts(self, a1, a2):
        a1.sort()
        v1 = []
        v2 = ''
        for v3 in a2:
            v2 += v3
            v4 = bisect.bisect_left(a1, v2)
            v5 = v2[:-1] + chr(ord(v3) + 1)
            v6 = bisect.bisect_left(a1, v5)
            v1.append(a1[v4:min(v4 + 3, v6)])
        return v1
