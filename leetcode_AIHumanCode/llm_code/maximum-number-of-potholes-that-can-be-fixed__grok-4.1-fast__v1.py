class Solution:
    def maxPotholes(self, road, budget):
        group_sizes = [len(run) for run in road.split('.') if run]
        group_sizes.sort(reverse=True)
        filled = 0
        funds = budget
        for size in group_sizes:
            req = size + 1
            alloc = min(req, funds)
            num_filled = alloc - 1
            if num_filled <= 0:
                break
            filled += num_filled
            funds -= alloc
        return filled
