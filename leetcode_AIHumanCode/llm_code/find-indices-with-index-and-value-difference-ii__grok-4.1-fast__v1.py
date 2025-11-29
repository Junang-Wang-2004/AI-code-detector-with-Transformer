class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        n = len(nums)
        if n < indexDifference + 1:
            return [-1, -1]
        suf_min = [0] * n
        suf_max = [0] * n
        suf_min[n-1] = n-1
        suf_max[n-1] = n-1
        for k in range(n-2, -1, -1):
            if nums[k] < nums[suf_min[k+1]]:
                suf_min[k] = k
            else:
                suf_min[k] = suf_min[k+1]
            if nums[k] > nums[suf_max[k+1]]:
                suf_max[k] = k
            else:
                suf_max[k] = suf_max[k+1]
        for i in range(n - indexDifference):
            j_start = i + indexDifference
            if nums[i] - nums[suf_min[j_start]] >= valueDifference:
                return [i, suf_min[j_start]]
            if nums[suf_max[j_start]] - nums[i] >= valueDifference:
                return [i, suf_max[j_start]]
        return [-1, -1]
