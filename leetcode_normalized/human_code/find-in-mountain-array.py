class C1(object):

    def get(self, a1):
        """
       """
        pass

    def length(self):
        """
       """
        pass

class C2(object):

    def findInMountainArray(self, a1, a2):
        """
        """

        def binarySearch(a1, a2, a3, a4):
            while a2 <= a3:
                v1 = a2 + (a3 - a2) // 2
                if a4(v1):
                    a3 = v1 - 1
                else:
                    a2 = v1 + 1
            return a2
        v1 = binarySearch(a2, 0, a2.length() - 1, lambda x: a2.get(x) >= a2.get(x + 1))
        v2 = binarySearch(a2, 0, v1, lambda x: a2.get(x) >= a1)
        if v2 <= v1 and a2.get(v2) == a1:
            return v2
        v3 = binarySearch(a2, v1, a2.length() - 1, lambda x: a2.get(x) <= a1)
        if v3 <= a2.length() - 1 and a2.get(v3) == a1:
            return v3
        return -1
