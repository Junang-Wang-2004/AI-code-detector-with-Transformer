class C1(object):

    def specialArray(self, a1):
        """
        """
        v1 = 1000

        def inplace_counting_sort(a1, a2=False):
            v1 = [0] * (v1 + 1)
            for v2 in a1:
                v1[v2] += 1
            for v3 in range(1, len(v1)):
                v1[v3] += v1[v3 - 1]
            for v3 in reversed(range(len(a1))):
                while a1[v3] >= 0:
                    v1[a1[v3]] -= 1
                    v4 = v1[a1[v3]]
                    a1[v3], a1[v4] = (a1[v4], ~a1[v3])
            for v3 in range(len(a1)):
                a1[v3] = ~a1[v3]
            if a2:
                a1.reverse()
        inplace_counting_sort(a1, reverse=True)
        v2, v3 = (0, len(a1) - 1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if a1[v4] <= v4:
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return -1 if v2 < len(a1) and a1[v2] == v2 else v2
