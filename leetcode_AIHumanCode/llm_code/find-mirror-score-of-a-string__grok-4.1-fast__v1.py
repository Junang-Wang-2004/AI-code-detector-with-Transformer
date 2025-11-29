class Solution(object):
    def calculateScore(self, s):
        score = 0
        base = ord('a')
        for p in range(13):
            q = 25 - p
            opens = []
            closes = []
            for j, c in enumerate(s):
                k = ord(c) - base
                if k == p:
                    if closes:
                        score += j - closes.pop()
                    else:
                        opens.append(j)
                elif k == q:
                    if opens:
                        score += j - opens.pop()
                    else:
                        closes.append(j)
        return score
