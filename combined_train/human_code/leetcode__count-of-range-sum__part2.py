class C1(object):

    def countRangeSum(self, a1, a2, a3):
        """
        """

        def countAndMergeSort(a1, a2, a3, a4, a5):
            if a3 - a2 <= 0:
                return 0
            v1 = a2 + (a3 - a2) / 2
            v2 = countAndMergeSort(a1, a2, v1, a4, a5) + countAndMergeSort(a1, v1 + 1, a3, a4, a5)
            v3, v4, v5 = (v1 + 1, v1 + 1, v1 + 1)
            v6 = []
            for v7 in range(a2, v1 + 1):
                while v4 <= a3 and a1[v4] - a1[v7] < a4:
                    v4 += 1
                while v3 <= a3 and a1[v3] - a1[v7] <= a5:
                    v3 += 1
                v2 += v3 - v4
                while v5 <= a3 and a1[v5] < a1[v7]:
                    v6.append(a1[v5])
                    v5 += 1
                v6.append(a1[v7])
            a1[a2:a2 + len(v6)] = v6
            return v2
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        return countAndMergeSort(v1, 0, len(v1) - 1, a2, a3)
