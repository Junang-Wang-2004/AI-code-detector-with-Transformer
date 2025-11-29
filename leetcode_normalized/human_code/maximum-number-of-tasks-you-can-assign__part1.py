from sortedcontainers import SortedList

class C1(object):

    def maxTaskAssign(self, a1, a2, a3, a4):
        """
        """

        def check(a1, a2, a3, a4, a5):
            v1 = SortedList(a1[:a5])
            for v2 in a2[-a5:]:
                v3 = v1.bisect_right(v2) - 1
                if v3 != -1:
                    v1.pop(v3)
                    continue
                if a3:
                    v3 = v1.bisect_right(v2 + a4) - 1
                    if v3 != -1:
                        v1.pop(v3)
                        a3 -= 1
                        continue
                return False
            return True
        a1.sort()
        a2.sort()
        v1, v2 = (1, min(len(a2), len(a1)))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, a3, a4, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
