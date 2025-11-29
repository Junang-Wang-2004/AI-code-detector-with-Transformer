class C1(object):

    def findMedianSortedArrays(self, a1, a2):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def getKth(a1, a2, a3):
            v1, v2 = (len(a1), len(a2))
            if v1 > v2:
                v1, v2 = (v2, v1)
                a1, a2 = (a2, a1)
            v5 = binary_search(max(a3 - v2, 0), min(v1, a3) - 1, lambda i: a1[v5] >= a2[a3 - 1 - v5])
            return max(a1[v5 - 1] if v5 - 1 >= 0 else float('-inf'), a2[a3 - 1 - v5] if a3 - 1 - v5 >= 0 else float('-inf'))
        v1, v2 = (len(a1), len(a2))
        if (v1 + v2) % 2 == 1:
            return getKth(a1, a2, (v1 + v2) // 2 + 1)
        else:
            return (getKth(a1, a2, (v1 + v2) // 2) + getKth(a1, a2, (v1 + v2) // 2 + 1)) * 0.5
