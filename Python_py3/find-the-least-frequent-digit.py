# Time:  O(logn + 10)
# Space: O(10)

# freq table
class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        """
        cnt = [0]*10
        while n:
            n, r = divmod(n, 10)
            cnt[r] += 1
        mn = min(x for x in cnt if x)
        return next(i for i in range(len(cnt)) if cnt[i] == mn)
