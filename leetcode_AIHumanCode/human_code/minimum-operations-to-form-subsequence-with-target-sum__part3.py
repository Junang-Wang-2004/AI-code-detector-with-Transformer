# Time:  O(nlogn)
# Space: O(n)
import heapq


# codeforces, https://codeforces.com/problemset/problem/1303/D
# heap, greedy
class Solution3(object):
    def minOperations(self, nums, target):
        """
        """
        total = sum(nums)
        if total < target:
            return -1

        result = 0
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        while target:
            x = -heapq.heappop(max_heap)
            if x <= target:
                target -= x
                total -= x
            elif total-x >= target:
                total -= x
            else:
                heapq.heappush(max_heap, -x//2)
                heapq.heappush(max_heap, -x//2)
                result += 1
        return result


