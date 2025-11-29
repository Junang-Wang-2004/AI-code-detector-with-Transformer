# Time:  O(n * (26 + n))
# Space: O(26)
# freq table
class Solution2(object):
    def longestBalanced(self, s):
        """
        """
        result = 0
        for i in range(len(s)):
            cnt = [0]*26
            mx = unique = 0
            for j in range(i, len(s)):
                if cnt[ord(s[j])-ord('a')] == 0:
                    unique += 1
                cnt[ord(s[j])-ord('a')] += 1
                mx = max(mx, cnt[ord(s[j])-ord('a')])
                if (j-i+1)%unique == 0 and (j-i+1)//unique == mx:
                    result = max(result, j-i+1)
        return result
