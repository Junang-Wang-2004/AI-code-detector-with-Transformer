import heapq
from collections import Counter

class Solution:
    def minimumCost(self, nums, k, dist):
        if k == 1:
            return nums[0]
        curr = 0
        best = float('inf')
        lo = []
        hi = []
        mark_lo = Counter()
        mark_hi = Counter()
        cnt_lo = [0]
        cnt_hi = [0]
        for i in range(1, len(nums)):
            v = nums[i]
            heapq.heappush(lo, -v)
            curr += v
            while len(lo) - cnt_lo[0] > k - 1:
                while lo and lo[0] in mark_lo:
                    x = heapq.heappop(lo)
                    mark_lo[x] -= 1
                    if mark_lo[x] == 0:
                        del mark_lo[x]
                    cnt_lo[0] -= 1
                if lo:
                    x = heapq.heappop(lo)
                    u = -x
                    heapq.heappush(hi, u)
                    curr -= u
            if i > dist + 1:
                oldv = nums[i - dist - 1]
                while hi and hi[0] in mark_hi:
                    x = heapq.heappop(hi)
                    mark_hi[x] -= 1
                    if mark_hi[x] == 0:
                        del mark_hi[x]
                    cnt_hi[0] -= 1
                if hi and hi[0] <= oldv:
                    mark_hi[oldv] += 1
                    cnt_hi[0] += 1
                else:
                    mark_lo[-oldv] += 1
                    cnt_lo[0] += 1
                    x = heapq.heappop(hi)
                    curr -= oldv - x
                    heapq.heappush(lo, -x)
                if cnt_lo[0] > len(lo) // 2:
                    new_lo = []
                    for p in lo:
                        if p in mark_lo:
                            mark_lo[p] -= 1
                            if mark_lo[p] == 0:
                                del mark_lo[p]
                        else:
                            new_lo.append(p)
                    lo[:] = new_lo
                    heapq.heapify(lo)
                    cnt_lo[0] = 0
                if cnt_hi[0] > len(hi) // 2:
                    new_hi = []
                    for p in hi:
                        if p in mark_hi:
                            mark_hi[p] -= 1
                            if mark_hi[p] == 0:
                                del mark_hi[p]
                        else:
                            new_hi.append(p)
                    hi[:] = new_hi
                    heapq.heapify(hi)
                    cnt_hi[0] = 0
            while lo and lo[0] in mark_lo:
                x = heapq.heappop(lo)
                mark_lo[x] -= 1
                if mark_lo[x] == 0:
                    del mark_lo[x]
                cnt_lo[0] -= 1
            if len(lo) - cnt_lo[0] == k - 1:
                best = min(best, curr)
        return nums[0] + best
