class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        digits = []
        temp = target
        while temp:
            digits.append(temp % x)
            temp //= x
        positive = 0
        negative = 0
        level = 0
        for rem in digits:
            if level == 0:
                positive = 2 * rem
                negative = 2 * (x - rem)
            else:
                new_pos = min(rem * level + positive, (rem + 1) * level + negative)
                new_neg = min((x - rem) * level + positive, (x - rem - 1) * level + negative)
                positive = new_pos
                negative = new_neg
            level += 1
        return min(positive, level + negative) - 1
