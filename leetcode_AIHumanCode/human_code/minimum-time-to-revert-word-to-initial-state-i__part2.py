# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
    def minimumTimeToInitialState(self, word, k):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        for i in range(k, len(word), k):
            if all(word[i+j] == word[j] for j in range(len(word)-i)):
                return i//k
        return ceil_divide(len(word), k)
