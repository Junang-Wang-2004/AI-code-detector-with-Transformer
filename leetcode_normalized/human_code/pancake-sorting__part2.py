class C1(object):

    def pancakeSort(self, a1):
        """
        """

        def smallerMergeSort(a1, a2, a3, a4):
            if a3 - a2 <= 0:
                return 0
            v1 = a2 + (a3 - a2) // 2
            smallerMergeSort(a1, a2, v1, a4)
            smallerMergeSort(a1, v1 + 1, a3, a4)
            v2 = a2
            v3 = []
            for v4 in range(v1 + 1, a3 + 1):
                while v2 <= v1 and a1[v2][0] < a1[v4][0]:
                    v3.append(a1[v2])
                    v2 += 1
                if v2 <= v1:
                    v3.append(a1[v4])
                a4[a1[v4][1]] += v2 - a2
            while v2 <= v1:
                v3.append(a1[v2])
                v2 += 1
            a1[a2:a2 + len(v3)] = v3
        v1 = []
        v2 = [0] * len(a1)
        for v3, v4 in enumerate(a1):
            v1.append((v4, v3))
        smallerMergeSort(v1, 0, len(v1) - 1, v2)
        v5 = []
        for v3, v6 in enumerate(v2):
            if v6 == v3:
                continue
            if v6 == 0:
                if v3 > 1:
                    v5.append(v3)
                v5.append(v3 + 1)
            else:
                if v6 > 1:
                    v5.append(v6)
                v5.append(v3)
                v5.append(v3 + 1)
                v5.append(v6 + 1)
        return v5
