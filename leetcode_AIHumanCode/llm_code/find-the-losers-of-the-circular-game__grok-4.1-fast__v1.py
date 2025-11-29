class Solution(object):
    def circularGameLosers(self, n, k):
        eliminated = set()
        pos = 0
        factor = 1
        while pos not in eliminated:
            eliminated.add(pos)
            pos = (pos + factor * k) % n
            factor += 1
        return [i + 1 for i in range(n) if i not in eliminated]
