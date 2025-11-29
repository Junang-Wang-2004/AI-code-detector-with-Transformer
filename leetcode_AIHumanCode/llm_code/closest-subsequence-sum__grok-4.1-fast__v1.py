import bisect

class Solution:
    def minAbsDifference(self, nums, goal):
        max_sum = sum(x for x in nums if x > 0)
        min_sum = sum(x for x in nums if x < 0)
        if goal > max_sum:
            return goal - max_sum
        if goal < min_sum:
            return min_sum - goal
        split = len(nums) // 2
        part1 = nums[:split]
        part2 = nums[split:]

        def all_sums(parts):
            totals = [0]
            for num in parts:
                extras = [t + num for t in totals]
                totals.extend(extras)
            return totals

        sorted_part1 = sorted(all_sums(part1))
        part2_sums = all_sums(part2)
        closest = abs(goal)
        for p2 in part2_sums:
            seek = goal - p2
            insert = bisect.bisect_left(sorted_part1, seek)
            if insert < len(sorted_part1):
                closest = min(closest, abs(sorted_part1[insert] - seek))
            if insert > 0:
                closest = min(closest, abs(sorted_part1[insert - 1] - seek))
            if closest == 0:
                return 0
        return closest
