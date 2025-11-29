class C1(object):

    def sortArray(self, a1):
        """
        """

        def mergeSort(a1, a2, a3):
            if a1 == a2:
                return
            v1 = a1 + (a2 - a1) // 2
            mergeSort(a1, v1, a3)
            mergeSort(v1 + 1, a2, a3)
            v2 = v1 + 1
            v3 = []
            for v4 in range(a1, v1 + 1):
                while v2 <= a2 and a3[v2] < a3[v4]:
                    v3.append(a3[v2])
                    v2 += 1
                v3.append(a3[v4])
            a3[a1:a1 + len(v3)] = v3
        mergeSort(0, len(a1) - 1, a1)
        return a1
