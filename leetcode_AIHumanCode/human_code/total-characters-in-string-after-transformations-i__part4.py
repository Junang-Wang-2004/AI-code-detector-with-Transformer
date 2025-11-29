# Time:  O(n + t * 26)
# Space: O(26)
# dp
class Solution4(object):
    def lengthAfterTransformations(self, s, t):
        """
        """
        MOD = 10**9+7
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        for _ in range(t):
            new_cnt = [0]*26
            for i in range(26):
                new_cnt[(i+1)%26] = (new_cnt[(i+1)%26]+cnt[i])%MOD
                if i == 25:
                    new_cnt[(i+2)%26] = (new_cnt[(i+2)%26]+cnt[i])%MOD
            cnt = new_cnt
        return reduce(lambda accu, x: (accu+x)%MOD, cnt, 0)
