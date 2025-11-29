import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        if k <= 0 or not nums1 or not nums2:
            return result
        pq = []
        seen = set()
        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
        seen.add((0, 0))
        while pq and len(result) < k:
            _, x, y = heapq.heappop(pq)
            result.append([nums1[x], nums2[y]])
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx < len(nums1) and ny < len(nums2) and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    heapq.heappush(pq, (nums1[nx] + nums2[ny], nx, ny))
        return result
