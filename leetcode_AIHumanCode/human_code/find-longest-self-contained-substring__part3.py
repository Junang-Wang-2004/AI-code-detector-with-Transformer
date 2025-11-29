# Time:  O(26 * n)
# Space: O(26)
# freq table, two pointers
class Solution3(object):
    def maxSubstringLength(self, s):
        """
        """
        def update(x, d, distinct, valid):
            x = ord(x)-ord('a')
            if cnt2[x] == cnt[x]:
                valid -= 1
            if cnt2[x] == 0:
                distinct += 1
            cnt2[x] += d
            if cnt2[x] == 0:
                distinct -= 1
            if cnt2[x] == cnt[x]:
                valid += 1
            return distinct, valid
                
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        result = -1
        for l in range(1, sum(x != 0 for x in cnt)):
            cnt2 = [0]*26
            left = distinct = valid = 0
            for right in range(len(s)):
                distinct, valid = update(s[right], +1, distinct, valid)
                while distinct == l+1:
                    distinct, valid = update(s[left], -1, distinct, valid)
                    left += 1
                if valid == l:
                    result = max(result, right-left+1)
        return result


