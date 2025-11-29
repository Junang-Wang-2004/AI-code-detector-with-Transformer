import heapq

class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        if multiplier == 1:
            return nums
        n = len(nums)
        minheap = [(nums[i], i) for i in range(n)]
        heapq.heapify(minheap)
        maxnum = max(nums)
        done = 0
        while done < k:
            curmin, pos = minheap[0]
            if curmin * multiplier > maxnum:
                break
            heapq.heappop(minheap)
            heapq.heappush(minheap, (curmin * multiplier, pos))
            done += 1
        remain = k - done
        currstate = []
        while minheap:
            currstate.append(heapq.heappop(minheap))
        full, extra = divmod(remain, n)
        mult_full = pow(multiplier, full)
        ans = [0] * n
        for rank in range(n):
            val, pos = currstate[rank]
            bonus = multiplier if rank < extra else 1
            ans[pos] = val * mult_full * bonus
        return ans
