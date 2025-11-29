import bisect

class C1(object):

    def maxDistance(self, a1, a2, a3):
        """
        """

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def check(a1, a2):
            v1 = a1
            for v2 in range(a3 - 1):
                v1 = bisect.bisect_left(p, p[v1] + a2, lo=v1 + 1)
                if v1 == len(p):
                    return False
            return p[a1] + 4 * a1 - p[v1] >= a2
        v1 = []
        for v2, v3 in a2:
            if v2 == 0:
                v1.append(0 * a1 + v3)
            elif v3 == a1:
                v1.append(1 * a1 + v2)
            elif v2 == a1:
                v1.append(2 * a1 + (a1 - v3))
            else:
                v1.append(3 * a1 + (a1 - v2))
        v1.sort()
        v4 = 1
        for v5 in range(len(v1) - a3 + 1):
            if v1[-1] - v1[v5] <= v4 * (a3 - 1):
                break
            v4 = binary_search_right(v4 + 1, 4 * a1 // a3, lambda x: check(v5, v2))
        return v4
