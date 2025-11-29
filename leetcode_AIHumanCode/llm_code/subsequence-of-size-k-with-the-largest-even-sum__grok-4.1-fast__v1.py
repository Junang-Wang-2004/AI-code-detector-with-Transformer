class Solution:
    def largestEvenSum(self, nums, k):
        arr = sorted(nums, reverse=True)
        prefix = sum(arr[:k])
        if prefix % 2 == 0:
            return prefix
        
        min_even_in = float('inf')
        min_odd_in = float('inf')
        for val in arr[:k]:
            if val % 2 == 0:
                min_even_in = min(min_even_in, val)
            else:
                min_odd_in = min(min_odd_in, val)
        
        max_even_out = float('-inf')
        max_odd_out = float('-inf')
        for val in arr[k:]:
            if val % 2 == 0:
                max_even_out = max(max_even_out, val)
            else:
                max_odd_out = max(max_odd_out, val)
        
        candidates = []
        if min_odd_in != float('inf') and max_even_out != float('-inf'):
            candidates.append(prefix - min_odd_in + max_even_out)
        if min_even_in != float('inf') and max_odd_out != float('-inf'):
            candidates.append(prefix - min_even_in + max_odd_out)
        
        return max(candidates) if candidates else -1
