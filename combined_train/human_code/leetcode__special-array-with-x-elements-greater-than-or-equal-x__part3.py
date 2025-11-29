class C1(object):

    def specialArray(self, a1):
        """
        """
        v1 = 1000

        def counting_sort(a1, a2=False):
            v1 = [0] * (v1 + 1)
            for v2 in a1:
                v1[v2] += 1
            for v3 in range(1, len(v1)):
                v1[v3] += v1[v3 - 1]
            v4 = [0] * len(a1)
            if not a2:
                for v2 in reversed(a1):
                    v1[v2] -= 1
                    v4[v1[v2]] = v2
            else:
                for v2 in a1:
                    v1[v2] -= 1
                    v4[v1[v2]] = v2
                v4.reverse()
            return v4
        a1 = counting_sort(a1, reverse=True)
        v3, v4 = (0, len(a1) - 1)
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if a1[v5] <= v5:
                v4 = v5 - 1
            else:
                v3 = v5 + 1
        return -1 if v3 < len(a1) and a1[v3] == v3 else v3
