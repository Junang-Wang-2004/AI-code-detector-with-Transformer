class C1(object):

    def searchRange(self, a1, a2):
        """
        """

        def binarySearch(a1, a2):
            v1, v2 = (0, a1 - 1)
            while v1 <= v2:
                v3 = v1 + (v2 - v1) // 2
                if a2(v3):
                    v2 = v3 - 1
                else:
                    v1 = v3 + 1
            return v1

        def binarySearch2(a1, a2):
            v1, v2 = (0, a1)
            while v1 < v2:
                v3 = v1 + (v2 - v1) // 2
                if a2(v3):
                    v2 = v3
                else:
                    v1 = v3 + 1
            return v1

        def binarySearch3(a1, a2):
            v1, v2 = (-1, a1 - 1)
            while v1 < v2:
                v3 = v2 - (v2 - v1) // 2
                if a2(v3):
                    v2 = v3 - 1
                else:
                    v1 = v3
            return v1 + 1

        def binarySearch4(a1, a2):
            v1, v2 = (-1, a1)
            while v2 - v1 >= 2:
                v3 = v1 + (v2 - v1) // 2
                if a2(v3):
                    v2 = v3
                else:
                    v1 = v3
            return v1 + 1
        v1 = binarySearch(len(a1), lambda i: a1[i] >= a2)
        if v1 == len(a1) or a1[v1] != a2:
            return [-1, -1]
        v2 = binarySearch(len(a1), lambda i: a1[i] > a2)
        return [v1, v2 - 1]
