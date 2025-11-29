class Solution:
    def splitArray(self, nums, m):
        def can_partition(maximum):
            segments = 1
            prefix = 0
            for element in nums:
                if prefix + element > maximum:
                    segments += 1
                    prefix = element
                else:
                    prefix += element
            return segments <= m

        minimum = max(nums)
        maximum = sum(nums)
        lower = minimum
        upper = maximum
        while lower < upper:
            middle = (lower + upper) // 2
            if can_partition(middle):
                upper = middle
            else:
                lower = middle + 1
        return lower
