class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        n = len(s)
        INF = n + 1
        memo = [[-1] * (k + 1) for _ in range(n + 1)]

        def group_cost(count):
            if count < 2:
                return count
            return 1 + len(str(count))

        def solve(start, deletes):
            if start == n:
                return 0
            if memo[start][deletes] != -1:
                return memo[start][deletes]
            result = INF
            if deletes > 0:
                result = solve(start + 1, deletes - 1)
            char = s[start]
            count = 0
            del_count = 0
            for end in range(start, n):
                if s[end] == char:
                    count += 1
                else:
                    del_count += 1
                if del_count > deletes:
                    break
                result = min(result, group_cost(count) + solve(end + 1, deletes - del_count))
            memo[start][deletes] = result
            return result

        return solve(0, k)
