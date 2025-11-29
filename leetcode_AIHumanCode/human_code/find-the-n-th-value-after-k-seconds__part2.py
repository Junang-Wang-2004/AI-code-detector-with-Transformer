# Time:  O(n * k)
# Space: O(n)
# prefix sum
class Solution2(object):
    def valueAfterKSeconds(self, n, k):
        """
        """
        MOD = 10**9+7
        prefix = [1]*n
        for _ in range(k):
            for i in range(1, n):
                prefix[i] = (prefix[i]+prefix[i-1])%MOD
        return prefix[-1]

