class Solution(object):
    def splitArraySameAverage(self, nums):
        arr_size = len(nums)
        arr_sum = sum(nums)
        max_subset_size = arr_size // 2
        if not any((arr_sum * k) % arr_size == 0 for k in range(1, max_subset_size + 1)):
            return False
        achievable = {0: {0}}
        for element in nums:
            additions = {}
            for size, sum_values in list(achievable.items()):
                for current_sum in sum_values:
                    new_size = size + 1
                    if new_size > max_subset_size:
                        continue
                    if new_size not in additions:
                        additions[new_size] = set()
                    additions[new_size].add(current_sum + element)
            for new_size, new_sum_values in additions.items():
                if new_size not in achievable:
                    achievable[new_size] = set()
                achievable[new_size].update(new_sum_values)
        for subset_size in range(1, max_subset_size + 1):
            if (arr_sum * subset_size) % arr_size == 0:
                required_sum = (arr_sum * subset_size) // arr_size
                if required_sum in achievable.get(subset_size, set()):
                    return True
        return False
