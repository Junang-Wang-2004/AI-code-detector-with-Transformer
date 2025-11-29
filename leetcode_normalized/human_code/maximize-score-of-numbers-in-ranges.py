class C1(object):

    def maxPossibleScore(self, a1, a2):
        """
        """

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def check(a1):
            v1 = float('-inf')
            for v2 in a1:
                v1 = max(v1 + a1, v2)
                if v1 > v2 + a2:
                    return False
            return True
        a1.sort()
        return binary_search_right(1, a1[-1] + a2 - a1[0], check)
