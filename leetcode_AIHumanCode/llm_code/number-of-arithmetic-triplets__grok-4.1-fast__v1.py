class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        pos = {}
        for i, val in enumerate(nums):
            pos.setdefault(val, []).append(i)
        count = 0
        for a in pos:
            b = a + diff
            c = b + diff
            if b in pos and c in pos:
                count += len(pos[a]) * len(pos[b]) * len(pos[c])
        return count
