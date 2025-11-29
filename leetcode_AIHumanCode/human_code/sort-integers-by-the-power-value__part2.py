# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    dp = {}

    def getKth(self, lo, hi, k):
        """
        """
        def power_value(x):
            y, result = x, 0
            while x > 1 and x not in Solution2.dp:
                result += 1
                if x%2:
                    x = 3*x + 1
                else:
                    x //= 2
            Solution2.dp[y] = result + (Solution2.dp[x] if x > 1 else 0)
            return Solution2.dp[y], y
        
        return sorted(list(range(lo, hi+1)), key=power_value)[k-1]
