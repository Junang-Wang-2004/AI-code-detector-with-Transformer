class Solution:
    def countPairs(self, nums1, nums2):
        diffs = [a - b for a, b in zip(nums1, nums2)]
        diffs.sort()
        n = len(diffs)
        cnt = 0
        i, j = 0, n - 1
        while i < j:
            if diffs[i] + diffs[j] > 0:
                cnt += j - i
                j -= 1
            else:
                i += 1
        return cnt
