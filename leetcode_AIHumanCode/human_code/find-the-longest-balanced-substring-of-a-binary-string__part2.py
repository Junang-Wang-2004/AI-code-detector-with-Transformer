# Time:  O(n)
# Space: O(1)
# string
class Solution2(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        """
        result = 0
        prev, cnt = [0]*2, [0]*2
        for c in s:
            cnt[int(c)] += 1
            if cnt[int(c)^1]:
                prev[int(c)^1], cnt[int(c)^1] = cnt[int(c)^1], 0
            result = max(result, 2*min(prev[0], cnt[1]))
        return result
