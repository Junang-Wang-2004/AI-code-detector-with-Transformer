# Time:  O(n^3), n is the length of A
# Space: O(n^2)
import collections


class Solution2(object):
    def countTriplets(self, A):
        """
        """
        count = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(len(A)):
                count[A[i]&A[j]] += 1
        result = 0
        for k in range(len(A)):
            for v in count:
                if A[k]&v == 0:
                    result += count[v]
        return result
