class Solution:
    def maxTotalReward(self, rewardValues):
        if not rewardValues:
            return 0
        maxv = max(rewardValues)
        smalls = sorted(v for v in set(rewardValues) if v < maxv)
        poss = {0}
        for w in smalls:
            poss |= {s + w for s in poss if s < w}
        return maxv + max((s for s in poss if s < maxv), default=0)
