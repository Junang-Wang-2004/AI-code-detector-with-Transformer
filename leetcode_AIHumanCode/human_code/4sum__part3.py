# Time:  O(n^2 * p) ~ O(n^4)
# Space: O(n^2)
class Solution3(object):
    def fourSum(self, nums, target):
        """
        """
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                lookup[nums[i] + nums[j]].append([i, j])

        for i in list(lookup.keys()):
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and \
                           b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)

