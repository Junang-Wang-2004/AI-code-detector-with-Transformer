class Solution(object):
    def elementInNums(self, nums, queries):
        size = len(nums)
        cycle_length = 2 * size
        output = []
        for pair in queries:
            step_count, position = pair
            adjusted_step = step_count % cycle_length
            if adjusted_step < size:
                available = size - adjusted_step
                candidate = nums[adjusted_step + position]
            else:
                available = adjusted_step - size
                candidate = nums[position]
            if position < available:
                output.append(candidate)
            else:
                output.append(-1)
        return output
