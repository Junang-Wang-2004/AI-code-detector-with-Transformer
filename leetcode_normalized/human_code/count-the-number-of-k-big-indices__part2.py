from sortedcontainers import SortedList

class C1(object):

    def kBigIndices(self, a1, a2):
        """
        """
        v1, v2 = (SortedList(), SortedList(a1))
        v3 = 0
        for v4 in a1:
            v2.remove(v4)
            if v1.bisect_left(v4) >= a2 and v2.bisect_left(v4) >= a2:
                v3 += 1
            v1.add(v4)
        return v3
