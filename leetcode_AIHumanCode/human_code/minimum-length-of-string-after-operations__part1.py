# Time:  O(n + 26)
# Space: O(26)

# freq table
class Solution(object):
    def minimumLength(self, s):
        """
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        return sum(2-x%2 for x in cnt if x)


