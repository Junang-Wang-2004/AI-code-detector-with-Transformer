import bisect
import itertools

class C1(object):

    def minArea(self, a1, a2, a3):
        """
        """

        def binarySearch(a1, a2, a3, a4, a5):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) / 2
                if a3(a4, a5, v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1
        v1 = lambda image, has_one, mid: any([int(row[mid]) for v2 in a1]) == has_one
        v3 = binarySearch(0, a3 - 1, v1, a1, True)
        v4 = binarySearch(a3 + 1, len(a1[0]) - 1, v1, a1, False)
        v5 = lambda image, has_one, mid: any(map(int, a1[mid])) == has_one
        v6 = binarySearch(0, a2 - 1, v5, a1, True)
        v7 = binarySearch(a2 + 1, len(a1) - 1, v5, a1, False)
        return (v4 - v3) * (v7 - v6)
