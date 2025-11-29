# Time:  O(n * 26)
# Space: O(26)
# freq table, greedy
class Solution3(object):
    def makeAntiPalindrome(self, s):
        """
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [-1]*len(s)
        for i in range(len(s)//2):
            j = next(j for j in range(len(cnt)) if cnt[j])
            cnt[j] -= 1
            result[i] = j
        for i in range(len(s)//2, len(s)):
            j = next(j for j in range(len(cnt)) if cnt[j] and result[(len(s)-1)-i] != j)
            cnt[j] -= 1
            result[i] = j
        return "".join([chr(ord('a')+x) for x in result])
