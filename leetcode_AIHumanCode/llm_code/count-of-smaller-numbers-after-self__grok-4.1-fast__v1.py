class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        vals = sorted(set(nums))
        pos = {v: i + 1 for i, v in enumerate(vals)}
        sz = len(vals)
        fen = [0] * (sz + 1)
        out = [0] * len(nums)

        def modify(index, amount):
            while index <= sz:
                fen[index] += amount
                index += index & -index

        def prefix_sum(index):
            sm = 0
            while index > 0:
                sm += fen[index]
                index -= index & -index
            return sm

        for j in range(len(nums) - 1, -1, -1):
            rk = pos[nums[j]]
            out[j] = prefix_sum(rk - 1)
            modify(rk, 1)
        return out
