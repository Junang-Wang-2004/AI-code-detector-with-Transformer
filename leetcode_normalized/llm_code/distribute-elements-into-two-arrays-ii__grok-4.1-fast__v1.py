from sortedcontainers import SortedList

class C1:

    def resultArray(self, a1):
        v1 = [a1[0]]
        v2 = [a1[1]]
        v3 = SortedList()
        v3.add(a1[0])
        v4 = SortedList()
        v4.add(a1[1])
        for v5 in a1[2:]:
            v6 = len(v3) - v3.bisect_right(v5)
            v7 = len(v4) - v4.bisect_right(v5)
            if v6 > v7 or (v6 == v7 and len(v1) <= len(v2)):
                v3.add(v5)
                v1.append(v5)
            else:
                v4.add(v5)
                v2.append(v5)
        return v1 + v2
