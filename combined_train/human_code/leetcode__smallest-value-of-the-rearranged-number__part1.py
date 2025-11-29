class C1(object):

    def smallestNumber(self, a1):
        """
        """

        def inplace_counting_sort(a1, a2=False):
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
        v1 = 1 if a1 >= 0 else -1
        v2 = list(map(int, list(str(abs(a1)))))
        inplace_counting_sort(v2, reverse=v1 == -1)
        v3 = next((v3 for v3 in range(len(v2)) if v2[v3] != 0), 0)
        v2[0], v2[v3] = (v2[v3], v2[0])
        return v1 * int(''.join(map(str, v2)))
