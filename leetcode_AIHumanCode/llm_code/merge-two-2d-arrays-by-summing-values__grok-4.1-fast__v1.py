class Solution(object):
    def mergeArrays(self, nums1, nums2):
        combined = []
        x, y = 0, 0
        m, n = len(nums1), len(nums2)
        while x < m or y < n:
            if y == n or (x < m and nums1[x][0] < nums2[y][0]):
                combined.append(nums1[x])
                x += 1
            else:
                combined.append(nums2[y])
                y += 1
        if not combined:
            return []
        ans = []
        prev = list(combined[0])
        for elem in combined[1:]:
            if elem[0] == prev[0]:
                prev[1] += elem[1]
            else:
                ans.append(prev)
                prev = list(elem)
        ans.append(prev)
        return ans
