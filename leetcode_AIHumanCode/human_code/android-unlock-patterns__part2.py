# Time:  O(9^2 * 2^9)
# Space: O(9 * 2^9)
# DP solution.
class Solution2(object):
    def numberOfPatterns(self, m, n):
        """
        """
        def merge(used, i):
            return used | (1 << i)

        def number_of_keys(i):
            number = 0
            while i > 0:
                i &= i - 1
                number += 1
            return number

        def exclude(used, i):
            return used & ~(1 << i)

        def contain(used, i):
            return bool(used & (1 << i))

        def convert(i, j):
            return 3 * i + j

        # dp[i][j]: i is the set of the numbers in binary representation,
        #            d[i][j] is the number of ways ending with the number j.
        dp = [[0] * 9 for _ in range(1 << 9)]
        for i in range(9):
            dp[merge(0, i)][i] = 1

        res = 0
        for used in range(len(dp)):
            number = number_of_keys(used)
            if number > n:
                continue

            for i in range(9):
                if not contain(used, i):
                    continue

                x1, y1 = divmod(i, 3)
                for j in range(9):
                    if i == j or not contain(used, j):
                        continue

                    x2, y2 = divmod(j, 3)
                    if ((x1 == x2 and abs(y1 - y2) == 2) or
                        (y1 == y2 and abs(x1 - x2) == 2) or
                        (abs(x1 - x2) == 2 and abs(y1 - y2) == 2)) and \
                       not contain(used,
                                   convert((x1 + x2) // 2, (y1 + y2) // 2)):
                            continue

                    dp[used][i] += dp[exclude(used, i)][j]

                if m <= number <= n:
                    res += dp[used][i]

        return res


