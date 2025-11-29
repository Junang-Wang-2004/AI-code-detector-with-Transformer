from sortedcontainers import SortedList

class C1(object):

    def closestRoom(self, a1, a2):
        """
        """

        def find_closest(a1, a2):
            v1, v2 = (-1, float('inf'))
            v3 = a1.bisect_right(a2)
            if v3 - 1 >= 0 and abs(a1[v3 - 1] - a2) < v2:
                v2 = abs(a1[v3 - 1] - a2)
                v1 = a1[v3 - 1]
            if v3 < len(a1) and abs(a1[v3] - a2) < v2:
                v2 = abs(a1[v3] - a2)
                v1 = a1[v3]
            return v1
        a1.sort(key=lambda x: x[1])
        for v1, v2 in enumerate(a2):
            v2.append(v1)
        a2.sort(key=lambda x: x[1])
        v3 = SortedList((v1 for v1, v4 in a1))
        v1 = 0
        v5 = [-1] * len(a2)
        for v6, v7, v8 in a2:
            while v1 < len(a1) and a1[v1][1] < v7:
                v3.remove(a1[v1][0])
                v1 += 1
            v5[v8] = find_closest(v3, v6)
        return v5
