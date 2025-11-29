# Time:  O(m + n)
# Space: O(min(m, n))

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        """
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        for i in nums1:
            lookup.add(i)

        res = []
        for i in nums2:
            if i in lookup:
                res += i,
                lookup.discard(i)

        return res

    def intersection2(self, nums1, nums2):
        """
        """
        return list(set(nums1) & set(nums2))


