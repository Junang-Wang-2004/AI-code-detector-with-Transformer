import bisect

class C1(object):

    def matrixMedian(self, a1):
        """
        """

        def check(a1):
            return sum((bisect_right(row, a1) for v1 in a1)) > len(a1) * len(a1[0]) // 2
        v1, v2 = (min((row[0] for v3 in a1)), max((v3[-1] for v3 in a1)))
        while v1 <= v2:
            v4 = v1 + (v2 - v1) // 2
            if check(v4):
                v2 = v4 - 1
            else:
                v1 = v4 + 1
        return v1
