# Time:  O(n + w * l)
# Space: O(n + w * l)

# rolling hash, hash table, two pointers, sliding window, dp
class Solution(object):
    def minValidStrings(self, words, target):
        """
        """
        MOD, P = 10**9+7, 131
        power = [1]
        for _ in range(len(target)):
            power.append(power[-1]*P%MOD)
        lookup = set()
        for w in words:
            h = 0
            for x in w:
                h = (h*P+(ord(x)-ord('a')+1))%MOD
                lookup.add(h)
        dp = [0]*(len(target)+1)
        left = h = 0
        for right in range(len(target)):
            h = (h*P+(ord(target[right])-ord('a')+1))%MOD
            while right-left+1 >= 1 and h not in lookup:
                h = (h-(ord(target[left])-ord('a')+1)*power[(right-left+1)-1])%MOD
                left += 1
            if right-left+1 == 0:
                return -1
            dp[right+1] = dp[(right-(right-left+1))+1]+1
        return dp[-1]


