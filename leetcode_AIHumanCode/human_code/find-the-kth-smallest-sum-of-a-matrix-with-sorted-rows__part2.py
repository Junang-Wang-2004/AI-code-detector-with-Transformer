# Time:  O((k + m) * log(m * MAX_NUM)) ~ O(k * m * log(m * MAX_NUM))
# Space: O(m)
class Solution2(object):
    def kthSmallest(self, mat, k):
        """
        """        
        def countArraysHaveSumLessOrEqual(mat, k, r, target):  # Time: O(k + m) ~ O(k * m)
            if target < 0:
                return 0
            if r == len(mat):
                return 1
            result = 0
            for c in range(len(mat[0])):
                cnt = countArraysHaveSumLessOrEqual(mat, k-result, r+1, target-mat[r][c])
                if not cnt:
                    break
                result += cnt
                if result > k:
                    break
            return result
        
        max_num = max(x for row in mat for x in row)
        left, right = len(mat), len(mat)*max_num
        while left <= right:
            mid = left + (right-left)//2
            cnt = countArraysHaveSumLessOrEqual(mat, k, 0, mid)
            if cnt >= k:
                right = mid-1
            else:
                left = mid+1
        return left

