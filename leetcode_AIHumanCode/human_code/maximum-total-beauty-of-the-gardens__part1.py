# Time:  O(nlogn)
# Space: O(1)

import bisect


# sort, prefix sum, greedy, two pointers, improved from solution3
class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        """
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix, suffix = 0, sum(flowers[i] for i in range(n))
        result = left = 0
        for right in range(n+1):
            if right:
                suffix -= flowers[right-1]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                continue
            while not (left == right or (left and (total+prefix)//left <= flowers[left])):
                prefix += flowers[left]
                left += 1
            mn = min((total+prefix)//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result


