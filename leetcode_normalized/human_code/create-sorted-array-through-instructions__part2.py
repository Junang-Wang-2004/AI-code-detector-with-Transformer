import itertools

class C1(object):

    def createSortedArray(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

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
                v3.append(a1[v4])
                a4[a1[v4][1]] += v2 - a2
            while v2 <= v1:
                v3.append(a1[v2])
                v2 += 1
            a1[a2:a2 + len(v3)] = v3

        def largerMergeSort(a1, a2, a3, a4):
            if a3 - a2 <= 0:
                return 0
            v1 = a2 + (a3 - a2) // 2
            largerMergeSort(a1, a2, v1, a4)
            largerMergeSort(a1, v1 + 1, a3, a4)
            v2 = a2
            v3 = []
            for v4 in range(v1 + 1, a3 + 1):
                while v2 <= v1 and a1[v2][0] <= a1[v4][0]:
                    v3.append(a1[v2])
                    v2 += 1
                if v2 <= v1:
                    v3.append(a1[v4])
                a4[a1[v4][1]] += v1 - v2 + 1
            while v2 <= v1:
                v3.append(a1[v2])
                v2 += 1
            a1[a2:a2 + len(v3)] = v3
        v2 = []
        v3, v4 = [[0] * len(a1) for v5 in range(2)]
        for v6, v7 in enumerate(a1):
            v2.append((v7, v6))
        smallerMergeSort(v2[:], 0, len(v2) - 1, v3)
        largerMergeSort(v2, 0, len(v2) - 1, v4)
        return sum((min(s, l) for v8, v9 in zip(v3, v4))) % v1
