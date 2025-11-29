from sortedcontainers import SortedList

class C1(object):

    def medianSlidingWindow(self, a1, a2):
        """
        """
        v1 = SortedList((float(a1[i]) for v2 in range(a2)))
        v3 = [(v1[a2 // 2] + v1[a2 // 2 - (1 - a2 % 2)]) / 2]
        for v2 in range(a2, len(a1)):
            v1.add(float(a1[v2]))
            v1.remove(a1[v2 - a2])
            v3.append((v1[a2 // 2] + v1[a2 // 2 - (1 - a2 % 2)]) / 2)
        return v3
