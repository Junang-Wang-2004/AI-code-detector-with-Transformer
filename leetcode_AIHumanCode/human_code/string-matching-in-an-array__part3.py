# Time:  O(n^2 * l^2), n is the number of strings
# Space: O(1)        , l is the max length of strings
class Solution3(object):
    def stringMatching(self, words):
        """
        """
        result = []
        for i, pattern in enumerate(words):
            for j, text in enumerate(words):
                if i != j and pattern in text:
                    result.append(pattern)
                    break
        return result
