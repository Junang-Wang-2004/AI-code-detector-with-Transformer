# Time:  O(m * n)
# Space: O(m * n)
class Solution2(object):
    def placeWordInCrossword(self, board, word):
        """
        """
        words = [word, word[::-1]]
        for mat in (board, list(zip(*board))):
            for row in mat:
                blocks = ''.join(row).split('#')
                for s in blocks:
                    if len(s) != len(word):
                        continue
                    for w in words:
                        if all(s[i] in (w[i], ' ') for i in range(len(s))):
                            return True
        return False
