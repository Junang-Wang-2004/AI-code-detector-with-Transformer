class C1(object):

    def punishmentNumber(self, a1):
        """
        """

        def backtracking(a1, a2):
            if a2 == 0:
                return a1 == 0
            v1 = 10
            while a1 >= v1 // 10:
                v2, v3 = divmod(a1, v1)
                if a2 - v3 < 0:
                    break
                if backtracking(v2, a2 - v3):
                    return True
                v1 *= 10
            return False
        return sum((i ** 2 for v1 in range(1, a1 + 1) if backtracking(v1 ** 2, v1)))
