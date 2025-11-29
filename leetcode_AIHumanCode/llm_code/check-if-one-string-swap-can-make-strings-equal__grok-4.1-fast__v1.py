class Solution(object):
    def areAlmostEqual(self, word1, word2):
        positions = []
        for idx in range(len(word1)):
            if word1[idx] != word2[idx]:
                positions.append(idx)
                if len(positions) > 2:
                    return False
        if len(positions) == 0:
            return True
        if len(positions) != 2:
            return False
        p, q = positions
        return word1[p] == word2[q] and word1[q] == word2[p]
