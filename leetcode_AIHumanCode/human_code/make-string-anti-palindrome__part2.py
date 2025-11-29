# Time:  O(n + 26)
# Space: O(26)
# counting sort, greedy, two pointers
class Solution2(object):
    def makeAntiPalindrome(self, s):
        """
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [i for i, x in enumerate(cnt) for _ in range(x)]
        left = len(s)//2
        right = left+1
        while right < len(s) and result[right] == result[left]:
            right += 1 
        while result[left] == result[len(s)-1-left]:
            result[left] , result[right] = result[right], result[left]
            left += 1
            right += 1
        return "".join([chr(ord('a')+x) for x in result])
    

