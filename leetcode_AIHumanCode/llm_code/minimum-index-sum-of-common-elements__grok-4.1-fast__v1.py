class Solution(object):
    def minimumSum(self, nums1, nums2):
        pos = {}
        for j, num in enumerate(nums2):
            if num not in pos:
                pos[num] = j
        minimum = float('inf')
        n = len(nums1)
        for i in range(n):
            if nums1[i] in pos:
                minimum = min(minimum, i + pos[nums1[i]])
        return minimum if minimum != float('inf') else -1
