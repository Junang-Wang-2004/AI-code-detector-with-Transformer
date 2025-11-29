class Solution:
    def minCost(self, nums1, nums2, fee):
        n = len(nums1)
        current = 0
        for i in range(n):
            current += abs(nums1[i] - nums2[i])
        nums1.sort()
        nums2.sort()
        optimal = 0
        for i in range(n):
            optimal += abs(nums1[i] - nums2[i])
        return min(current, fee + optimal)
