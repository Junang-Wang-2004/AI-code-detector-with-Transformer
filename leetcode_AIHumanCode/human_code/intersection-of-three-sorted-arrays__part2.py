from functools import reduce
# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        """
        intersect = reduce(set.intersection, list(map(set, [arr2, arr3])))
        return [x for x in arr1 if x in intersect]
