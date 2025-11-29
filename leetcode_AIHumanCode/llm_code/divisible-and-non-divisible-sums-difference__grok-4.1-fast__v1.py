class Solution:
    def differenceOfSums(self, n, m):
        overall_sum = n * (n + 1) // 2
        num_multiples = n // m
        multiples_total = m * num_multiples * (num_multiples + 1) // 2
        return overall_sum - 2 * multiples_total
