class Solution:
    def kthSmallest(self, mat, target):
        def count_le(val):
            res = 0
            for row in mat:
                left, right = 0, len(row) - 1
                while left <= right:
                    md = (left + right) // 2
                    if row[md] <= val:
                        left = md + 1
                    else:
                        right = md - 1
                res += left
            return res
        
        l, r = mat[0][0], mat[-1][-1]
        while l < r:
            md = (l + r) // 2
            if count_le(md) >= target:
                r = md
            else:
                l = md + 1
        return l
