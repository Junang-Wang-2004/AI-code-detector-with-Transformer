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

        def check(a1):
            for v1 in range(len(a2)):
                v2 = v1
                for v3 in range(a3 - 1):
                    v2 = bisect.bisect_left(p, p[v2] + a1, lo=v2 + 1, hi=v1 + len(a2))
                    if v2 == v1 + len(a2):
                        break
                else:
                    if p[v1 + len(a2)] - p[v2] >= a1:
                        return True
            return False
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
        v1 += [v2 + 4 * a1 for v2 in v1]
        return binary_search_right(1, 4 * a1 // a3, check)
