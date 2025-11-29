# Time:  O(nlogn)
# Space: O(1)
import bisect


# sort, prefix sum, greedy, two pointers, improved from solution4
class Solution2(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        """
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+flowers[i]
        result = suffix = 0
        left = n
        for right in reversed(range(n+1)):
            if right != n:
                suffix += flowers[right]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                continue
            left = min(left, right)
            while not (left == 0 or (prefix[left]-prefix[left-1])*left-prefix[left] <= total):
                left -= 1
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result


