# Time:  O(max(logk, x) * (max(logk, x) / x))
# Space: O(1)
# bit manipulation, binary search, combinatorics
class Solution4(object):
    def findMaximumNumber(self, k, x):
        """
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def count(v):
            cnt = i = 0
            while 1<<(i+x-1) <= v:
                q, r = divmod(v+1, 1<<((i+x-1)+1))
                cnt += q*1*(1<<(i+x-1))+max(r-1*(1<<(i+x-1)), 0)
                i += x
            return cnt

        return binary_search_right(1, max(k<<2, 1<<x), lambda v: count(v) <= k)  # right bound is verified by checking all possible (k, v) values, or just set right = solution.findMaximumNumber(10**15, 8) <= 10**15
