# Time:  O(n)
# Space: O(n)
import itertools


class Solution2(object):
    def maxRepOpt1(self, text):
        """
        """
        A = [[c, len(list(group))] for c, group in itertools.groupby(text)]
        total_count = collections.Counter(text)
        result = max(min(l+1, total_count[c]) for c, l in A)
        for i in range(1, len(A)-1):
            if A[i-1][0] == A[i+1][0] and A[i][1] == 1:
                result = max(result, min(A[i-1][1] + 1 + A[i+1][1], total_count[A[i+1][0]]))
        return result
