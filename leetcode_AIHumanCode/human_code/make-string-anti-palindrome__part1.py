# Time:  O(n + 26)
# Space: O(26)

# counting sort, greedy
class Solution(object):
    def makeAntiPalindrome(self, s):
        """
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [i for i, x in enumerate(cnt) for _ in range(x)]
        l = next(l for l in range((len(s)//2)//2+1) if result[len(s)//2+l] != result[len(s)//2-1])
        if l:
            for i in range(cnt[result[len(s)//2-1]]-l):
                result[len(s)//2+i], result[len(s)//2+i+l] = result[len(s)//2+i+l], result[len(s)//2+i]
        return "".join([chr(ord('a')+x) for x in result])


