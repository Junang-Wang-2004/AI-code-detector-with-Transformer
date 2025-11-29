# Time:  O(logn)
# Space: O(1)
class Solution2(object):
    def baseNeg2(self, N):
        """
        """
        BASE = -2
        result = []
        while N:
            N, r = divmod(N, BASE)
            if r < 0:
                r -= BASE
                N += 1
            result.append(str(r))
        result.reverse()
        return "".join(result) if result else "0"
