class Solution:
    def canReach(self, nums, pos):
        n = len(nums)
        visited = set([pos])
        stk = [pos]
        while stk:
            curr = stk.pop()
            if nums[curr] == 0:
                return True
            step = nums[curr]
            for nxt_pos in [curr - step, curr + step]:
                if 0 <= nxt_pos < n and nxt_pos not in visited:
                    visited.add(nxt_pos)
                    stk.append(nxt_pos)
        return False
