class Solution(object):
    def maximumSum(self, nums):
        groups = {}
        for num in nums:
            digsum = sum(int(c) for c in str(num))
            if digsum not in groups:
                groups[digsum] = []
            groups[digsum].append(num)
        maxsum = -1
        for group in groups.values():
            if len(group) >= 2:
                group.sort(reverse=True)
                maxsum = max(maxsum, group[0] + group[1])
        return maxsum
