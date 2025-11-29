class Solution:
    def countOfPeaks(self, nums, queries):
        n = len(nums)
        
        class Fenwick:
            def __init__(self, size):
                self.size = size
                self.tree = [0] * (size + 1)
            
            def update(self, i, val):
                i += 1
                while i <= self.size:
                    self.tree[i] += val
                    i += i & -i
            
            def prefix(self, i):
                i += 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res
        
        ft = Fenwick(n)
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                ft.update(i, 1)
        
        res = []
        for q in queries:
            t, l, r = q
            if t == 1:
                if r - 1 < l + 1:
                    res.append(0)
                else:
                    res.append(ft.prefix(r - 1) - ft.prefix(l))
            else:
                deltas_pos = range(max(l - 1, 1), min(l + 2, n - 1))
                for pos in deltas_pos:
                    if nums[pos - 1] < nums[pos] > nums[pos + 1]:
                        ft.update(pos, -1)
                nums[l] = r
                for pos in deltas_pos:
                    if nums[pos - 1] < nums[pos] > nums[pos + 1]:
                        ft.update(pos, 1)
        return res
