# Time:  O(n * nlogn + n^3 + n^2 * k) = O(n^3)
# Space: O(n * nlogn) = O(n^2 * logn)
# number theory, dp
class Solution2(object):
    def minimumChanges(self, s, k):
        """
        """
        divisors = [[] for _ in range(len(s)+1)]
        for i in range(1, len(divisors)):  # Time: O(nlogn), Space: O(nlogn)
            for j in range(i, len(divisors), i):
                divisors[j].append(i)
        dp = [[{} for _ in range(len(s))] for _ in range(len(s))]
        for l in range(1, len(s)+1):  # Time: O(n * nlogn + n^3), Space: O(n * nlogn)
            for left in range(len(s)-l+1):
                right = left+l-1
                for d in divisors[l]:
                    dp[left][right][d] = (dp[left+d][right-d][d] if left+d < right-d else 0)+sum(s[left+i] != s[(right-(d-1))+i] for i in range(d))
        dp2 = [[len(s)]*(k+1) for _ in range(len(s)+1)]
        dp2[0][0] = 0
        for i in range(len(s)):  # Time: O(n^2 * logn + n^2 * k), Space: O(n * k)
            for j in range(i):
                c = min(dp[j][i][d] for d in divisors[i-j+1] if d != i-j+1)
                for l in range(k):
                    dp2[i+1][l+1] = min(dp2[i+1][l+1], dp2[j][l]+c)
        return dp2[len(s)][k]


