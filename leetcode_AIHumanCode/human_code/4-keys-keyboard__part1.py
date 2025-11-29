# Time:  O(1)
# Space: O(1)


class Solution(object):
    def maxA(self, N):
        """
        """
        if N < 7:
            return N
        if N == 10:
            return 20  # the following rule doesn't hold when N = 10

        n = N // 5 + 1  # n3 + n4 increases one every 5 keys
        # (1) n     =     n3 +     n4
        # (2) N + 1 = 4 * n3 + 5 * n4
        #     5 x (1) - (2) => 5*n - N - 1 = n3
        n3 = 5*n - N - 1
        n4 = n - n3
        return 3**n3 * 4**n4


