# Time:  O(n * logr * (logn * logr)) = O(n * (logr)^2 * logn), r = max(nums)
# Space: O(nlogn)
# number theory, binary search, rmq, sparse table, prefix sum
class Solution3_TLE(object):
    def maxGcdSum(self, nums, k):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        # RMQ - Sparse Table
        # Template: https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds/blob/main/Round%20D/genetic_sequences2.py3
