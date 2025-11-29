class C1(object):

    def reversePairs(self, a1):
        """
        """

        def merge(a1, a2, a3, a4):
            v1 = a3 + 1
            v2 = []
            for v3 in range(a2, a3 + 1):
                while v1 <= a4 and a1[v3] > a1[v1]:
                    v2.append(a1[v1])
                    v1 += 1
                v2.append(a1[v3])
            a1[a2:a2 + len(v2)] = v2

        def countAndMergeSort(a1, a2, a3):
            if a3 - a2 <= 0:
                return 0
            v1 = a2 + (a3 - a2) / 2
            v2 = countAndMergeSort(a1, a2, v1) + countAndMergeSort(a1, v1 + 1, a3)
            v3 = v1 + 1
            for v4 in range(a2, v1 + 1):
                while v3 <= a3 and a1[v4] > a1[v3] * 2:
                    v3 += 1
                v2 += v3 - (v1 + 1)
            merge(a1, a2, v1, a3)
            return v2
        return countAndMergeSort(a1, 0, len(a1) - 1)
