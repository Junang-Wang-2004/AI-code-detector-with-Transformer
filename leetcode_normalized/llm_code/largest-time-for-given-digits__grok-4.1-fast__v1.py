class C1(object):

    def largestTimeFromDigits(self, a1):
        v1 = ''
        for v2 in range(4):
            for v3 in range(4):
                if v3 == v2:
                    continue
                for v4 in range(4):
                    if v4 == v2 or v4 == v3:
                        continue
                    v5 = 6 - (v2 + v3 + v4)
                    v6 = 10 * a1[v2] + a1[v3]
                    v7 = 10 * a1[v4] + a1[v5]
                    if v6 <= 23 and v7 <= 59:
                        v8 = f'{v6:02d}:{v7:02d}'
                        if v8 > v1:
                            v1 = v8
        return v1
