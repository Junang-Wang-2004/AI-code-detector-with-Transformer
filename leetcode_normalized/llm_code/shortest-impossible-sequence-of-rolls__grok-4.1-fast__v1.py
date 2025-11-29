class C1(object):

    def shortestSequence(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        v3 = 1
        while v2 < v1:
            v4 = set()
            v5 = 0
            while v2 < v1 and v5 < a2:
                v6 = a1[v2]
                if v6 not in v4:
                    v4.add(v6)
                    v5 += 1
                v2 += 1
            if v5 == a2:
                v3 += 1
        return v3
