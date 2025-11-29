# Time:  O(n * m)
# Space: O(min(n, m))
# dp
class Solution3(object):
    def minOperations(self, initial, target):
        """
        """
        if len(initial) < len(target):
            initial, target = target, initial
        result = 0
        dp = [0]*(len(target)+1)
        for i in range(len(initial)):
            for j in reversed(range(len(target))):
                dp[j+1] = dp[j]+1 if initial[i] == target[j] else 0
            result = max(result, max(dp))
        return len(initial)+len(target)-2*result
