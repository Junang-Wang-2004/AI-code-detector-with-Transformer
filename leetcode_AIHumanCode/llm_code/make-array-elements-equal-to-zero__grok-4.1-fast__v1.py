class Solution:
    def countValidSelections(self, arr):
        overall = sum(arr)
        ways = 0
        left_sum = 0
        for num in arr:
            if num == 0:
                delta = abs(2 * left_sum - overall)
                ways += max(2 - delta, 0)
            left_sum += num
        return ways
