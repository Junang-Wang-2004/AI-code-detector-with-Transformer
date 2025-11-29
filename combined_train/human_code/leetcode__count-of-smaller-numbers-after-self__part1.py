class C1(object):

    def countSmaller(self, a1):
        """
        """

        def countAndMergeSort(a1, a2, a3, a4):
            if a3 - a2 <= 0:
                return
            v1 = a2 + (a3 - a2) // 2
            countAndMergeSort(a1, a2, v1, a4)
            countAndMergeSort(a1, v1 + 1, a3, a4)
            v2 = v1 + 1
            v3 = []
            for v4 in range(a2, v1 + 1):
                while v2 <= a3 and a1[v2][0] < a1[v4][0]:
                    v3.append(a1[v2])
                    v2 += 1
                v3.append(a1[v4])
                a4[a1[v4][1]] += v2 - (v1 + 1)
            a1[a2:a2 + len(v3)] = v3
        v1 = []
        v2 = [0] * len(a1)
        for v3, v4 in enumerate(a1):
            v1.append((v4, v3))
        countAndMergeSort(v1, 0, len(v1) - 1, v2)
        return v2
