# Time:  (m * n grids) * (O(3*3*2^(m-2)) possible states per grid) = O(n * m * 2^m)
# Space: O(3*3*2^(m-2)) = O(2^m)
import collections


# better complexity for large m, large n
class Solution3(object):
    def colorTheGrid(self, m, n):
        """
        """
        MOD = 10**9+7
        def normalize(basis, mask, lookup):  # compute and cache, at most O(3*2^(m-3)) time and space
            if mask not in lookup[basis]:
                norm = {}
                result, b = 0, basis
                while b:
                    x = mask//b%3
                    if x not in norm:
                        norm[x] = len(norm)
                    result += norm[x]*b
                    b //= 3
                lookup[basis][mask] = result
            return lookup[basis][mask]

        if m > n:
            m, n = n, m
        basis = b = 3**(m-1)
        lookup = collections.defaultdict(dict)
        dp = collections.Counter({0: 1})
        for idx in range(m*n):
            r, c = divmod(idx, m)
            # sliding window with size m doesn't cross rows:
            #   [3, 2, ..., 2] => 3*2^(m-1) combinations
            assert(r != 0 or c != 0 or len(dp) == 1)
            assert(r != 0 or c == 0 or len(dp) == 3*2**(c-1) // 3 // (2 if c >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
            assert(r == 0 or c != 0 or len(dp) == 3*2**(m-1) // 3 // (2 if m >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
            # sliding window with size m crosses rows:
            #   [*, ..., *, *, 3, 2, ..., 2] => 3*3 * 2^(m-2) combinations
            #   [2, ..., 2, 3, *, *, ..., *]
            assert(r == 0 or c == 0 or len(dp) == (1 if m == 1 else 2 if m == 2 else 3*3 * 2**(m-2) // 3 // 2))  # divided by 3 * 2 for m >= 3 is since the first two colors of window are normalized to speed up performance
            new_dp = collections.Counter()
            for mask, v in dp.items():
                choices = {0, 1, 2}
                if r > 0:
                    choices.discard(mask%3)  # get up grid
                if c > 0:
                    choices.discard(mask//basis)  # get left grid
                for x in choices:
                    new_mask = normalize(basis//b, ((x*basis)+(mask//3))//b, lookup)*b  # encoding mask
                    new_dp[new_mask] = (new_dp[new_mask]+v)%MOD
            if b > 1:
                b //= 3
            dp = new_dp
        return reduce(lambda x,y: (x+y)%MOD, iter(dp.values()), 0)  # Time: O(2^m)
