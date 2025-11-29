class Solution:
    def maximumCostSubstring(self, s, chars, vals):
        overrides = dict(zip(chars, vals))
        letter_costs = [overrides.get(chr(ord('a') + i), i + 1) for i in range(26)]
        best = 0
        running = 0
        for ch in s:
            i = ord(ch) - ord('a')
            running = max(running + letter_costs[i], 0)
            best = max(best, running)
        return best
