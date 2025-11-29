class Solution:
    def maximumsSplicedArray(self, nums1, nums2):
        total1 = total2 = max_gain1 = max_gain2 = curr1 = curr2 = 0
        length = len(nums1)
        for i in range(length):
            total1 += nums1[i]
            delta1 = nums2[i] - nums1[i]
            curr1 = max(0, curr1 + delta1)
            max_gain1 = max(max_gain1, curr1)
            
            total2 += nums2[i]
            delta2 = nums1[i] - nums2[i]
            curr2 = max(0, curr2 + delta2)
            max_gain2 = max(max_gain2, curr2)
        return max(total1 + max_gain1, total2 + max_gain2)
