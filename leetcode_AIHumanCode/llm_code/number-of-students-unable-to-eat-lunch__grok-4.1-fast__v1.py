class Solution:
    def countStudents(self, pupils, buns):
        req = [pupils.count(0), pupils.count(1)]
        idx = 0
        n = len(buns)
        while idx < n and req[buns[idx]] > 0:
            req[buns[idx]] -= 1
            idx += 1
        return n - idx
