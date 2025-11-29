from sortedcontainers import SortedList

class C1(object):

    def resultArray(self, a1):
        """
        """
        v1, v2 = (SortedList([a1[0]]), SortedList([a1[1]]))
        v3, v4 = ([a1[0]], [a1[1]])
        for v5 in range(2, len(a1)):
            v6 = len(v1) - v1.bisect_right(a1[v5])
            v7 = len(v2) - v2.bisect_right(a1[v5])
            if v6 > v7 or (v6 == v7 and len(v3) <= len(v4)):
                v1.add(a1[v5])
                v3.append(a1[v5])
            else:
                v2.add(a1[v5])
                v4.append(a1[v5])
        return v3 + v4
