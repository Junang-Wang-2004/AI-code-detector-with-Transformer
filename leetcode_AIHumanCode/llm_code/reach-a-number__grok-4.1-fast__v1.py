class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        position = 0
        step = 0
        while True:
            step += 1
            position += step
            if position >= target and (position - target) % 2 == 0:
                return step
