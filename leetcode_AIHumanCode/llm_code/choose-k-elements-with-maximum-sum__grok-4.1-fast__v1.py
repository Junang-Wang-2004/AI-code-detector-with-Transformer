import heapq

class Solution:
    def findMaxSum(self, nums1, nums2, k):
        n = len(nums1)
        ans = [0] * n
        positions = sorted(range(n), key=lambda idx: nums1[idx])
        pq = []
        prefix_sum = 0
        pos = 0
        while pos < n:
            val = nums1[positions[pos]]
            grp_begin = pos
            while pos < n and nums1[positions[pos]] == val:
                pos += 1
            for j in range(grp_begin, pos):
                ans[positions[j]] = prefix_sum
            for j in range(grp_begin, pos):
                num = nums2[positions[j]]
                prefix_sum += num
                heapq.heappush(pq, num)
                if len(pq) == k + 1:
                    prefix_sum -= heapq.heappop(pq)
        return ans
