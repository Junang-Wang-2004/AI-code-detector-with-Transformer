class Solution(object):
    def getCommon(self, nums1, nums2):
        p = 0
        q = 0
        while True:
            if p >= len(nums1) or q >= len(nums2):
                return -1
            if nums1[p] == nums2[q]:
                return nums1[p]
            if nums1[p] < nums2[q]:
                p += 1
            else:
                q += 1
