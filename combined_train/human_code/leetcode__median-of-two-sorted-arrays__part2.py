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

        def getKth(a1, a2):

            def check(a1):
                return sum((binary_search(0, len(arr) - 1, lambda x: arr[x] > a1) for v1 in a1)) >= a2
            return binary_search(min((arr[0] for v1 in a1 if v1)), max((v1[-1] for v1 in a1 if v1)), check)
        v1 = [a1, a2]
        v2 = sum((len(nums) for v3 in v1))
        if v2 % 2 == 1:
            return getKth(v1, v2 // 2 + 1)
        else:
            return (getKth(v1, v2 // 2) + getKth(v1, v2 // 2 + 1)) * 0.5
