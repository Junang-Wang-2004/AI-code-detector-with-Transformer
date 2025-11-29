import heapq

class Solution:
    def convertArray(self, nums):
        def calc_cost(iterable):
            cost = 0
            h = []
            for n in iterable:
                if h and -h[0] > n:
                    prev_max = -heapq.heappop(h)
                    cost += prev_max - n
                    heapq.heappush(h, -n)
                heapq.heappush(h, -n)
            return cost
        a = calc_cost(nums)
        b = calc_cost(reversed(nums))
        return min(a, b)
