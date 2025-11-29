# Time:  O(min(m, n)^2 * max(m, n) * log(max(m, n)))
# Space: O(max(m, n))

from bisect import bisect_left, insort

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        """
        if not matrix:
            return 0

        m = min(len(matrix), len(matrix[0]))
        n = max(len(matrix), len(matrix[0]))
        result = float("-inf")

        for i in range(m):
            sums = [0] * n
            for j in range(i, m):
                for l in range(n):
                    sums[l] += matrix[j][l] if m == len(matrix) else matrix[l][j]

                # Find the max subarray no more than K.
                accu_sum_set, accu_sum = [0], 0
                for sum in sums:
                    accu_sum += sum
                    it = bisect_left(accu_sum_set, accu_sum - k)  # Time: O(logn)
                    if it != len(accu_sum_set):
                        result = max(result, accu_sum - accu_sum_set[it])
                    insort(accu_sum_set, accu_sum)  # Time: O(n)

        return result


