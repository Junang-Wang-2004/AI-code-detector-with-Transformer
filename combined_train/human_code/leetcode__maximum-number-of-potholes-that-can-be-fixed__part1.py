class C1(object):

    def maxPotholes(self, a1, a2):
        """
        """

        def inplace_counting_sort(a1, a2=False):
            if not a1:
                return
            v1 = [0] * (max(a1) + 1)
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
        v1 = []
        v2 = 0
        for v3 in range(len(a1)):
            v2 += 1
            if v3 + 1 == len(a1) or a1[v3 + 1] != a1[v3]:
                if a1[v3] == 'x':
                    v1.append(v2)
                v2 = 0
        inplace_counting_sort(v1)
        v4 = 0
        for v2 in reversed(v1):
            v5 = min(v2 + 1, a2)
            if v5 - 1 <= 0:
                break
            v4 += v5 - 1
            a2 -= v5
        return v4
