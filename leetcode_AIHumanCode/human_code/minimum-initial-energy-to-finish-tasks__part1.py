# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minimumEffort(self, tasks):
        """
        """
        tasks.sort(key=lambda x: x[1]-x[0])  # sort by waste in asc
        result = 0
        # you can see proof here, https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/discuss/944633/Explanation-on-why-sort-by-difference
        for a, m in tasks:  # we need to pick all the wastes, so greedily to pick the least waste first is always better
            result = max(result+a, m)
        return result


