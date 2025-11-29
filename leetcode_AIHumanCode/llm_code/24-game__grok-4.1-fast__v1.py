from fractions import Fraction

class Solution:
    def judgePoint24(self, nums):
        def possible(pile):
            if len(pile) == 1:
                return pile[0] == Fraction(24)
            for i in range(len(pile)):
                for j in range(i + 1, len(pile)):
                    others = pile[:i] + pile[i + 1:j] + pile[j + 1:]
                    x, y = pile[i], pile[j]
                    if possible(others + [x + y]):
                        return True
                    if possible(others + [x * y]):
                        return True
                    if possible(others + [x - y]):
                        return True
                    if possible(others + [y - x]):
                        return True
                    if y != 0 and possible(others + [x / y]):
                        return True
                    if x != 0 and possible(others + [y / x]):
                        return True
            return False

        return possible([Fraction(val) for val in nums])
