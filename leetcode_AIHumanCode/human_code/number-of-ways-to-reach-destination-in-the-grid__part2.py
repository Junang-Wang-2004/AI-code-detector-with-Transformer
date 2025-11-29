# Time:  O(n)
# Space: O(1)
# dp
class Solution2(object):
    def numberOfWays(self, n, m, k, source, dest):
        """
        """
        MOD = 10**9+7
        both_same = row_same = col_same = no_same = 0
        if source == dest:
            both_same = 1
        elif source[0] == dest[0]:
            row_same = 1
        elif source[1] == dest[1]:
            col_same = 1
        else:
            no_same = 1
        for _ in range(k):
            both_same, row_same, col_same, no_same = (row_same+col_same)%MOD, (both_same*(m-1)+row_same*(m-2)+no_same)%MOD, (both_same*(n-1)+col_same*(n-2)+no_same)%MOD, (row_same*(n-1)+col_same*(m-1)+no_same*((n-2)+(m-2)))%MOD
        return both_same
