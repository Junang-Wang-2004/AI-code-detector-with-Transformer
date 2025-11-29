class C1(object):

    def minDays(self, a1):
        v1 = 0
        v2, v3 = ([a1], set([a1]))
        while v2:
            v4 = []
            for v5 in v2:
                if not v5:
                    return v1
                if v5 - 1 not in v3:
                    v3.add(v5 - 1)
                    v4.append(v5 - 1)
                if v5 % 2 == 0 and v5 // 2 not in v3:
                    v3.add(v5 // 2)
                    v4.append(v5 // 2)
                if v5 % 3 == 0 and v5 // 3 not in v3:
                    v3.add(v5 // 3)
                    v4.append(v5 // 3)
            v1 += 1
            v2 = v4
        return v1
