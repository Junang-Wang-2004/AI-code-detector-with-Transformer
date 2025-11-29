class Solution:
    def canBeEqual(self, goal, vals):
        freq = {}
        for num in goal:
            freq[num] = freq.get(num, 0) + 1
        for num in vals:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1
        return True
