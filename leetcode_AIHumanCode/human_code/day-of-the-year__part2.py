# Time:  O(1)
# Space: O(1)
class Solution2(object):
    def dayOfYear(self, date):
        """
        """
        def numberOfDays(Y, M):
            leap = 1 if ((Y % 4 == 0) and (Y % 100 != 0)) or (Y % 400 == 0) else 0
            return (28+leap if (M == 2) else 31-(M-1)%7%2)

        Y, M, result = list(map(int, date.split("-")))
        for i in range(1, M):
            result += numberOfDays(Y, i)
        return result
