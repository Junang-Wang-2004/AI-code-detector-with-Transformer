class Solution(object):
    def countCollisions(self, directions):
        n = len(directions)
        moving = 0
        for char in directions:
            if char != 'S':
                moving += 1
        pref = 0
        while pref < n and directions[pref] == 'L':
            pref += 1
        suff = 0
        pos = n - 1
        while pos >= 0 and directions[pos] == 'R':
            suff += 1
            pos -= 1
        return moving - pref - suff
