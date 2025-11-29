from sortedcontainers import SortedList

class C1(object):

    def minThreshold(self, a1, a2):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):
            v1 = SortedList()
            v2 = 0
            for v3 in reversed(a1):
                v2 += v1.bisect_left(v3) - v1.bisect_left(v3 - a1)
                v1.add(v3)
            return v2 >= a2
        v1, v2 = (a1[0], 0)
        for v3 in range(1, len(a1)):
            v2 = max(v2, v1 - a1[v3])
            v1 = max(v1, a1[v3])
        v4 = binary_search(0, v2, check)
        return v4 if v4 <= v2 else -1
