from functools import reduce
# Time:  O((b/2) * (n/(b/2)+1)^(b/2))
# Space: O((n/(b/2)+1)^(b/2))
# dp solution
class Solution2(object):
    def maxHappyGroups(self, batchSize, groups):
        """
        """
        count = [0]*batchSize
        for i in groups:
            count[i%len(count)] += 1
        result = count[0]
        count[0] = 0
        for i in range(1, len(count)//2+1):  # optimization
            pair_count = min(count[i], count[len(count)-i]) if 2*i != len(count) else count[i]//2
            result += pair_count
            count[i] -= pair_count
            count[len(count)-i] -= pair_count
        new_count = {i:c for i, c in enumerate(count) if c}
        max_mask = reduce(lambda total, c: total*(c+1), iter(new_count.values()), 1)
        dp = [0]*max_mask
        for mask in range(len(dp)):
            remain = 0
            curr, basis = mask, 1
            for i, c in new_count.items():
                ai = curr%(c+1)
                if ai:
                    dp[mask] = max(dp[mask], dp[mask-basis])
                remain = (remain+ai*i)%batchSize
                basis *= c+1
                curr //= c+1
            if mask != len(dp)-1 and remain == 0:
                dp[mask] += 1
        return result+dp[-1]
