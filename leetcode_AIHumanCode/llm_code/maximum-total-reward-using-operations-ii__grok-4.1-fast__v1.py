class Solution(object):
    def maxTotalReward(self, rewardValues):
        mx = max(rewardValues)
        candidates = sorted(v for v in set(rewardValues) if v < mx)
        cap = (1 << mx) - 1
        bits = 1
        for reward in candidates:
            segment = bits & ((1 << reward) - 1)
            bits |= (segment << reward) & cap
        highest_small = bits.bit_length() - 1
        return mx + highest_small
