# Time:  O(m * n)
# Space: O(m * n)

import collections


class Solution2(object):
    def findBlackPixel(self, picture, N):
        """
        """
        lookup = collections.Counter(list(map(tuple, picture)))
        cols = [col.count('B') for col in zip(*picture)]
        return sum(N * list(zip(row, cols)).count(('B', N)) \
                   for row, cnt in lookup.items() \
                   if cnt == N == row.count('B'))

