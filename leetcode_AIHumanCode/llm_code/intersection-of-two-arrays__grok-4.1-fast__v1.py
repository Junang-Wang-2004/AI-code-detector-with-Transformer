class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = []
        p, q = 0, 0
        m, n = len(nums1), len(nums2)
        while p < m and q < n:
            if nums1[p] == nums2[q]:
                result.append(nums1[p])
                target = nums1[p]
                while p < m and nums1[p] == target:
                    p += 1
                while q < n and nums2[q] == target:
                    q += 1
            elif nums1[p] < nums2[q]:
                p += 1
            else:
                q += 1
        return result
