from sortedcontainers import SortedList

class C1(object):

    def getSubarrayBeauty(self, a1, a2, a3):
        """
        """
        v1 = []
        v2 = SortedList()
        for v3, v4 in enumerate(a1):
            if v3 - a2 >= 0:
                v2.remove(a1[v3 - a2])
            v2.add(v4)
            if v3 - a2 + 1 >= 0:
                v1.append(min(v2[a3 - 1], 0))
        return v1
