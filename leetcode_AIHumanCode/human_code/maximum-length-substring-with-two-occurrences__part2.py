# Time:  O(n + 26)
# Space: O(26)
# freq table, sliding window, two pointers
class Solution2(object):
    def maximumLengthSubstring(self, s):
        """
        """
        COUNT = 2
        result = 0
        cnt = [0]*26
        left = 0
        for right, x in enumerate(s):
            cnt[ord(x)-ord('a')] += 1
            while cnt[ord(x)-ord('a')] > COUNT:
                cnt[ord(s[left])-ord('a')] -= 1
                left += 1
            result = max(result, right-left+1)
        return result
