# Time:  O(max(m, n) * log(max(m, n)))
# Space: O(1)
# Two pointers solution.
class Solution3(object):
    def intersection(self, nums1, nums2):
        """
        """
        nums1.sort(), nums2.sort()
        res = []

        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                if not res or res[-1] != nums1[it1]:
                    res += nums1[it1],
                it1 += 1
                it2 += 1

        return res

