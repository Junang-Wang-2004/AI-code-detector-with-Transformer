class C1(object):

    def sequentialDigits(self, a1, a2):
        v1 = []
        for v2 in range(1, 10):
            for v3 in range(1, 11 - v2):
                v4 = 0
                for v5 in range(v2):
                    v4 = v4 * 10 + v3 + v5
                if a1 <= v4 <= a2:
                    v1.append(v4)
        return v1
