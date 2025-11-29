from sortedcontainers import SortedList

class C1(object):

    def getSubarrayBeauty(self, a1, a2, a3):
        v1 = []
        v2 = SortedList()
        v3 = len(a1)
        for v4 in range(v3):
            if v4 >= a2:
                v5 = a1[v4 - a2]
                if v5 <= 0:
                    v2.remove(v5)
            v6 = a1[v4]
            if v6 <= 0:
                v2.add(v6)
            if v4 >= a2 - 1:
                if len(v2) >= a3:
                    v1.append(v2[a3 - 1])
                else:
                    v1.append(0)
        return v1
