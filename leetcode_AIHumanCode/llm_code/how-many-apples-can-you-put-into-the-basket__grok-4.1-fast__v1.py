class Solution:
    def maxNumberOfApples(self, weights):
        capacity = 5000
        sorted_weights = sorted(weights)
        current_load = 0
        count = 0
        while count < len(sorted_weights) and current_load + sorted_weights[count] <= capacity:
            current_load += sorted_weights[count]
            count += 1
        return count
