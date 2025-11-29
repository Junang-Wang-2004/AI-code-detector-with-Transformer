class Solution(object):
    def countQuadruples(self, firstString, secondString):
        minpos = [-1] * 26
        for pos, ch in enumerate(firstString):
            i = ord(ch) - ord('a')
            if minpos[i] == -1:
                minpos[i] = pos
        maxpos = [-1] * 26
        for pos, ch in enumerate(secondString):
            i = ord(ch) - ord('a')
            maxpos[i] = pos
        differences = []
        for i in range(26):
            if minpos[i] != -1 and maxpos[i] != -1:
                differences.append(minpos[i] - maxpos[i])
        if not differences:
            return 0
        smallest = min(differences)
        return differences.count(smallest)
