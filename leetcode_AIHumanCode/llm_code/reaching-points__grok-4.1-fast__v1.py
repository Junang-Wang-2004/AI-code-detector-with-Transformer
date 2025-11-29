class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if ty == sy and (tx - sx) % ty == 0:
                return True
            if tx == sx and (ty - sy) % tx == 0:
                return True
            if tx >= ty:
                tx %= ty
            else:
                ty %= tx
        return False
