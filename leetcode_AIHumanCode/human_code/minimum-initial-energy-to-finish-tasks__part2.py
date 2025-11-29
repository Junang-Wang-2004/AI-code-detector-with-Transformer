# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def minimumEffort(self, tasks):
        """
        """
        tasks.sort(key=lambda x: x[0]-x[1])  # sort by save in desc
        result = curr = 0
        for a, m in tasks:  # we need to pick all the saves, so greedily to pick the most save first is always better
            result += max(m-curr, 0)
            curr = max(curr, m)-a
        return result
