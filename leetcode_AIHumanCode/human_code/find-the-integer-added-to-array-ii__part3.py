# Time:  O(nlogn)
# Space: O(1)
# sort
class Solution3(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        """
        nums1.sort()
        nums2.sort()
        for i in range(3):
            d = nums2[-1]-nums1[~i]
            cnt = 0
            for j in range(len(nums2)):
                while j+cnt < len(nums1) and nums1[j+cnt]+d != nums2[j]:
                    cnt += 1
            if cnt <= 2:
                return d
        return -1
