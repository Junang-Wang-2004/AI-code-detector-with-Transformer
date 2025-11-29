import bisect

class C1(object):

    def maxTaskAssign(self, a1, a2, a3, a4):
        """
        """

        def check(a1, a2, a3, a4, a5):
            v1 = a2[-a5:]
            for v2 in a1[-a5:]:
                v3 = bisect.bisect_left(v1, v2)
                if v3 != len(v1):
                    v1.pop(v3)
                    continue
                if a3:
                    v3 = bisect.bisect_left(v1, v2 - a4)
                    if v3 != len(v1):
                        v1.pop(v3)
                        a3 -= 1
                        continue
                return False
            return True
        a1.sort(reverse=True)
        a2.sort()
        v1, v2 = (1, min(len(a2), len(a1)))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, a3, a4, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
