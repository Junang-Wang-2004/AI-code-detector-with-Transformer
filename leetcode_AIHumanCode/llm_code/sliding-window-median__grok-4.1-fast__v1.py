import collections
import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo = []  # max-heap (negated) for lower half
        hi = []  # min-heap for upper half
        del_count = collections.defaultdict(int)

        def purge(heap, sgn):
            while heap and sgn * heap[0] in del_count:
                val = sgn * heap[0]
                del_count[val] -= 1
                if del_count[val] == 0:
                    del del_count[val]
                heapq.heappop(heap)

        def restore():
            curr = []
            for nv in lo:
                v = -nv
                if v not in del_count or del_count[v] == 0:
                    curr.append(v)
                else:
                    del_count[v] -= 1
                    if del_count[v] == 0:
                        del del_count[v]
            for v in hi:
                if v not in del_count or del_count[v] == 0:
                    curr.append(v)
                else:
                    del_count[v] -= 1
                    if del_count[v] == 0:
                        del del_count[v]
            lo.clear()
            hi.clear()
            curr.sort()
            half = (k + 1) // 2
            for j in range(half):
                heapq.heappush(lo, -curr[j])
            for j in range(half, k):
                heapq.heappush(hi, curr[j])

        medians = []

        # Initialize first window
        for val in nums[:k]:
            if len(lo) == 0 or val <= -lo[0]:
                heapq.heappush(lo, -val)
            else:
                heapq.heappush(hi, val)
            # Rebalance sizes
            if len(lo) > len(hi) + 1:
                heapq.heappush(hi, -heapq.heappop(lo))
            if len(hi) > len(lo):
                heapq.heappush(lo, -heapq.heappop(hi))
        purge(lo, -1)
        purge(hi, 1)
        median = float(-lo[0]) if k % 2 else (-lo[0] + hi[0]) / 2
        medians.append(median)

        # Process remaining windows
        for i in range(k, len(nums)):
            del_count[nums[i - k]] += 1
            val = nums[i]
            purge(lo, -1)
            purge(hi, 1)
            if len(lo) == 0 or val <= -lo[0]:
                heapq.heappush(lo, -val)
            else:
                heapq.heappush(hi, val)
            if len(lo) > len(hi) + 1:
                heapq.heappush(hi, -heapq.heappop(lo))
            if len(hi) > len(lo):
                heapq.heappush(lo, -heapq.heappop(hi))
            if len(lo) + len(hi) > 2 * k:
                restore()
            purge(lo, -1)
            purge(hi, 1)
            median = float(-lo[0]) if k % 2 else (-lo[0] + hi[0]) / 2
            medians.append(median)

        return medians
