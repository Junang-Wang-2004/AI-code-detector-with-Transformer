class Solution(object):
    def maxTotalFruits(self, fruits, spos, maxdist):
        maxreach = max(spos, max((p for p, _ in fruits), default=spos))
        counts = [0] * (maxreach + 1)
        for position, amount in fruits:
            counts[position] = amount
        presum = [0] * (maxreach + 2)
        for i in range(1, maxreach + 2):
            presum[i] = presum[i - 1] + counts[i - 1]
        best = 0
        for dleft in range(spos + 1):
            leftp = spos - dleft
            if leftp < 0:
                break
            opt1 = maxdist - 2 * dleft
            opt2 = (maxdist - dleft) // 2
            dright = max(0, opt1, opt2)
            rightp = min(maxreach, spos + dright)
            harvest = presum[rightp + 1] - presum[leftp]
            if harvest > best:
                best = harvest
        return best
