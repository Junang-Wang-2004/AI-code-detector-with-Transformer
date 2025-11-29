class C1(object):

    def threeSumSmaller(self, a1, a2):
        a1.sort()
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1 - 2):
            v4 = v3 + 1
            v5 = v1 - 1
            while v4 < v5:
                v6 = a1[v3] + a1[v4] + a1[v5]
                if v6 < a2:
                    v2 += v5 - v4
                    v4 += 1
                else:
                    v5 -= 1
        return v2
