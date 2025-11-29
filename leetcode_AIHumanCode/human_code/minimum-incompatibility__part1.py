# Time:  O(sum(i*d * nCr(i*d, d) * nCr(n, i*d) for i in xrange(1, k+1))) < O(sum(n * 2^m * nCr(n, m) for m in xrange(n+1))) = O(n * 3^n)
# Space: O(n * k)

import itertools


class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        """
        inf = (len(nums)-1)*(len(nums)//k)+1
        def backtracking(nums, d, lookup):
            if not nums:
                return 0
            if nums not in lookup:
                ret = inf
                for new_nums in itertools.combinations(nums, d):
                    new_nums_set = set(new_nums)
                    if len(new_nums_set) < d:
                        continue
                    left = []
                    for num in nums:
                        if num in new_nums_set:
                            new_nums_set.remove(num)
                            continue
                        left.append(num)
                    ret = min(ret, max(new_nums)-min(new_nums) + backtracking(tuple(left), d, lookup))
                lookup[nums] = ret
            return lookup[nums]
        
        result = backtracking(tuple(nums), len(nums)//k, {})
        return result if result != inf else -1


