# Time:  O(n * m * l), n is the number of patterns
#                    , l is the max length of patterns
#                    , m is the length of word
# Space: O(1)
# built-in solution
class Solution3(object):
    def numOfStrings(self, patterns, word):
        return sum(pattern in word for pattern in patterns)
