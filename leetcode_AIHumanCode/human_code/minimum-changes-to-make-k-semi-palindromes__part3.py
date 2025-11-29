# Time:  O(n^2 * nlogn + n^2 * k) = O(n^3 * logn)
# Space: O(nlogn + n * k)
# number theory, dp
class Solution3(object):
    def minimumChanges(self, s, k):
        """
        """
        def min_dist(left, right):  # Time: O(nlogn)
            return min(sum(s[left+i] != s[right-((i//d+1)*d-1)+(i%d)] for i in range((right-left+1)//2))
 for d in divisors[right-left+1])

        divisors = [[] for _ in range(len(s)+1)]
        for i in range(1, len(divisors)):  # Time: O(nlogn), Space: O(nlogn)
            for j in range(i+i, len(divisors), i):
                divisors[j].append(i)
        dp = [[len(s)]*(k+1) for _ in range(len(s)+1)]
        dp[0][0] = 0
        for i in range(len(s)):  # Time: O(n^2 * nlogn + n^2 * k), Space: O(n * k)
            for j in range(i):
                c = min_dist(j, i)
                for l in range(k):
                    dp[i+1][l+1] = min(dp[i+1][l+1], dp[j][l]+c)
        return dp[len(s)][k]
