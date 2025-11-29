class Solution:
    def longestBalanced(self, nums):
        m = len(nums)
        class SegTree:
            def __init__(self, size):
                self.size = size
                self.tmin = [0] * (4 * size)
                self.tmax = [0] * (4 * size)
                self.lazy = [0] * (4 * size)

            def propagate(self, idx, left, right):
                if self.lazy[idx]:
                    self.tmin[idx] += self.lazy[idx]
                    self.tmax[idx] += self.lazy[idx]
                    if left != right:
                        self.lazy[2 * idx] += self.lazy[idx]
                        self.lazy[2 * idx + 1] += self.lazy[idx]
                    self.lazy[idx] = 0

            def update_range(self, ul, ur, value, idx=1, left=0, right=None):
                if right is None:
                    right = self.size - 1
                self.propagate(idx, left, right)
                if ul > right or ur < left:
                    return
                if ul <= left and right <= ur:
                    self.lazy[idx] += value
                    self.propagate(idx, left, right)
                    return
                mid = (left + right) // 2
                self.update_range(ul, ur, value, 2 * idx, left, mid)
                self.update_range(ul, ur, value, 2 * idx + 1, mid + 1, right)
                self.tmin[idx] = min(self.tmin[2 * idx], self.tmin[2 * idx + 1])
                self.tmax[idx] = max(self.tmax[2 * idx], self.tmax[2 * idx + 1])

            def get_leftmost(self, target, idx=1, left=0, right=None):
                if right is None:
                    right = self.size - 1
                self.propagate(idx, left, right)
                if self.tmin[idx] > target or self.tmax[idx] < target:
                    return float('inf')
                if left == right:
                    return left if self.tmin[idx] == target else float('inf')
                mid = (left + right) // 2
                res_left = self.get_leftmost(target, 2 * idx, left, mid)
                if res_left != float('inf'):
                    return res_left
                return self.get_leftmost(target, 2 * idx + 1, mid + 1, right)

        tree = SegTree(m + 1)
        recent = {}
        bal = 0
        best = 0
        for pos in range(1, m + 1):
            val = nums[pos - 1]
            incr = 1 if (val & 1) else -1
            if val in recent:
                prior = recent[val]
                tree.update_range(prior, m, -incr)
                bal -= incr
            bal += incr
            recent[val] = pos
            tree.update_range(pos, m, incr)
            start = tree.get_leftmost(bal)
            leng = pos - start
            if leng > best:
                best = leng
        return best
