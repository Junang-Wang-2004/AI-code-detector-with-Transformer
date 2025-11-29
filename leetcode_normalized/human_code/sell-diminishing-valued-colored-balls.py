class C1(object):

    def maxProfit(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def check(a1, a2, a3):
            return count(a1, a3) > a2

        def count(a1, a2):
            return sum((count - a2 + 1 for v1 in a1 if v1 >= a2))
        v2, v3 = (1, max(a1))
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if not check(a1, a2, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return (sum(((v2 + cnt) * (cnt - v2 + 1) // 2 for v5 in a1 if v5 >= v2)) + (v2 - 1) * (a2 - count(a1, v2))) % v1
