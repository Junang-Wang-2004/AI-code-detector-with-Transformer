class C1(object):

    def sumOfNumberAndReverse(self, a1):
        """
        """

        def backtracking(a1, a2):
            if a1 == 0:
                return True
            if a2 == 1:
                return False
            if a1 <= 18:
                return a1 % 2 == 0 or (a1 == 11 and a2 == 0)
            if a2 == 2:
                return False
            for v1 in (a1 % 10, 10 + a1 % 10):
                if not 1 <= v1 <= 18:
                    continue
                v2 = 11
                if a2:
                    v2 = a2
                else:
                    while v1 * ((v2 - 1) * 10 + 1) <= a1:
                        v2 = (v2 - 1) * 10 + 1
                if a1 - v1 * v2 >= 0 and backtracking((a1 - v1 * v2) // 10, v2 // 100 + 1):
                    return True
            return False
        return backtracking(a1, 0)
