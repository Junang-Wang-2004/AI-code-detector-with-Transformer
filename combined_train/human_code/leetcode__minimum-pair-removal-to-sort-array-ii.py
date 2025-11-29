from sortedcontainers import SortedList

class C1(object):

    def minimumPairRemoval(self, a1):
        """
        """

        def add(a1):
            if 0 <= a1 < right[a1] < len(a1):
                sl.add([a1[a1] + a1[right[a1]], a1])
                if a1[a1] > a1[right[a1]]:
                    cnt[0] += 1

        def remove(a1):
            if 0 <= a1 < right[a1] < len(a1):
                sl.remove([a1[a1] + a1[right[a1]], a1])
                if a1[a1] > a1[right[a1]]:
                    cnt[0] -= 1
        v1 = list(range(-1, len(a1) + 1 - 1))
        v2 = list(range(1, len(a1) + 1))
        v3 = [sum((a1[i] > a1[i + 1] for v4 in range(len(a1) - 1)))]
        v5 = SortedList(([a1[v4] + a1[v4 + 1], v4] for v4 in range(len(a1) - 1)))
        v6 = 0
        while v3[0]:
            v7, v4 = v5[0]
            remove(v1[v4])
            remove(v4)
            remove(v2[v4])
            a1[v4] += a1[v2[v4]]
            v1[v2[v2[v4]]] = v4
            v2[v4] = v2[v2[v4]]
            add(v1[v4])
            add(v4)
            v6 += 1
        return v6
