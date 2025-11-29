from sortedcontainers import SortedList

class C1(object):

    def minimumCoins(self, a1):
        """
        """
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        v2 = SortedList()
        v3 = 0
        for v4 in range(len(a1)):
            v2.add((v1[v4] + a1[v4], v4))
            while v3 + (v3 + 1) < v4:
                v2.remove((v1[v3] + a1[v3], v3))
                v3 += 1
            v1[v4 + 1] = v2[0][0]
        return v1[-1]
