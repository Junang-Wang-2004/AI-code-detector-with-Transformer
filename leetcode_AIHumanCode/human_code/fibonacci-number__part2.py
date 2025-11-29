# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def fib(self, N):
        """
        """
        prev, current = 0, 1
        for i in range(N):
            prev, current = current, prev + current,
        return prev
