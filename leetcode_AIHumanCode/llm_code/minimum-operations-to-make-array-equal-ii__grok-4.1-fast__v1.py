class Solution:
    def minOperations(self, nums1, nums2, k):
        deficit = surplus = 0
        n = len(nums1)
        for i in range(n):
            a = nums1[i]
            b = nums2[i]
            d = b - a
            if d != 0:
                if k == 0 or d % k != 0:
                    return -1
                moves = abs(d) // k
                if d > 0:
                    deficit += moves
                else:
                    surplus += moves
        return deficit if deficit == surplus else -1
