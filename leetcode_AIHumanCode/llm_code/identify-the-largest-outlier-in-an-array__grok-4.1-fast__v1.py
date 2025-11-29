class Solution:
    def getLargestOutlier(self, nums):
        overall_sum = 0
        occurrences = {}
        for number in nums:
            overall_sum += number
            occurrences[number] = occurrences.get(number, 0) + 1
        possible_outliers = sorted(occurrences, reverse=True)
        for outlier in possible_outliers:
            leftover_sum = overall_sum - outlier
            if leftover_sum % 2 != 0:
                continue
            target_sum = leftover_sum // 2
            deduction = 1 if target_sum == outlier else 0
            if target_sum in occurrences and occurrences[target_sum] >= 1 + deduction:
                return outlier
        return float('-inf')
